# theoretical_mechanics_py

## 简介
`theoretical_mechanics_py` 是一个用于理论力学计算和可视化的 Python 库。

## 安装

1. 克隆仓库：
    ```sh
    git clone https://github.com/TseYatSing/theoretical_mechanics_py.git
    cd theoretical_mechanics_py
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

## 使用示例

### 坐标转换

```python
from src.core.coordinate_systems import CoordinateTransform

cartesian = (1, 1, 1)
spherical = CoordinateTransform.cartesian_to_spherical(*cartesian)
print(f"{cartesian} -> {spherical}")
```
### 向量操作
```
from src.core.vectors import Vector3D

v1 = Vector3D(3, 4, 0)
print(f"向量 v1: {v1}")
print(f"向量 v1 的模: {v1.magnitude():.2f}")
```
## 目录结构
```
theoretical_mechanics_py/
├── examples/
│   ├── simple_demo.py
│   ├── rotating_frame_demo.py
│   └── double_pendulum_chaos.py
├── src/
│   ├── core/
│   │   ├── coordinate_systems.py
│   │   └── vectors.py
│   ├── dynamics/
│   ├── kinematics/
│   ├── statics/
│   └── visualization/
├── tests/
├── LICENSE
└── README.md
```

## 许可证
本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。
