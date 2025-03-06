import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# 定义SpringMassSystem类
class SpringMassSystem:
    def __init__(self):
        self.x = 1.0  # 初始位移
        self.v = 0.0  # 初始速度
        self.k = 10.0  # 弹簧劲度系数
        self.m = 1.0  # 质量

    def step(self, dt):
        """执行一步物理模拟"""
        a = -self.k / self.m * self.x  # 加速度计算
        self.v += a * dt  # 更新速度
        self.x += self.v * dt  # 更新位移

    def energy(self):
        """计算系统总能量"""
        return 0.5 * self.m * self.v ** 2 + 0.5 * self.k * self.x ** 2

class EnergyPlot:
    def __init__(self, system, t_span, dt):
        self.system = system
        self.dt = dt
        self.time = t_span[0]
        self.t_end = t_span[1]
        self.times = []
        self.energies = []

        # 初始化图形界面
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlim(t_span[0], t_span[1])
        self.ax.set_ylim(0, 10)
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Energy (J)')
        self.line, = self.ax.plot([], [], lw=2)

    def init_animation(self):
        """动画初始化"""
        self.line.set_data([], [])
        return self.line,

    def update_frame(self, frame):
        """更新动画帧"""
        self.system.step(self.dt)
        self.times.append(self.time)
        self.energies.append(self.system.energy())
        self.line.set_data(self.times, self.energies)
        self.time += self.dt
        return self.line,

    def run(self):
        """运行动画"""
        ani = FuncAnimation(self.fig, self.update_frame,
                            frames=int((self.t_end - self.time) / self.dt),
                            init_func=self.init_animation,
                            blit=True, interval=1000 * self.dt)
        plt.show()

if __name__ == "__main__":
    system = SpringMassSystem()
    energy_plot = EnergyPlot(system, t_span=[0, 10], dt=0.01)
    energy_plot.run()