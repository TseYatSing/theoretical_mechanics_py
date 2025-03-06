"""
牛顿力学动量定理实现
包含动量守恒判断、冲量计算
"""
import numpy as np
from typing import List, Tuple


class NewtonianSystem:
    def __init__(self, masses: List[float]):
        """
        :param masses: 各质点质量列表 [m1, m2,...] (单位:kg)
        """
        self.masses = np.array(masses)
        self.velocities = np.zeros((len(masses), 3))  # 每个质点的速度

    def apply_impulse(self, index: int, impulse: np.ndarray):
        """施加冲量到指定质点"""
        self.velocities[index] += impulse / self.masses[index]

    def total_momentum(self) -> np.ndarray:
        """计算系统总动量"""
        return np.sum(self.masses[:, None] * self.velocities, axis=0)

    def check_conservation(self, initial_momentum: np.ndarray,
                           tolerance: float = 1e-6) -> bool:
        """检查动量是否守恒"""
        current = self.total_momentum()
        return np.allclose(current, initial_momentum, atol=tolerance)


def collision_2d(m1: float, v1: np.ndarray,
                 m2: float, v2: np.ndarray,
                 e: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    二维完全弹性碰撞计算
    :param e: 恢复系数 (e=1为完全弹性)
    :return: (v1_final, v2_final)
    """
    # 转换为质心系
    v_cm = (m1 * v1 + m2 * v2) / (m1 + m2)
    v1_rel = v1 - v_cm
    v2_rel = v2 - v_cm

    # 碰撞后相对速度反向并缩放
    v1_rel_new = -e * v1_rel
    v2_rel_new = -e * v2_rel

    # 转换回原参考系
    return (v1_rel_new + v_cm, v2_rel_new + v_cm)