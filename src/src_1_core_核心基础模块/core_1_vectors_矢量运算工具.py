# 矢量运算工具
import numpy as np
from typing import Union, List


class Vector3D:
    """三维矢量类，支持基本运算与物理量表示"""

    def __init__(self, x: float, y: float, z: float = 0):
        self.components = np.array([x, y, z], dtype=np.float64)

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(*(self.components + other.components))

    def __sub__(self, other: 'Vector3D') -> 'Vector3D':
        return Vector3D(*(self.components - other.components))

    def __mul__(self, scalar: float) -> 'Vector3D':
        return Vector3D(*(self.components * scalar))

    def __truediv__(self, scalar: float) -> 'Vector3D':
        return Vector3D(*(self.components / scalar))

    def dot(self, other: 'Vector3D') -> float:
        """矢量点积"""
        return np.dot(self.components, other.components)

    def cross(self, other: 'Vector3D') -> 'Vector3D':
        """矢量叉积"""
        return Vector3D(*np.cross(self.components, other.components))

    def magnitude(self) -> float:
        """矢量模长"""
        return np.linalg.norm(self.components)

    def unit_vector(self) -> 'Vector3D':
        """单位矢量"""
        mag = self.magnitude()
        return Vector3D(*(self.components / mag)) if mag != 0 else Vector3D(0, 0, 0)

    def rotate(self, axis: 'Vector3D', theta: float) -> 'Vector3D':
        """绕任意轴旋转（使用罗德里格斯公式）"""
        axis = axis.unit_vector().components
        cos_t = np.cos(theta)
        sin_t = np.sin(theta)
        # 罗德里格斯旋转矩阵
        rot_matrix = (
                cos_t * np.eye(3) +
                (1 - cos_t) * np.outer(axis, axis) +
                sin_t * np.array([
            [0, -axis[2], axis[1]],
            [axis[2], 0, -axis[0]],
            [-axis[1], axis[0], 0]
        ])
        )
        return Vector3D(*np.dot(rot_matrix, self.components))

    def to_polar(self) -> tuple:
        """转换为极坐标系（仅适用于二维情况）"""
        if self.components[2] != 0:
            raise ValueError("三维矢量需先投影到平面")
        r = self.magnitude()
        theta = np.arctan2(self.components[1], self.components[0])
        return (r, theta)

    def __repr__(self):
        return f"Vector3D({self.components[0]:.2f}, {self.components[1]:.2f}, {self.components[2]:.2f})"