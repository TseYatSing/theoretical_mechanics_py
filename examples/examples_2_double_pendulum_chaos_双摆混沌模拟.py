import numpy as np
from src.dynamics动力学.analytical分析力学.lagrangian拉格朗日体系 import derive_lagrange_equation
from src.dynamics动力学.numerical数值方法.ode_solvers import RK4Solver
from src.visualization可视化模块.animations import animate_pendulum

# 系统参数
m1, m2 = 1.0, 1.0  # 质量
l1, l2 = 1.0, 1.0  # 摆长
g = 9.81

# 定义广义坐标
theta1 = Function('theta1')(t)
theta2 = Function('theta2')(t)
theta1_dot = diff(theta1, t)
theta2_dot = diff(theta2, t)

# 计算动能和势能
# 第一摆锤位置
x1 = l1 * theta1.sin()
y1 = -l1 * theta1.cos()

# 第二摆锤位置
x2 = x1 + l2 * theta2.sin()
y2 = y1 - l2 * theta2.cos()

# 动能
v1_sq = (l1 * theta1_dot)**2
v2_sq = (l1**2 * theta1_dot**2 + l2**2 * theta2_dot**2 +
        2*l1*l2*theta1_dot*theta2_dot*(theta1 - theta2).cos())
T = 0.5*m1*v1_sq + 0.5*m2*v2_sq

# 势能
V = m1*g*y1 + m2*g*y2

# 推导运动方程
L = T - V
eq1 = derive_lagrange_equation(L, theta1, theta1_dot)
eq2 = derive_lagrange_equation(L, theta2, theta2_dot)

# 转换为数值可解的ODE函数
def double_pendulum_ode(t, state):
    theta1, omega1, theta2, omega2 = state
    # 此处需将符号方程转换为数值计算表达式
    # 此处省略具体实现（需使用lambdify转换符号表达式）
    dydt = [omega1, calc_omega1, omega2, calc_omega2]
    return np.array(dydt)

# 数值求解与可视化
solver = RK4Solver(double_pendulum_ode, [np.pi/2, 0, np.pi, 0], [0, 10], 0.01)
result = solver.integrate()
animate_pendulum(result)  # 生成动画