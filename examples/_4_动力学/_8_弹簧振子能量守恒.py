# examples/dynamics/newtonian/spring_energy_demo.py
from dynamics.newtonian.energy import EnergyAnalyzer
import numpy as np
import matplotlib.pyplot as plt

# 系统参数
m = 0.5  # 质量 (kg)
k = 20.0  # 劲度系数 (N/m)
x0 = 0.2  # 初始位移 (m)

# 初始化分析器
analyzer = EnergyAnalyzer(masses=[m])
analyzer.positions = np.array([[x0, 0, 0]])  # 初始位置
analyzer.velocities = np.array([[0, 0, 0]])  # 初始静止

# 运动参数（简谐振动解析解）
t = np.linspace(0, 2*np.pi*np.sqrt(m/k), 100)
x = x0 * np.cos(np.sqrt(k/m)*t)
v = -x0 * np.sqrt(k/m) * np.sin(np.sqrt(k/m)*t)

# 计算能量变化
kinetic = []
potential = []
for pos, vel in zip(x, v):
    analyzer.positions[0,0] = pos
    analyzer.velocities[0,0] = vel
    kinetic.append(analyzer.kinetic_energy())
    potential.append(analyzer.spring_potential(k, [0,0,0]))

# 可视化
plt.figure(figsize=(10,6))
plt.plot(t, kinetic, label='动能')
plt.plot(t, potential, label='势能')
plt.plot(t, np.array(kinetic)+np.array(potential), 'k--', label='总机械能')
plt.title("弹簧振子能量变化 (理论解)")
plt.xlabel("时间 (s)")
plt.ylabel("能量 (J)")
plt.legend()
plt.grid()
plt.show()