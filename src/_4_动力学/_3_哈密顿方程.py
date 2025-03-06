"""
哈密顿力学实现
包含勒让德变换、正则方程推导
"""
from sympy import symbols, diff, Matrix, simplify
from src._4_动力学._2_拉格朗日方程 import LagrangianSystem


class HamiltonianSystem(LagrangianSystem):
    def __init__(self, dof: int):
        super().__init__(dof)
        self.p = [symbols(f'p{i}') for i in range(self.N)]  # 广义动量

    def legendre_transform(self):
        """执行勒让德变换生成哈密顿量"""
        if self.L is None:
            raise ValueError("需要先定义拉格朗日量")

        # 计算广义动量 p = ∂L/∂qdot
        p = [diff(self.L, qd) for qd in self.qdot]

        # 表达式替换：用p表示qdot
        substitutions = {}
        H = 0
        for i in range(self.N):
            qd_expr = self.solve_qdot(p[i])
            substitutions[self.qdot[i]] = qd_expr
            H += self.p[i] * qd_expr

        H -= self.L.subs(substitutions)
        return H

    def canonical_equations(self):
        """推导正则方程"""
        H = self.legendre_transform()
        equations = []
        for i in range(self.N):
            dqdt = diff(H, self.p[i])
            dpdt = -diff(H, self.q[i])
            equations.extend([dqdt, dpdt])
        return equations


# 示例：谐振子系统
def harmonic_oscillator_example():
    t, m, k = symbols('t m k')
    q = Function('q')(t)
    p = symbols('p')

    # 哈密顿量 H = p²/(2m) + 0.5k q²
    H_expr = p ** 2 / (2 * m) + 0.5 * k * q ** 2

    # 正则方程
    dqdt = diff(H_expr, p)  # dq/dt = p/m
    dpdt = -diff(H_expr, q)  # dp/dt = -k q

    print(f"正则方程: dq/dt = {dqdt}, dp/dt = {dpdt}")