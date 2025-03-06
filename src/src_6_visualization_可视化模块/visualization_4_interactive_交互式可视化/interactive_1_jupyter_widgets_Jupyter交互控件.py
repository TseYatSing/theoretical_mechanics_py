from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
import numpy as np


def interactive_pendulum():
    """交互式单摆参数探索"""
    fig, ax = plt.subplots(figsize=(8, 6))
    line, = ax.plot([], [], 'o-', lw=2)
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 0.5)
    ax.set_aspect('equal')

    @interact(
        length=FloatSlider(1.0, 0.5, 2.0, 0.1),
        theta0=FloatSlider(np.pi / 4, 0, np.pi / 2, 0.1),
        gravity=FloatSlider(9.8, 1.0, 20.0, 0.5)
    )
    def update(length=1.0, theta0=np.pi / 4, gravity=9.8):
        x = length * np.sin(theta0)
        y = -length * np.cos(theta0)
        line.set_data([0, x], [0, y])
        fig.canvas.draw_idle()


# 在Jupyter中运行
interactive_pendulum()