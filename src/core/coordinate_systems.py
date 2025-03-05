# 坐标系转换
import numpy as np
from sympy import symbols, sin, cos, Matrix
from typing import Tuple


class CoordinateTransform:
    """坐标系转换工具类"""

    @staticmethod
    def cartesian_to_spherical(x: float, y: float, z: float) -> Tuple[float, float, float]:
        """笛卡尔坐标转球坐标 (r, theta, phi)"""
        r = np.sqrt(x ** 2 + y ** 2 + z ** 2)
        theta = np.arccos(z / r) if r != 0 else 0
        phi = np.arctan2(y, x)
        return (r, theta, phi)

    @staticmethod
    def spherical_to_cartesian(r: float, theta: float, phi: float) -> Tuple[float, float, float]:
        """球坐标转笛卡尔坐标"""
        x = r * sin(theta) * cos(phi)
        y = r * sin(theta) * sin(phi)
        z = r * cos(theta)
        return (x, y, z)

    @staticmethod
    def rotation_matrix(axis: str, angle: float) -> Matrix:
        """生成符号旋转矩阵（SymPy 符号运算）"""
        theta = symbols('theta')
        if axis == 'x':
            return Matrix([
                [1, 0, 0],
                [0, cos(theta), -sin(theta)],
                [0, sin(theta), cos(theta)]
            ]).subs(theta, angle)
        elif axis == 'y':
            return Matrix([
                [cos(theta), 0, sin(theta)],
                [0, 1, 0],
                [-sin(theta), 0, cos(theta)]
            ]).subs(theta, angle)
        elif axis == 'z':
            return Matrix([
                [cos(theta), -sin(theta), 0],
                [sin(theta), cos(theta), 0],
                [0, 0, 1]
            ]).subs(theta, angle)

    @staticmethod
    def euler_angles_rotation(angles: Tuple[float, float, float], order: str = 'zyx') -> Matrix:
        """欧拉角旋转矩阵生成器"""
        # 实现不同旋转顺序的组合
        pass  # 具体实现可根据需求扩展


class ReferenceFrame:
    """参考坐标系管理类"""

    def __init__(self, name: str, parent=None):
        self.name = name
        self.parent = parent
        self.rotation_matrix = np.eye(3)

    def transform_vector(self, vector: np.ndarray) -> np.ndarray:
        """将矢量转换到父坐标系"""
        if self.parent is None:
            return vector
        return self.rotation_matrix.T @ vector

    def add_rotation(self, axis: str, angle: float):
        """累积旋转操作"""
        rot_map = {
            'x': np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]]),
            'y': np.array([[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]]),
            'z': np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
        }
        self.rotation_matrix = rot_map[axis] @ self.rotation_matrix