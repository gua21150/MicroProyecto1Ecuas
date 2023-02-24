import numpy as np


def metodo_euler(x0, y0, h, xf, f):
    x_array = np.arange(x0, xf + h, h)  # valores de x que seran iterados
    y_array = np.zeros(len(x_array))  # arreglo donde se almacenan los valores de x
    y_array[0] = y0

    for i in range(0, len(x_array) - 1):
        y_array[i + 1] = y_array[i] + h * f(x_array[i], y_array[i])

    print(" x  ", " y ")

    for k in range(len(x_array)):
        print(round(x_array[k], 4), round(y_array[k], 4))


def metodo_euler_mejorado(x0, y0, h, xf, f):
    x_values = np.arange(x0, xf + h, h)  # valores de x que seran iterados
    y_values = np.zeros(len(x_values))  # arreglo donde se almacenan los valores de aproximacion
    y_values[0] = y0

    for i in range(0, len(x_values) - 1):
        y_temp = y_values[i] + h * f(x_values[i], y_values[i])
        y_values[i + 1] = y_values[i] + h / 2 * (f(x_values[i], y_values[i]) + f(x_values[i + 1], y_temp))

    print(" x  ", " y ")
    for k in range(len(x_values)):
        print(round(x_values[k], 4), round(y_values[k], 4))

def valor_real(x0,xf,h, f):
    x_values = np.arange(x0, xf + h, h)  # valores de x que seran iterados
    for i in range(len(x_values)):
        print(round(x_values[i], 4), round(f(x_values[i]), 4))

if __name__ == '__main__':

    # ejercicio a h=0.1
    print("Ejercicio 1.a.a")
    metodo_euler(x0=1, y0=5, h=0.1, xf=1.2, f=lambda x, y: 2 * x - 3 * y + 1)
    print("Ejercicio 1.a.a mejorado")
    metodo_euler_mejorado(1, 5, 0.1, 1.2, lambda x, y: 2 * x - 3 * y + 1)

    # ejercicio a h=0.05
    print("Ejercicio 1.a.b")
    metodo_euler(1, 5, 0.05, 1.2, lambda x, y: 2 * x - 3 * y + 1)
    print("Ejercicio 1.a.b")
    metodo_euler_mejorado(1, 5, 0.05, 1.2, lambda x, y: 2 * x - 3 * y + 1)

    # ejercicio b h=0.1
    print("Ejercicio 2.b.a.")
    metodo_euler(0, 0, 0.1, 0.2, lambda x, y: x + y ** 2)
    print("Ejercicio 2.b.a.")
    metodo_euler_mejorado(0, 0, 0.1, 0.2, lambda x, y: x + y ** 2)

    # ejercicio b h=0.05
    print("Ejercicio 2.b.b.")
    metodo_euler(0, 0   , 0.05, 0.2, lambda x, y: x + y ** 2)
    print("Ejercicio 2.b.b.")
    metodo_euler_mejorado(0, 0, 0.05, 0.2, lambda x, y: x + y ** 2)

    # ejercicio c h=0.1
    print("Ejercicio 3.c.a")
    metodo_euler(0, 1, 0.1, 1.0, lambda x, y: 2 * x * y)
    print("Ejercicio 3.c.a")
    metodo_euler_mejorado(0, 1, 0.1, 1.0, lambda x, y: 2 * x * y)

    # ejercicio c h=0.05
    print("Ejercicio 3.c.b")
    metodo_euler(0, 1, 0.05, 1.0, lambda x, y: 2 * x * y)
    print("Ejercicio 3.c.b")
    metodo_euler_mejorado(0, 1, 0.05, 1.0, lambda x, y: 2 * x * y)

    # ejercicio d h=0.1
    print("Ejercicio 4.d.a")
    metodo_euler(1, 1, 0.1, 1.5, lambda x, y: x * y ** 2 - y / x)
    print("Ejercicio 4.d.a")
    metodo_euler_mejorado(1, 1, 0.1, 1.5, lambda x, y: x * y ** 2 - y / x)

    # ejercicio d h=0.05
    print("Ejercicio 4.d.b")
    metodo_euler(1, 1, 0.05, 1.5, lambda x, y: x * y ** 2 - y / x)
    print("Ejercicio 4.d.b")
    metodo_euler_mejorado(1, 1, 0.05, 1.5, lambda x, y: x * y ** 2 - y / x)

    # ejercicio e h=0.1
    print("Ejercicio 5.e.a.")
    metodo_euler(0, 0.5, 0.1, 0.5, lambda x, y: y - y ** 2)
    print("Ejercicio 5.e.a.")
    metodo_euler_mejorado(0, 0.5, 0.1, 0.5, lambda x, y: y - y ** 2)

    # ejercicio e h=0.05
    print("Ejercicio 5.e.b")
    metodo_euler(0, 0.5, 0.05, 0.5, lambda x, y: y - y ** 2)
    print("Ejercicio 5.e.b")
    metodo_euler_mejorado(0, 0.5, 0.05, 0.5, lambda x, y: y - y ** 2)
