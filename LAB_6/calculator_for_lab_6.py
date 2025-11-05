class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

    @staticmethod
    def is_prime_number(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
