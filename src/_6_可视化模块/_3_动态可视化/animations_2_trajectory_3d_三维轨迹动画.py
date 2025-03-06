import numpy as np
import plotly.graph_objects as go

def animate_pendulum(states, l1=1, l2=1):
    """
    生成双摆系统的三维动画
    :param states: 状态数组，形状为 (n_steps, 4)
    :param l1: 第一摆长
    :param l2: 第二摆长
    :return: plotly.graph_objects.Figure 对象
    """
    theta1 = states[:, 0]
    theta2 = states[:, 2]

    # 计算轨迹坐标
    x1 = l1 * np.sin(theta1)
    y1 = -l1 * np.cos(theta1)
    x2 = x1 + l2 * np.sin(theta2)
    y2 = y1 - l2 * np.cos(theta2)
    z = np.zeros_like(x1)

    # 创建图形对象
    fig = go.Figure(
        data=[go.Scatter3d(x=[0, x1[0], x2[0]],
                           y=[0, y1[0], y2[0]],
                           z=[0, 0, 0],
                           mode='lines+markers',
                           line=dict(width=6, color='blue'),
                           marker=dict(size=12, color=['green', 'red', 'red']))]
    )

    # 设置动画帧
    frames = [go.Frame(
        data=[go.Scatter3d(
            x=[0, x1[i], x2[i]],
            y=[0, y1[i], y2[i]],
            z=[0, 0, 0]
        )]
    ) for i in range(len(theta1))]

    # 设置动画参数
    fig.frames = frames
    fig.update_layout(
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, {"frame": {"duration": 50}}])]
        )]
    )

    # 设置场景参数
    fig.update_layout(scene=dict(
        xaxis=dict(range=[-2.5, 2.5]),
        yaxis=dict(range=[-2.5, 2.5]),
        zaxis=dict(range=[-1, 1]),
        aspectmode='cube'
    ))
    return fig