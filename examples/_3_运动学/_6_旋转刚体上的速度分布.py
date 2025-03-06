import matplotlib
matplotlib.use('TkAgg')  # 设置 matplotlib 后端

from src._3_运动学._2_刚体运动 import RigidBody2D
import matplotlib.pyplot as plt
import numpy as np

# 设置字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建旋转圆盘模型 (角速度3rad/s)
disk = RigidBody2D(com=[0, 0], theta=0)
disk.angular_vel = 3.0

# 在圆盘上取多个点分析
angles = np.linspace(0, 2 * np.pi, 8)
points = [[np.cos(theta), np.sin(theta)] for theta in angles]  # 半径1m

# 计算各点绝对速度
velocities = []
for p in points:
    v = disk.point_velocity(p)
    velocities.append(v)

# 可视化速度分布
plt.figure(figsize=(8, 8))
for (x, y), (vx, vy) in zip(points, velocities):
    plt.quiver(x, y, vx, vy, color='r', scale=50, width=0.005)
    plt.plot(x, y, 'bo')

circle = plt.Circle((0, 0), 1.0, fill=False, linestyle='--')
plt.gca().add_patch(circle)
plt.title("旋转刚体速度分布 (红色箭头为速度矢量)")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.axis('equal')
plt.grid(True)
plt.show()