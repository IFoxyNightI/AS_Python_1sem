if __name__ == "__main__":
    pass
def TrianglePS(a) :
    P = 3 * a
    S = (3 / 4 * a ** 2)
    return P, S
a = float(input("Введите сторону треугольника: "))
perimeter, area = TrianglePS(a)
print(f"Периметр: {perimeter}")
print(f"Площадь: {area}")
