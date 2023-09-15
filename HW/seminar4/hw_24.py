# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
import random
quantity_num = int(input("введите количество кустов: "))
berries = list(random.randint(0, 10) for i in range(quantity_num))
result = []
i = 0
sum = 0
sum_1 = 0
for i in range(len(berries)):
    sum = berries[i - 1] + berries[i] + berries[i - quantity_num + 1]
    print(berries[i], end= " ")
    # print()
    result.append(sum)
sorted(result)
print(result)
print(f"максимальное число ягод,собранных за один заход {result[-1]}")