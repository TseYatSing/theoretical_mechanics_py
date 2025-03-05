# tests/test_vectors.py
import pytest
import numpy as np
from src.core.vectors import Vector3D  # 修正后的导入路径


def test_vector_operations():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)

    # 测试加法
    assert (v1 + v2).components.tolist() == [5, 7, 9]

    # 测试点积
    assert abs(v1.dot(v2) - 32) < 1e-9

    # 测试叉积
    cross = v1.cross(v2)
    expected = Vector3D(-3, 6, -3)
    assert np.allclose(cross.components, expected.components)


def test_rotation():
    v = Vector3D(1, 0, 0)
    rotated = v.rotate(Vector3D(0, 0, 1), np.pi / 2)  # 绕z轴旋转90度
    assert np.allclose(rotated.components, [0, 1, 0], atol=1e-9)