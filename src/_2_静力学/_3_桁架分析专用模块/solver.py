from src._2_静力学._3_桁架分析专用模块.truss_model import TrussModel

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import spsolve

def solve_truss(model: TrussModel) -> dict:
    """
    求解桁架内力（节点法）
    返回: {member_id: force_value}
    """
    # 构建全局刚度矩阵
    n_nodes = len(model.nodes)
    total_dof = 2 * n_nodes
    K = np.zeros((total_dof, total_dof))
    F = np.zeros(total_dof)

    # 组装荷载向量
    for node_id, load in model.loads.items():
        idx = 2 * node_id
        F[idx:idx + 2] = load

    # 组装刚度矩阵
    for member in model.members.values():
        n1 = model.nodes[member.start_node]
        n2 = model.nodes[member.end_node]
        L = np.hypot(n2.x - n1.x, n2.y - n1.y)
        c = (n2.x - n1.x) / L
        s = (n2.y - n1.y) / L
        k_local = (member.E * member.A / L) * np.array([
            [ c*c,  c*s, -c*c, -c*s],
            [ c*s,  s*s, -c*s, -s*s],
            [-c*c, -c*s,  c*c,  c*s],
            [-c*s, -s*s,  c*s,  s*s]
        ])
        dof_indices = [2*n1.id, 2*n1.id+1, 2*n2.id, 2*n2.id+1]
        for i in range(4):
            for j in range(4):
                K[dof_indices[i], dof_indices[j]] += k_local[i, j]

    # 处理约束
    constrained_dof = []
    for node in model.nodes.values():
        if node.is_supported:
            idx = 2 * node.id
            if node.support_type == 'pin':
                constrained_dof.extend([idx, idx + 1])
            elif node.support_type == 'roller':
                constrained_dof.append(idx)  # 假设水平滚动支座

    # 打印约束信息
    print(f"约束自由度: {constrained_dof}")

    # 求解方程组
    free_dof = [i for i in range(total_dof) if i not in constrained_dof]
    K_free = csr_matrix(K[np.ix_(free_dof, free_dof)])  # 转换为CSR格式
    F_free = F[free_dof]

    # 打印自由度信息
    print(f"自由自由度: {free_dof}")
    print(f"K_free: {K_free}")
    print(f"F_free: {F_free}")

    U = np.zeros(total_dof)
    U[free_dof] = spsolve(K_free, F_free)

    # 计算杆件内力
    forces = {}
    for member in model.members.values():
        n1 = model.nodes[member.start_node]
        n2 = model.nodes[member.end_node]
        L = np.hypot(n2.x - n1.x, n2.y - n1.y)
        c = (n2.x - n1.x) / L
        s = (n2.y - n1.y) / L
        u = U[2 * n1.id:2 * n1.id + 2]
        v = U[2 * n2.id:2 * n2.id + 2]
        delta = (v[0] - u[0]) * c + (v[1] - u[1]) * s
        force = (member.E * member.A / L) * delta
        forces[member.id] = force

    return forces