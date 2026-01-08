import matplotlib.pyplot as plt
import numpy as np

# Ejemplo de función (puedes cambiarla)
def f(x):
    return np.sin(x) + 0.5*x - 1

x = np.linspace(0, 4, 400)
y = f(x)

x_points = [1.0, 2.0, 2.5]  # x0, x1, x2
y_points = [f(x) for x in x_points]

try:
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label='f(x)', color='blue')
    plt.scatter(x_points, y_points, color='red', zorder=5)

    # Dibujar secantes
    for i in range(len(x_points)-1):
        plt.plot([x_points[i], x_points[i+1]], [y_points[i], y_points[i+1]], 
                 'r--', label=f'Secante {i+1}' if i==0 else "")

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Método de la Secante - Aproximación iterativa')
    plt.legend()
    # plt.show() # Skip show in headless
    print("Execution successful")
except Exception as e:
    print(f"Error: {e}")
