from fake_math import divide as fm
from true_math import divide as tm

first = 13
second = 0

fake_result = fm(first, second)
true_result = tm(first, second)

print(f"Результат из fake_math: result {fake_result}")
print(f"Результат из true_math: result {true_result}")



