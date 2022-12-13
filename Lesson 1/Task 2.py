# Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(not(x and y and z) == (not(x) or not(y) or not(z)))