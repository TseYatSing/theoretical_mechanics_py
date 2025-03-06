import matplotlib
matplotlib.use('TkAgg')  # 更改 matplotlib 后端

import matplotlib.pyplot as plt
import numpy as np

class ForceSystemVisualizer:
    def __init__(self, scale=1.0):
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.set_aspect('equal')
        self.scale = scale  # 力的缩放系数

    def add_force(self, point, vector, label=None, color='red'):
        """添加单个力矢量"""
        x, y = point
        dx, dy = vector[0]*self.scale, vector[1]*self.scale
        self.ax.quiver(x, y, dx, dy,
                      angles='xy', scale_units='xy', scale=1,
                      color=color, label=label)

    def add_moment(self, center, value, radius=0.3, color='blue'):
        """添加力矩图示"""
        if value > 0:  # 逆时针
            arc = self._draw_arc(center, radius, 0, 180, color)
        else:          # 顺时针
            arc = self._draw_arc(center, radius, 180, 360, color)
        self.ax.text(center[0]+radius*1.2, center[1],
                    f'M={abs(value):.1f}N·m', ha='left')

    def _draw_arc(self, center, r, start, end, color):
        """绘制圆弧"""
        theta = np.linspace(np.radians(start), np.radians(end), 50)
        x = center[0] + r * np.cos(theta)
        y = center[1] + r * np.sin(theta)
        return self.ax.plot(x, y, color=color, lw=2)

    def show(self):
        """显示图形"""
        self.ax.legend()
        plt.grid(True)
        plt.show()

# 使用示例
if __name__ == "__main__":
    vis = ForceSystemVisualizer(scale=0.5)
    vis.add_force((0,0), (3,4), label='F1')
    vis.add_force((2,1), (-1,2), color='green', label='F2')
    vis.add_moment((1.5, 1.5), 5.6)
    vis.show()