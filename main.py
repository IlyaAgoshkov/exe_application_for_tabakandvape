def sum_user_list(user_list):
    sum = 0
    for i in user_list:
        sum += i
    return sum
n = int(input("Введите количество товаров:"))
user_list = []
i = 0

while i < n:
    price = int(input("Введите цену товара №" + str(i+1) + ": "))
    user_list.append(int(price))
    i += 1
m = int(input("Какую купюру вам дали? "))
print('Нужно выдать сдачу в размере:')
print(m-(sum_user_list(user_list)))
input()