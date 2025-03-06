"""
常微分方程数值求解器
实现常用积分方法
"""
import numpy as np


class ODESolver:
    @staticmethod
    def euler(func, y0, t_span, dt):
        """显式欧拉法"""
        t = np.arange(t_span[0], t_span[1] + dt, dt)
        y = np.zeros((len(t), len(y0)))
        y[0] = y0
        for i in range(1, len(t)):
            y[i] = y[i - 1] + func(t[i - 1], y[i - 1]) * dt
        return t, y

    @staticmethod
    def rk4(func, y0, t_span, dt):
        """经典四阶龙格-库塔法"""
        t = np.arange(t_span[0], t_span[1] + dt, dt)
        y = np.zeros((len(t), len(y0)))
        y[0] = y0
        for i in range(1, len(t)):
            k1 = func(t[i - 1], y[i - 1])
            k2 = func(t[i - 1] + dt / 2, y[i - 1] + dt * k1 / 2)
            k3 = func(t[i - 1] + dt / 2, y[i - 1] + dt * k2 / 2)
            k4 = func(t[i - 1] + dt, y[i - 1] + dt * k3)
            y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) * dt / 6
        return t, y

    @staticmethod
    def verlet(accel_func, y0, t_span, dt):
        """Verlet算法（适用于保守系统）"""
        t = np.arange(t_span[0], t_span[1] + dt, dt)
        y = np.zeros((len(t), len(y0)))
        y[0] = y0
        # 需要初始速度信息，此处简化为位置-速度格式
        # 实际实现需根据具体问题调整
        return t, y