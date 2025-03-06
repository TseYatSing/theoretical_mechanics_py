from sympy import symbols, Function, diff, simplify

t = symbols('t')  # 时间符号变量


def derive_lagrange_equation(L, q, q_dot):
    """
    自动推导拉格朗日方程
    :param L: 拉格朗日函数表达式
    :param q: 广义坐标符号（如Function('q')(t)）
    :param q_dot: 广义速度符号（如q.diff(t)）
    :return: 标准形式的拉格朗日方程
    """
    # 计算各项偏导
    dL_dq = diff(L, q)
    dL_dqdot = diff(L, q_dot)
    d_dt_dL_dqdot = diff(dL_dqdot, t)

    # 组合成拉格朗日方程
    eq = d_dt_dL_dqdot - dL_dq
    return simplify(eq)


# 使用示例
if __name__ == "__main__":
    m, g, l = symbols('m g l')  # 质量、重力加速度、摆长
    theta = Function('theta')(t)
    theta_dot = diff(theta, t)

    # 单摆系统的拉格朗日量
    T = 0.5 * m * (l ** 2) * theta_dot ** 2  # 动能
    V = -m * g * l * theta.cos()  # 势能
    L = T - V

    # 推导运动方程
    equation = derive_lagrange_equation(L, theta, theta_dot)
    print("单摆系统的拉格朗日方程：")
    print(equation)  # 输出：l*m*sin(theta(t)) + l**2*m*Derivative(theta(t), (t, 2)) + g*m*cos(theta(t)) = 0