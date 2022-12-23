# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

a = int(input('Input divisible number: '))
b = int(input('Input divider: '))
precision = int(input('Input precision: '))

result = float(round(a/b, precision))

print(result)