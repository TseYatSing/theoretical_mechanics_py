import matplotlib
matplotlib.use('TkAgg')  # 或者使用其他适合的后端，如 'Agg', 'Qt5Agg', 'WXAgg'

from src._4_动力学._2_拉格朗日方程 import LagrangianSystem
from src._4_动力学._4_数值方法._1_微分方程求解器 import ODESolver
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos

# 定义系统参数
m1, m2 = 1.0, 1.0  # 质量
l1, l2 = 1.0, 1.0  # 摆长
g = 9.81

# 构建拉格朗日量
sys = LagrangianSystem(dof=2)
q1, q2 = sys.q
q1d, q2d = sys.qdot

# 动能项
T1 = 0.5 * m1 * (l1**2) * q1d**2
T2 = 0.5 * m2 * ((l1**2)*q1d**2 + (l2**2)*q2d**2 + 2*l1*l2*q1d*q2d*cos(q1-q2))
T = T1 + T2

# 势能项
V = -(m1 + m2)*g*l1*cos(q1) - m2*g*l2*cos(q2)

sys.set_lagrangian(T, V)
sys.derive_equations()  # 推导欧拉-拉格朗日方程
eqns = sys.to_ode_system()

# 转换为数值可解形式
def double_pendulum_ode(t, state):
    theta1, omega1, theta2, omega2 = state
    dtheta1 = omega1
    dtheta2 = omega2
    delta = theta2 - theta1
    den1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta) * np.cos(delta)
    den2 = (l2 / l1) * den1
    domega1 = ((m2 * l1 * omega1 * omega1 * np.sin(delta) * np.cos(delta) +
                m2 * g * np.sin(theta2) * np.cos(delta) +
                m2 * l2 * omega2 * omega2 * np.sin(delta) -
                (m1 + m2) * g * np.sin(theta1)) / den1)
    domega2 = ((-m2 * l2 * omega2 * omega2 * np.sin(delta) * np.cos(delta) +
                (m1 + m2) * g * np.sin(theta1) * np.cos(delta) -
                (m1 + m2) * l1 * omega1 * omega1 * np.sin(delta) -
                (m1 + m2) * g * np.sin(theta2)) / den2)
    return np.array([dtheta1, domega1, dtheta2, domega2])  # 确保返回的是 numpy 数组

# 初始条件
y0 = np.array([np.pi / 2, 0, np.pi, 0])  # 确保初始条件是 numpy 数组

# 数值求解
t, y = ODESolver.rk4(double_pendulum_ode, y0, [0, 10], 0.01)

# 可视化
plt.figure(figsize=(10, 6))
plt.plot(t, y[:, 0], label='Pendulum 1')
plt.plot(t, y[:, 2], label='Pendulum 2')
plt.title("Double Pendulum Simulation")
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.legend()
plt.grid()
plt.show()