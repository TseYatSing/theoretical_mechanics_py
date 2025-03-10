# File: examples/_1_简单的示例.py
from src._1_核心基础模块._1_矢量运算工具 import Vector3D
from src._1_核心基础模块._2_坐标系转换 import CoordinateTransform


def main():
    # 矢量运算演示
    v1 = Vector3D(3, 4, 0)
    print(f"矢量v1: {v1}")
    print(f"模长: {v1.magnitude():.2f}")

    # 坐标系转换演示
    cartesian = (1, 1, 1)
    spherical = CoordinateTransform.cartesian_to_spherical(*cartesian)
    print(f"\n笛卡尔坐标 {cartesian} -> 球坐标:")
    print(f"r: {spherical[0]:.2f}, θ: {spherical[1]:.2f} rad, φ: {spherical[2]:.2f} rad")


if __name__ == "__main__":
    main()