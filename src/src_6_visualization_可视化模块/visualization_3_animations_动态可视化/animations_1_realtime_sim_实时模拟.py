import matplotlib

matplotlib.use('TkAgg')  # 设置Matplotlib后端
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


# 新增：定义缺失的SpringMassSystem类
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


class RealTimeSim:
    def __init__(self, system, init_state, t_span, dt):
        self.system = system
        self.state = np.array(init_state)
        self.dt = dt
        self.time = t_span[0]
        self.t_end = t_span[1]

        # 初始化图形界面
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-1, 1)
        self.ax.set_aspect('equal')
        self.ax.grid(True)

        # 初始化图形元素
        self.line, = self.ax.plot([], [], 'o-', lw=2, markersize=10)
        self.text = self.ax.text(0.05, 0.9, '', transform=self.ax.transAxes)

    def init_animation(self):
        """动画初始化"""
        self.line.set_data([], [])
        return self.line, self.text

    def update_frame(self, frame):
        """更新动画帧"""
        # 更新物理系统状态
        self.system.x = self.state[0]
        self.system.v = self.state[1]
        self.system.step(self.dt)
        self.state = np.array([self.system.x, self.system.v])

        # 更新图形数据
        x_data = [0, self.system.x]
        y_data = [0, 0]
        self.line.set_data(x_data, y_data)

        # 更新文本信息
        self.text.set_text(f'Time: {self.time:.2f}s\n'
                           f'Energy: {self.system.energy():.2f}J')
        self.time += self.dt

        return self.line, self.text

    def run(self):
        """运行动画"""
        ani = FuncAnimation(self.fig, self.update_frame,
                            frames=int((self.t_end - self.time) / self.dt),
                            init_func=self.init_animation,
                            blit=True, interval=1000 * self.dt)
        plt.show()


if __name__ == "__main__":
    # 正确初始化系统
    system = SpringMassSystem()  # 现在这个类已定义
    animator = RealTimeSim(
        system=system,
        init_state=[system.x, system.v],  # 初始状态 [位置, 速度]
        t_span=[0, 10],  # 模拟时长10秒
        dt=0.01  # 时间步长
    )
    animator.run()