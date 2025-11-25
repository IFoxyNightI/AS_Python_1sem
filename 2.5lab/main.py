if __name__ == "__main__":
    pass
def SqrtK(x, k, n):
    if n == 0:
        return 1  # y(0) = 1
    else:
        y_prev = SqrtK(x, k, n - 1)
        return y_prev - (y_prev - x / (y_prev ** (k - 1))) / k
#Пример:
print(SqrtK(16, 4, 10))
