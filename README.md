# theoretical_mechanics_py

## 项目简介
`theoretical_mechanics_py` 是一个用于理论力学教学和研究的 Python 项目，包含了静力学、动力学、运动学等多个模块，提供了矢量运算、坐标系转换、数值积分等功能。

## 目录结构
```
. 
├── main.py 
├── README.md 
├── .idea/ 
├── .pytest_cache/ 
├── examples/ 
│ ├── double_pendulum_chaos.py 
│ ├── rotating_frame_demo.py 
│ ├── simple_demo.py 
│ ├── vector_visualization.py 
│ └── pendulum/ 
├── src/ 
│ ├── advanced/ 
│ ├── core/ 
│ ├── dynamics动力学/ 
│ ├── kinematics运动学/ 
│ ├── statics静力学/ 
│ └── visualization/ 
└── tests/
```
## 安装与运行
1. 克隆仓库：
    ```sh
    git clone https://github.com/TseYatSing/theoretical_mechanics_py.git
    cd theoretical_mechanics_py
    ```

2. 安装依赖：
    ```sh
    pip install -r requirements.txt
    ```

3. 运行示例：
    ```sh
    python examples/simple_demo.py
    ```

## 示例
### 矢量运算
在 `examples/simple_demo.py` 中展示了矢量运算的基本用法：

```python
from src.core核心基础模块.vectors import Vector3D

v1 = Vector3D(3, 4, 0)
print(f"矢量v1: {v1}")
print(f"模长: {v1.magnitude():.2f}")
```

### 坐标系转换
在 examples/simple_demo.py 中展示了坐标系转换的基本用法：

```
from src.core.coordinate_systems import CoordinateTransform

cartesian = (1, 1, 1)
spherical = CoordinateTransform.cartesian_to_spherical(*cartesian)
print(f"笛卡尔坐标 {cartesian} -> 球坐标: {spherical}")
```

## 贡献
欢迎贡献代码！请提交 Pull Request 或报告 Issue。

## 许可证
本项目采用 MIT 许可证，详情请参阅 LICENSE 文件。