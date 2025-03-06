# examples/statics/equilibrium_demo.py
import numpy as np
from src._2_静力学._1_力系分析 import Force, ForceSystem

# 创建二维力系
system = ForceSystem(dimension=2)

# 添加力 (单位：牛顿)
system.add_force(Force([30, 40], [0, 0]))    # 作用在原点
system.add_force(Force([-20, -30], [3, 4]))
system.add_force(Force([10, -5], [2, 1]))

# 计算主矢和主矩
resultant_force = system.resultant_force
resultant_moment = system.resultant_moment(np.zeros(2))

print(f"主矢: {resultant_force} N")
print(f"对原点主矩: {resultant_moment[2]} N·m")  # 二维取Mz

# 判断平衡
equilibrium = np.allclose(resultant_force, 0) and np.isclose(resultant_moment[2], 0)
print(f"系统是否平衡: {equilibrium}")

# 可视化力系
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
for f in system.forces:
    plt.quiver(f.point[0], f.point[1], f.vector[0], f.vector[1],
               angles='xy', scale_units='xy', scale=1, color=['r','g','b'])
plt.grid()
plt.axis('equal')
plt.title("Force System Visualization")
plt.xlabel("X (m)")
plt.ylabel("Y (m)")
plt.show()