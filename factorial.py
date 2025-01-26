def factorial(n):
    """Рекурсивная функция для вычисления факториала числа."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_from_string(s):
    """Вызывает factorial(), преобразуя строку в число."""
    try:
        number = int(s)  # Преобразуем строку в число
        if number < 0:
            raise ValueError("Факториал определён только для неотрицательных чисел.")
        return factorial(number)
    except ValueError as e:
        return f"Ошибка: {e}"
