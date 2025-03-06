"""
机械能守恒分析
包含动能/势能计算、守恒条件判断
"""
import numpy as np


class EnergyAnalyzer:
    def __init__(self, masses, gravity=9.81):
        self.masses = np.array(masses)
        self.gravity = gravity
        self.positions = None  # 需外部更新位置数据
        self.velocities = None

    def kinetic_energy(self) -> float:
        """计算总动能"""
        return 0.5 * np.sum(self.masses * np.linalg.norm(self.velocities, axis=1) ** 2)

    def gravitational_potential(self, ref_height: float = 0) -> float:
        """计算重力势能（相对于参考高度）"""
        heights = self.positions[:, 1] - ref_height
        return np.sum(self.masses * self.gravity * heights)

    def spring_potential(self, k: float, equilibrium_pos: np.ndarray) -> float:
        """弹簧势能计算"""
        displacements = np.linalg.norm(self.positions - equilibrium_pos, axis=1)
        return 0.5 * k * np.sum(displacements ** 2)

    def mechanical_energy(self, **potential_args) -> float:
        """计算总机械能"""
        return self.kinetic_energy() + self.gravitational_potential(**potential_args)