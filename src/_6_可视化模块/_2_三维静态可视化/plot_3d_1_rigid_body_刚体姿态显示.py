import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class RigidBodyVisualizer3D:
    def __init__(self, vertices, edges):
        """
        :param vertices: 顶点坐标数组 (N,3)
        :param edges: 边连接列表 [(i,j), ...]
        """
        self.vertices = np.array(vertices)
        self.edges = edges
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')

    def update_pose(self, rotation_matrix):
        """更新刚体姿态"""
        rotated = self.vertices @ rotation_matrix.T
        self.ax.clear()

        # 绘制边
        for (i, j) in self.edges:
            self.ax.plot3D(*zip(rotated[i], rotated[j]), 'blue')

        # 绘制顶点
        self.ax.scatter3D(*rotated.T, s=50, c='red')

        # 设置坐标轴
        self.ax.set_xlim3d(-2, 2)
        self.ax.set_ylim3d(-2, 2)
        self.ax.set_zlim3d(-2, 2)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

    def show(self):
        plt.show()


# 使用示例
if __name__ == "__main__":
    # 定义立方体
    cube_verts = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
                           [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]])
    cube_edges = [(0, 1), (1, 2), (2, 3), (3, 0),
                  (4, 5), (5, 6), (6, 7), (7, 4),
                  (0, 4), (1, 5), (2, 6), (3, 7)]

    viz = RigidBodyVisualizer3D(cube_verts, cube_edges)

    # 绕Z轴旋转45度
    theta = np.pi / 4
    rot_z = np.array([[np.cos(theta), -np.sin(theta), 0],
                      [np.sin(theta), np.cos(theta), 0],
                      [0, 0, 1]])
    viz.update_pose(rot_z)
    viz.show()