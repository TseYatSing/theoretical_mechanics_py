"""
静力平衡问题求解器
包含：
- 平衡条件判断
- 约束反力求解
- 超静定识别
"""
import numpy as np
from scipy.linalg import null_space
from .force_system import ForceSystem


class EquilibriumSolver:
    def __init__(self, force_system: ForceSystem):
        self.system = force_system
        self.A = None  # 系数矩阵
        self.b = None  # 常数项

    def is_in_equilibrium(self, tolerance=1e-6) -> bool:
        """判断当前力系是否平衡"""
        R = self.system.resultant_force
        M = self.system.resultant_moment(np.zeros(self.system.dimension))
        return (
                np.allclose(R, 0, atol=tolerance) and
                np.allclose(M, 0, atol=tolerance)
        )

    def build_equations(self, unknowns: List[Tuple[int, int]]):
        """
        构建平衡方程组 Ax = b
        :param unknowns: 未知力位置列表 [(force_index, component_index), ...]
        """
        # 示例：二维系统构建三个方程
        if self.system.dimension == 2:
            self.A = np.zeros((3, len(unknowns)))
            self.b = np.zeros(3)

            # 遍历每个力生成方程
            for i, force in enumerate(self.system.forces):
                for j, (f_idx, comp) in enumerate(unknowns):
                    if i == f_idx:
                        if comp == 0:  # Fx
                            self.A[0, j] = 1
                        elif comp == 1:  # Fy
                            self.A[1, j] = 1
                        # 力矩项
                        self.A[2, j] = force.point[0] * force.vector[1] - force.point[1] * force.vector[0]

    def solve_static(self) -> dict:
        """求解静定问题"""
        if self.A is None:
            raise RuntimeError("需要先构建方程组")

        if self.A.shape[0] != self.A.shape[1]:
            raise ValueError("超静定问题，需要额外约束条件")

        x = np.linalg.solve(self.A, -self.b)
        return {f"unknown_{i}": val for i, val in enumerate(x)}

    def check_redundancy(self):
        """检查超静定次数"""
        rank = np.linalg.matrix_rank(self.A)
        return self.A.shape[1] - rank
