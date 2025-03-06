import numpy as np


class InertiaTensor:
    def __init__(self, mass, points):
        """
        :param mass: 刚体总质量
        :param points: 各质点坐标列表 [(x1,y1,z1), (x2,y2,z2), ...]
        """
        self.mass = mass
        self.points = np.array(points)
        self.N = len(points)

    def calculate_tensor(self):
        """计算转动惯量张量"""
        I = np.zeros((3, 3))
        for r in self.points:
            r_sq = np.dot(r, r)
            I += np.eye(3) * r_sq - np.outer(r, r)
        return I * (self.mass / self.N)

    def principal_axes(self):
        """计算主轴方向"""
        I = self.calculate_tensor()
        eigvals, eigvecs = np.linalg.eigh(I)
        return eigvals, eigvecs


# 使用示例
if __name__ == "__main__":
    # 定义立方体质点分布
    cube_points = [(x, y, z) for x in [-1, 1] for y in [-1, 1] for z in [-1, 1]]
    cube = InertiaTensor(mass=8.0, points=cube_points)

    print("转动惯量张量：\n", cube.calculate_tensor())
    print("主转动惯量：\n", cube.principal_axes()[0])