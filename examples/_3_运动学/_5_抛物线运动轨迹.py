import matplotlib
matplotlib.use('TkAgg')  # 设置 matplotlib 后端

from src._3_运动学._1_质点运动 import Particle
import numpy as np
import matplotlib.pyplot as plt

# 设置字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 初始条件：初速50m/s，仰角60度
v0 = 50
theta = np.deg2rad(60)
initial_velocity = [v0*np.cos(theta), v0*np.sin(theta), 0]

# 创建质点对象
projectile = Particle(
    position=[0, 0, 0],
    velocity=initial_velocity
)

# 定义加速度函数（考虑空气阻力）
def acceleration(r, v, t):
    g = 9.81
    k = 0.1  # 空气阻力系数
    a_x = -k * v[0]
    a_y = -g - k * v[1]
    return np.array([a_x, a_y, 0])

# 计算轨迹（持续到落地）
trajectory = projectile.cartesian_acceleration(acceleration, t_end=10)

# 提取数据
t = trajectory[:,0]
x = trajectory[:,1]
y = trajectory[:,2]

# 可视化
plt.figure(figsize=(10,6))
plt.plot(x, y, label='有空气阻力')
plt.title("抛射体运动轨迹")
plt.xlabel("水平距离 (m)")
plt.ylabel("高度 (m)")
plt.grid(True)

# 对比无阻力情况
analytic_x = v0*np.cos(theta)*t
analytic_y = v0*np.sin(theta)*t - 0.5*9.81*t**2
plt.plot(analytic_x, analytic_y, 'r--', label='无空气阻力')
plt.legend()
plt.show()