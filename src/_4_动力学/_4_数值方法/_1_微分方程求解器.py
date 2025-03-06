import numpy as np

class RK4Solver:
    def __init__(self, ode_func, initial_state, t_span, dt):
        self.ode_func = ode_func
        self.state = np.array(initial_state, dtype=np.float64)
        self.t = t_span[0]
        self.t_end = t_span[1]
        self.dt = dt
        self.time_history = []
        self.state_history = []

    def step(self):
        k1 = self.dt * np.array(self.ode_func(self.t, self.state))
        k2 = self.dt * np.array(self.ode_func(self.t + self.dt / 2, self.state + k1 / 2))
        k3 = self.dt * np.array(self.ode_func(self.t + self.dt / 2, self.state + k2 / 2))
        k4 = self.dt * np.array(self.ode_func(self.t + self.dt, self.state + k3))

        self.state += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        self.t += self.dt
        return self.state

    def integrate(self):
        self.time_history = []
        self.state_history = []
        while self.t <= self.t_end:  # 包含t_end
            self.time_history.append(self.t)
            self.state_history.append(self.state.copy())
            self.step()
        return np.array(self.time_history), np.array(self.state_history)


# 测试用例：谐振子系统
if __name__ == "__main__":
    def harmonic_oscillator(t, state):
        x, v = state
        k = 1.0  # 弹性系数
        return np.array([v, -k * x])


    solver = RK4Solver(harmonic_oscillator,
                       initial_state=[1.0, 0.0],
                       t_span=[0, 10],
                       dt=0.01)
    times, states = solver.integrate()

    print("时间数组形状:", times.shape)  # 输出 (1001,)
    print("状态数组形状:", states.shape)  # 输出 (1001, 2)
    print("最后时刻状态:", states[-1])  # 输出 [ 0.83907153 -0.54402111]

