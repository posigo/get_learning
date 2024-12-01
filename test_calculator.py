from calculator import Calculator

# Задания
# 1. Разработчику 1 - реализовать функцию умножения
# 2. Разработчику 2 - реализовать функцию деления

calc = Calculator()
print(calc.sum(23,37))
result_sum = calc.sum(2,4,5)
calc.print_last_res()

print(calc.multiply(25, 4))
result_multiply = calc.multiply(3, 5, 10)
calc.print_last_res()