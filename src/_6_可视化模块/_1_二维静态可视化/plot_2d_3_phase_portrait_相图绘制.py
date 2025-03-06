import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib
matplotlib.use('TkAgg')


class PhasePortrait:
    def __init__(self, system_func, bounds=(-5, 5), density=20):
        """
        :param system_func: 系统微分方程函数 dy/dt = f(y, t)
        """
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.system = system_func
        self.bounds = bounds
        self.density = density

    def generate(self, trajectories=5):
        """生成相图"""
        # 生成网格
        x = np.linspace(*self.bounds, self.density)
        y = np.linspace(*self.bounds, self.density)
        X, Y = np.meshgrid(x, y)

        # 计算方向场
        U, V = np.zeros_like(X), np.zeros_like(Y)
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                U[i, j], V[i, j] = self.system([X[i, j], Y[i, j]], 0)

        # 绘制方向场
        self.ax.streamplot(X, Y, U, V, density=1.5, color='gray')

        # 绘制示例轨迹
        for _ in range(trajectories):
            y0 = np.random.uniform(*self.bounds, 2)
            t = np.linspace(0, 10, 300)
            sol = odeint(self.system, y0, t)
            self.ax.plot(sol[:, 0], sol[:, 1], lw=1.5)

        self.ax.set_xlabel('Position')
        self.ax.set_ylabel('Velocity')
        return self.fig


# 使用示例：阻尼振子
if __name__ == "__main__":
    def damped_oscillator(state, t, b=0.2, k=1.0):
        x, v = state
        return [v, -b * v - k * x]


    pp = PhasePortrait(lambda y, t: damped_oscillator(y, t))
    pp.generate()
    plt.show()