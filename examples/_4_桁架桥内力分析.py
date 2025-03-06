# examples/statics/truss_bridge_demo.py
from src._2_静力学._3_桁架分析专用模块 import TrussModel, Node, Member, solve_truss
import numpy as np

# 创建简支桁架模型
model = TrussModel()

# 创建节点 (单位：米)
model.add_node(Node(0, 0, 0, is_supported=True, support_type='pin'))    # 左支座
model.add_node(Node(1, 8, 0, is_supported=True, support_type='roller')) # 右支座
model.add_node(Node(2, 2, 3))
model.add_node(Node(3, 6, 3))

# 创建杆件
model.add_member(Member(0, 0, 2))
model.add_member(Member(1, 0, 3))
model.add_member(Member(2, 1, 3))
model.add_member(Member(3, 1, 2))
model.add_member(Member(4, 2, 3))

# 打印节点和杆件信息以进行调试
print("节点信息:")
for node in model.nodes.values():
    print(f"节点{node.id}: ({node.x}, {node.y}), 支座: {node.is_supported}, 类型: {node.support_type}")

print("\n杆件信息:")
for member in model.members.values():
    print(f"杆件{member.id}: 节点{member.start_node} -> 节点{member.end_node}")

# 施加荷载 (集中力10kN)
model.apply_load(2, np.array([0, -1e4]))  # 节点2竖向力
model.apply_load(3, np.array([0, -1e4]))  # 节点3竖向力

# 求解内力
forces = solve_truss(model)

# 打印结果
print("\n杆件内力分析结果 (单位：N):")
for member_id, force in forces.items():
    print(f"杆件{member_id}: {force:.1f} ({'受拉' if force > 0 else '受压'})")

# 可视化桁架
# from src.visualization.plot_2d import plot_truss
# plot_truss(model, forces)  # 需实现此绘图函数