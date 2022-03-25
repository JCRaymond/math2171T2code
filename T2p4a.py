from math import sin, cos


def ord3_taylor(f1, f2, f3, x0, y0, h, N):
    x = x0
    y = y0
    print(x, y)
    for _ in range(N):
        dydx = f1(x, y)
        d2ydx2 = f2(x, y)
        d3ydx3 = f3(x, y)
        x += h
        y += h * dydx + h * h / 2 * d2ydx2 + h * h * h / 6 * d3ydx3
        print(x, y)
    return x, y


def runge_kutta(f, x0, y0, h, N):
    x = x0
    y = y0
    print(x, y)
    for _ in range(N):
        K1 = f(x, y)
        K2 = f(x + h / 2, y + h / 2 * K1)
        K3 = f(x + h / 2, y + h / 2 * K2)
        K4 = f(x + h, y + h * K3)
        K = (K1 + 2 * K2 + 2 * K3 + K4) / 6
        x += h
        y += h * K
        print(x, y)
    return x, y


def f1(x, y):
    return sin(x) * y * y - pow(x * y, 1 / 3)


def f2(x, y):
    dydx = f1(x, y)
    return -(x * dydx + y) / (
        3 * pow(x * y, 2 / 3)) + 2 * y * sin(x) * dydx + y * y * cos(x)


def f3(x, y):
    dydx = f1(x, y)
    d2ydx2 = f2(x, y)
    return 2 * pow((x * dydx + y), 2) / (9 * x * y * pow(x * y, 2 / 3)) \
        - (x * d2ydx2 + 2 * dydx) / (3 * pow(x * y, 2 / 3))             \
        + 4 * y * cos(x) * dydx                                         \
        + sin(x) * (2 * y * d2ydx2 + 2 * pow(dydx, 2) - y * y)


if __name__ == '__main__':
    print("Third Order Taylor's Method")
    ord3_taylor(f1, f2, f3, 1, 1, 0.2, 5)

    print()
    print("Runge-Kutta Method")
    runge_kutta(f1, 1, 1, 0.2, 5)
