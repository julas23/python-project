from pydantic import BaseModel

class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation
    
    def calculate(self) -> float:
        if self.operation not in ['add', 'sub']:
            raise ValueError('Invalid operation. Must be add or sub.')

        if self.operation == 'add':
            result = self.a + self.b
        elif self.operation == 'sub':
            result = self.a - self.b

        if result < 0:
            raise ValueError('Result cannot be negative.')

        return result

def get_user_input():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = input("Enter the operation (add or sub): ").strip().lower()

        calc = Calculator(a=a, b=b, operation=operation)
        result = calc.calculate()

        print(f"The result is: {result}")
    except ValueError as ve:
        print(f"Error: {ve}")

get_user_input()