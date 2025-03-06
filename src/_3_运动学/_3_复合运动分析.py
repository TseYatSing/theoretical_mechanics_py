"""
复合运动分析模块
包含参考系变换、科里奥利加速度计算
支持旋转和平动参考系
"""
import numpy as np
from typing import Optional  # 添加这一行

class MovingFrame:
    def __init__(self,
                 origin: np.ndarray,
                 angular_vel: Optional[np.ndarray] = None):
        """
        :param origin: 参考系原点在全局系中的坐标
        :param angular_vel: 参考系角速度矢量 (三维) [rad/s]
        """
        self.origin = np.array(origin)
        self.angular_vel = angular_vel if angular_vel is not None else np.zeros(3)

    def relative_position(self, absolute_pos: np.ndarray) -> np.ndarray:
        """绝对坐标 -> 相对坐标"""
        return absolute_pos - self.origin

    def absolute_position(self, relative_pos: np.ndarray) -> np.ndarray:
        """相对坐标 -> 绝对坐标"""
        return self.origin + relative_pos

    def transform_velocity(self,
                           abs_velocity: np.ndarray,
                           rel_position: np.ndarray) -> np.ndarray:
        """
        速度转换公式
        :return: 相对速度 v_rel = v_abs - v_frame
        """
        v_frame = np.cross(self.angular_vel, rel_position)
        return abs_velocity - v_frame

    def transform_acceleration(self,
                               abs_accel: np.ndarray,
                               rel_velocity: np.ndarray,
                               rel_position: np.ndarray) -> np.ndarray:
        """
        加速度转换公式（包含科里奥利项）
        :return: 相对加速度 a_rel
        """
        coriolis = 2 * np.cross(self.angular_vel, rel_velocity)
        centrifugal = np.cross(self.angular_vel, np.cross(self.angular_vel, rel_position))
        return abs_accel - (centrifugal + coriolis)


def coriolis_acceleration_demo():
    # 在北纬40度的地面参考系中分析自由落体
    latitude = np.deg2rad(40)
    omega_earth = 7.292e-5  # 地球自转角速度 (rad/s)

    # 建立当地参考系（x-东, y-北, z-天）
    omega_frame = np.array([0, omega_earth * np.sin(latitude), omega_earth * np.cos(latitude)])
    frame = MovingFrame(origin=[0, 0, 0], angular_vel=omega_frame)

    # 物体初始条件（从100m静止下落）
    z0 = 100.0
    v_abs = np.zeros(3)
    r_rel = np.array([0, 0, z0])

    # 计算科里奥利加速度
    a_abs = np.array([0, 0, -9.81])  # 真实加速度
    a_rel = frame.transform_acceleration(a_abs, np.zeros(3), r_rel)

    print(f"东向偏移加速度: {a_rel[0]:.2e} m/s²")
    print(f"北向偏移加速度: {a_rel[1]:.2e} m/s²")