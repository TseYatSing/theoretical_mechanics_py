# 在 vector_visualization.py 最前面添加：
import matplotlib
matplotlib.use('TkAgg')  # 强制使用Tkinter后端

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# ... 其他代码保持不变 ...
from src.src_1_core_核心基础模块.core_1_vectors_矢量运算工具 import Vector3D


def plot_3d_vector():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    origin = [0, 0, 0]
    v = Vector3D(1, 2, 3)

    ax.quiver(*origin, *v.components, color='r')
    ax.set_xlim([0, 4])
    ax.set_ylim([0, 4])
    ax.set_zlim([0, 4])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('3D Vector Visualization')
    plt.show()


if __name__ == "__main__":
    plot_3d_vector()