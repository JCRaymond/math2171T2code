from math import sqrt


def euler(dx, dy, x_0, y_0, h, steps):
    x = x_0
    y = y_0
    print(x, y)
    for _ in range(steps):
        x_new = x + h * dx(x, y)
        y_new = y + h * dy(x, y)
        x, y = x_new, y_new
        print(x, y)
    return x, y


def improved_euler(dx, dy, x_0, y_0, h, steps):
    x = x_0
    y = y_0
    print(x, y)
    for _ in range(steps):
        x_e = x + h * dx(x, y)
        y_e = y + h * dy(x, y)
        x_new = x + h / 2 * (dx(x, y) + dx(x_e, y_e))
        y_new = y + h / 2 * (dy(x, y) + dy(x_e, y_e))
        x, y = x_new, y_new
        print(x, y)
    return x, y


def f(x, y):
    return -x + (y + x) / sqrt(y * y + x * x)


def g(x, y):
    return -y + (y - x) / sqrt(y * y + x * x)


if __name__ == '__main__':
    print("Euler's Method")
    euler(f, g, 1, 2, 1, 5)

    print()
    print("Improved Euler's Method")
    improved_euler(f, g, 1, 2, 1, 5)
