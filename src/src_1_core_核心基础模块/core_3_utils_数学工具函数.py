# 数学工具函数
import numpy as np
from scipy.integrate import simpson
from sympy import symbols, Function, diff


class MathUtils:
    """通用数学工具集合"""

    @staticmethod
    def numerical_integrate(f, a: float, b: float, n: int = 1000, method: str = 'trapezoid') -> float:
        """数值积分工具"""
        x = np.linspace(a, b, n)
        y = f(x)
        if method == 'trapezoid':
            return np.trapz(y, x)
        elif method == 'simpson':
            return simpson(y, x)
        else:
            raise ValueError("Unsupported integration method")

    @staticmethod
    def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
        """解线性方程组 Ax = b"""
        return np.linalg.solve(A, b)

    @staticmethod
    def rk4_step(f, t: float, y: np.ndarray, dt: float) -> np.ndarray:
        """四阶龙格-库塔法单步计算"""
        k1 = f(t, y)
        k2 = f(t + dt / 2, y + dt * k1 / 2)
        k3 = f(t + dt / 2, y + dt * k2 / 2)
        k4 = f(t + dt, y + dt * k3)
        return y + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6


class SymbolicTools:
    """符号计算辅助工具"""

    @staticmethod
    def define_symbols(vars: str) -> tuple:
        """快速定义符号变量：'x y z' -> (x, y, z)"""
        return symbols(vars)

    @staticmethod
    def lagrangian_derivative(L, q: Function, t: symbols) -> dict:
        """自动计算拉格朗日方程项"""
        dL_dq = diff(L, q)
        dL_dqdot = diff(L, diff(q(t), t))
        d_dt_dL_dqdot = diff(dL_dqdot, t)
        return {'equation': d_dt_dL_dqdot - dL_dq, 'terms': (dL_dq, dL_dqdot)}