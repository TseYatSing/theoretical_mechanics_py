"""
质点运动学分析
支持直角坐标系、极坐标系、自然坐标系
包含运动轨迹计算与参数化描述
"""
import numpy as np
from scipy.integrate import odeint
from typing import Callable, Optional


class Particle:
    def __init__(self, position: np.ndarray, velocity: np.ndarray):
        """
        :param position: 初始位置 [x, y, z] (单位:m)
        :param velocity: 初始速度 [vx, vy, vz] (单位:m/s)
        """
        self.state = np.concatenate([position, velocity])
        self.time = 0.0

    @property
    def position(self) -> np.ndarray:
        return self.state[:3]

    @property
    def velocity(self) -> np.ndarray:
        return self.state[3:]

    def cartesian_acceleration(self,
                               acceleration_func: Callable[[np.ndarray, float], np.ndarray],
                               t_end: float,
                               dt: float = 0.01) -> np.ndarray:
        """
        计算直角坐标系下的运动轨迹（数值积分）
        :param acceleration_func: 加速度函数 a(r,v,t)
        :param t_end: 模拟总时长
        :param dt: 时间步长
        :return: 轨迹数组 [[t, x, y, z, vx, vy, vz], ...]
        """
        t = np.arange(0, t_end + dt, dt)

        def state_deriv(y, t):
            r = y[:3]
            v = y[3:]
            a = acceleration_func(r, v, t)
            return np.concatenate([v, a])

        trajectory = odeint(state_deriv, self.state, t)
        return np.column_stack([t, trajectory])

    def polar_coordinates(self) -> tuple:
        """转换为极坐标系(r, θ)（二维情况）"""
        x, y = self.position[:2]
        r = np.hypot(x, y)
        theta = np.arctan2(y, x)
        return r, theta

    def normal_tangential_acceleration(self,
                                       curvature: float) -> tuple:
        """
        计算切向和法向加速度
        :param curvature: 轨迹曲率半径 (单位:m)
        :return: (a_t, a_n)
        """
        v = np.linalg.norm(self.velocity)
        a_t = np.dot(self.acceleration, self.velocity) / v if v != 0 else 0
        a_n = (v ** 2) / curvature if curvature != 0 else 0
        return a_t, a_n


# 示例：抛物线运动模拟
def projectile_motion():
    g = 9.81

    def acceleration(r, v, t):
        return np.array([0, -g, 0])

    p = Particle([0, 0, 0], [20, 30, 0])
    trajectory = p.cartesian_acceleration(acceleration, t_end=6)
    return trajectory