"""
力系分析与操作工具
包含力的合成、力矩计算、主矢主矩计算
支持二维和三维力系
"""
import numpy as np
from typing import List, Tuple


class Force:
    def __init__(self, vector: np.ndarray, point: np.ndarray):
        """
        :param vector: 力矢量 [Fx, Fy, (Fz)]
        :param point: 作用点坐标 [x, y, (z)]
        """
        self.vector = np.array(vector)
        self.point = np.array(point)

    def moment_about(self, origin: np.ndarray) -> np.ndarray:
        """计算对某点的力矩"""
        r = self.point - origin
        return np.cross(r, self.vector)


class ForceSystem:
    def __init__(self, dimension: int = 3):
        self.forces: List[Force] = []
        self.dimension = dimension  # 2 或 3维

    def add_force(self, force: Force):
        """添加力到力系"""
        if force.vector.size != self.dimension:
            raise ValueError("力的维度与系统不匹配")
        self.forces.append(force)

    @property
    def resultant_force(self) -> np.ndarray:
        """计算主矢"""
        return sum(f.vector for f in self.forces)

    def resultant_moment(self, origin: np.ndarray) -> np.ndarray:
        """计算对某点的主矩"""
        return sum(f.moment_about(origin) for f in self.forces)

    def reduce_to_point(self, point: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        将力系简化为某点的等效力和力偶
        返回: (主矢, 主矩)
        """
        return self.resultant_force, self.resultant_moment(point)

    def as_matrix(self) -> np.ndarray:
        """将力系转换为矩阵形式(用于平衡方程求解)"""
        if self.dimension == 2:
            # 二维: [Fx, Fy, Mz]
            return np.array([
                [f.vector[0], f.vector[1], f.moment_about([0, 0])[2]]
                for f in self.forces
            ])
        else:
            # 三维: [Fx, Fy, Fz, Mx, My, Mz]
            raise NotImplementedError("三维矩阵形式待实现")
