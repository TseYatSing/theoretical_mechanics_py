# theoretical_mechanics_py

## 项目简介
`theoretical_mechanics_py` 是一个用于理论力学教学和研究的 Python 项目，包含了静力学、动力学、运动学等多个模块，提供了矢量运算、坐标系转换、数值积分等功能。

## 目录结构
```
. 
├── main.py 
├── README.md 
├── .idea/ 
├── .pytest_cache/ 
├── examples/ 
│ ├── _1_简单的示例.py
│ ├── _2_双摆混沌模拟.py 
│ ├── _3_旋转参考系演示.py 
│ ├── _4_矢量可视化.py 
│ ├── _5_单摆.py 
│ ├── _6_旋转刚体上的速度分布.py 
│ ├── _7_用拉格朗日方程+龙格库塔法模拟双摆.py 
│ └── pendulum/ 
├── src/ 
│ ├── advanced/ 
│ ├── core/ 
│ ├── dynamics动力学/ 
│ ├── kinematics运动学/ 
│ ├── statics静力学/ 
│ └── visualization/ 
└── tests/
```

## 安装与运行
1. 克隆仓库：
    ```sh
    git clone https://github.com/TseYatSing/theoretical_mechanics_py.git
    cd theoretical_mechanics_py
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

3. 运行示例：
    ```sh
    python examples/_1_简单的示例.py
    ```

## 示例
### 矢量运算
在 `examples/_1_简单的示例.py` 中展示了矢量运算的基本用法：

```python
from src.core.vectors import Vector3D

v1 = Vector3D(3, 4, 0)
print(f"矢量v1: {v1}")
print(f"模长: {v1.magnitude():.2f}")
```

### 坐标系转换
在 `examples/_1_简单的示例.py` 中展示了坐标系转换的基本用法：

```python
from src.core.coordinate_systems import CoordinateTransform

cartesian = (1, 1, 1)
spherical = CoordinateTransform.cartesian_to_spherical(*cartesian)
print(f"笛卡尔坐标 {cartesian} -> 球坐标: {spherical}")
```

### 单摆系统
在 `examples/_5_单摆.py` 中展示了单摆系统的基本用法：

```python
from src._4_动力学._2_拉格朗日方程 import LagrangianSystem
from sympy import symbols, Function, diff

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
```

### 双摆系统
在 `examples/_7_用拉格朗日方程+龙格库塔法模拟双摆.py` 中展示了双摆系统的基本用法：

```python
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
```

## 贡献
欢迎贡献代码！请提交 Pull Request 或报告 Issue。

## 许可证
本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。