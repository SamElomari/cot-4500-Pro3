def f(t, y):
    return t - y**2

def euler_method(f, t0, y0, t_end, iterations):
    h = (t_end - t0) / iterations
    t, y = t0, y0
    for _ in range(iterations):
        y += h * f(t, y)
        t += h
    return y

def runge_kutta_method(f, t0, y0, t_end, iterations):
    h = (t_end - t0) / iterations
    t, y = t0, y0
    for _ in range(iterations):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5*h, y + 0.5*k1)
        k3 = h * f(t + 0.5*h, y + 0.5*k2)
        k4 = h * f(t + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
    return y
