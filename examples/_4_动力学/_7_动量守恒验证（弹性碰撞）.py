# examples/dynamics/newtonian/collision_demo.py
import numpy as np
from dynamics.newtonian.momentum import NewtonianSystem, collision_2d
import matplotlib.pyplot as plt

# 初始化系统（两个质量相同的质点）
system = NewtonianSystem(masses=[1.0, 1.0])

# 设置初始速度（二维）
system.velocities = np.array([[2.0, 0.0], [-1.0, 0.0]])

# 计算初始动量
initial_momentum = system.total_momentum()

# 模拟完全弹性碰撞
v1, v2 = collision_2d(1.0, system.velocities[0],
                     1.0, system.velocities[1], e=1.0)
system.velocities = np.array([v1, v2])

# 验证动量守恒
print("碰撞前总动量:", initial_momentum)
print("碰撞后总动量:", system.total_momentum())
print("动量是否守恒:", system.check_conservation(initial_momentum))

# 可视化碰撞过程
plt.figure(figsize=(10,4))
plt.quiver(0, 0, system.velocities[0,0], system.velocities[0,1],
           scale=10, color='r', label='质点1')
plt.quiver(1, 0, system.velocities[1,0], system.velocities[1,1],
           scale=10, color='b', label='质点2')
plt.xlim(-2, 2)
plt.ylim(-1, 1)
plt.title("碰撞前后速度矢量变化")
plt.legend()
plt.grid()
plt.show()