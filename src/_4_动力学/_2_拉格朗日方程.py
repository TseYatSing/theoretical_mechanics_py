"""
拉格朗日力学框架
支持自动推导运动方程
"""
from sympy import symbols, Function, diff, Matrix
from sympy.physics.mechanics import LagrangesMethod, Lagrangian
from sympy.physics.vector import ReferenceFrame

class LagrangianSystem:
    def __init__(self, dof: int):
        """
        :param dof: 系统自由度数量
        """
        self.N = dof
        self.t = symbols('t')
        self.q = [Function(f'q{i}')(self.t) for i in range(self.N)]
        self.qdot = [diff(q, self.t) for q in self.q]

        self.L = None  # 拉格朗日量表达式
        self.equations = None  # 运动方程

    def set_lagrangian(self, T, V):
        """设置系统动能和势能"""
        self.L = T - V

    def derive_equations(self, simplify=True) -> Matrix:
        """推导欧拉-拉格朗日方程"""
        if self.L is None:
            raise ValueError("未定义拉格朗日量")

        lm = LagrangesMethod(self.L, self.q)
        lm.form_lagranges_equations()

        self.equations = lm.eom
        if simplify:
            self.equations = [eq.simplify() for eq in self.equations]
        return Matrix(self.equations)

    def to_ode_system(self):
        """将二阶方程转换为一阶ODE系统"""
        substitutions = {diff(q, self.t): qd for q, qd in zip(self.q, self.qdot)}
        return [eq.subs(substitutions) for eq in self.equations]

# 示例：单摆系统
def pendulum_example():
    # 定义符号
    t, m, l, g = symbols('t m l g')
    theta = Function('theta')(t)
    theta_dot = diff(theta, t)

    # 动能和势能
    T = 0.5 * m * (l**2) * theta_dot**2
    V = -m * g * l * theta.cos()  # 以最低点为参考

    # 生成方程
    sys = LagrangianSystem(dof=1)
    sys.set_lagrangian(T, V)
    equations = sys.derive_equations()
    print("单摆运动方程:", equations)