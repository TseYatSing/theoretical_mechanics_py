"""
刚体运动学分析
支持平面运动和三维空间运动
包含基点法、瞬时转动中心计算
"""
import numpy as np
from scipy.spatial.transform import Rotation

class RigidBody2D:
    def __init__(self, com: np.ndarray, theta: float = 0.0):
        """
        :param com: 质心坐标 [x, y]
        :param theta: 初始转角 (弧度)
        """
        self.com = np.array(com)
        self.theta = theta
        self.angular_vel = 0.0
        self.com_vel = np.zeros(2)  # 添加质心速度属性

    def update_motion(self, com_vel: np.ndarray, angular_acc: float, dt: float):
        """
        更新刚体状态（欧拉积分法）
        :param com_vel: 质心速度 [vx, vy]
        :param angular_acc: 角加速度 (rad/s²)
        :param dt: 时间步长
        """
        self.com += com_vel * dt
        self.angular_vel += angular_acc * dt
        self.theta += self.angular_vel * dt

    def point_velocity(self, point: np.ndarray) -> np.ndarray:
        """
        计算刚体上任意点的速度（基点法）
        :param point: 点相对于质心的位置 [dx, dy]
        :return: 绝对速度 [vx, vy]
        """
        r = np.array(point)
        omega = self.angular_vel
        return self.com_vel + np.array([-omega * r[1], omega * r[0]])

    @property
    def rotation_matrix(self) -> np.ndarray:
        """二维旋转矩阵"""
        return np.array([
            [np.cos(self.theta), -np.sin(self.theta)],
            [np.sin(self.theta), np.cos(self.theta)]
        ])

class RigidBody3D:
    def __init__(self, com: np.ndarray, orientation: np.ndarray = None):
        """
        :param com: 质心坐标 [x, y, z]
        :param orientation: 姿态四元数 [w, x, y, z]
        """
        self.com = np.array(com)
        self.orientation = orientation if orientation else Rotation.identity()
        self.angular_vel = np.zeros(3)

    def rotate_axis_angle(self, axis: np.ndarray, angle: float):
        """绕指定轴旋转"""
        self.orientation *= Rotation.from_rotvec(angle * axis)

    def point_velocity(self, point_local: np.ndarray) -> np.ndarray:
        """
        计算刚体上点的绝对速度
        :param point_local: 点在局部坐标系中的坐标
        :return: 绝对速度 [vx, vy, vz]
        """
        # 全局坐标系中的位置矢量
        r_global = self.orientation.apply(point_local)
        return self.com_vel + np.cross(self.angular_vel, r_global)

    @property
    def euler_angles(self) -> tuple:
        """转换为欧拉角 (ZYX顺序)"""
        return self.orientation.as_euler('zyx')

# 示例：定轴转动刚体上的点速度分析
def rotating_disk_demo():
    body = RigidBody2D(com=[0, 0], theta=0)
    body.angular_vel = 2.0  # 2 rad/s

    # 计算边缘点速度 (半径1m)
    point_rel = [1, 0]
    v = body.point_velocity(point_rel)
    print(f"点绝对速度: {v} m/s")