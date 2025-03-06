from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
import numpy as np


class InteractivePendulum:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.line, = self.ax.plot([], [], 'o-', lw=2)
        self.ax.set_xlim(-2, 2)
        self.ax.set_ylim(-2, 2)
        self.ax.grid(True)

    def update(self, length=1.0, mass=1.0, theta0=np.pi / 4, gravity=9.8):
        x = length * np.sin(theta0)
        y = -length * np.cos(theta0)
        self.line.set_data([0, x], [0, y])
        self.ax.set_title(f'Pendulum Simulation\nLength={length}m, Mass={mass}kg')
        self.fig.canvas.draw()


# 在Jupyter中运行
if __name__ == "__main__":
    pendulum = InteractivePendulum()
    interact(
        pendulum.update,
        length=FloatSlider(value=1.0, min=0.5, max=2.0, step=0.1),
        mass=FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1),
        theta0=FloatSlider(value=np.pi / 4, min=-np.pi / 2, max=np.pi / 2, step=0.1),
        gravity=FloatSlider(value=9.8, min=3.0, max=15.0, step=0.5)
    )