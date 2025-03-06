import matplotlib
matplotlib.use('TkAgg')  # 新增后端设置
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot_rigid_body(vertices, edges, rotation_matrix=None, ax=None):
    """
    绘制刚体三维姿态
    :param vertices: 顶点坐标数组(N,3)
    :param edges: 边连接关系列表[(i,j), ...]
    :param rotation_matrix: 旋转矩阵(3,3)
    :param ax: Matplotlib 3D坐标轴对象
    """
    if ax is None:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

    # 应用旋转
    if rotation_matrix is not None:
        rotated_verts = vertices @ rotation_matrix.T
    else:
        rotated_verts = vertices

    # 绘制边
    for (i, j) in edges:
        ax.plot3D(*zip(rotated_verts[i], rotated_verts[j]), color='blue')

    # 绘制顶点
    ax.scatter3D(*rotated_verts.T, s=50, c='red', depthshade=True)

    # 设置坐标轴
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    return ax


# 使用示例
if __name__ == "__main__":
    # 定义立方体顶点和边
    cube_vertices = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                              [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]])
    cube_edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                  (4, 5), (5, 6), (6, 7), (7, 4),
                  (0, 4), (1, 5), (2, 6), (3, 7)]

    # 绕Z轴旋转45度
    theta = np.pi / 4
    rot_mat = np.array([[np.cos(theta), -np.sin(theta), 0],
                        [np.sin(theta), np.cos(theta), 0],
                        [0, 0, 1]])

    plot_rigid_body(cube_vertices, cube_edges, rot_mat)
    plt.show()