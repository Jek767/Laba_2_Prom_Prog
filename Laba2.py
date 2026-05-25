print("Введите количество пропусков и количество пар")
propuski = int(input())
paru = int(input())
if propuski/paru <= 0.3:
    print("Скорее всего сдашь")
elif propuski/paru > 0.3 and propuski/paru <= 0.7:
    print("Шанс сдать есть")
else:
    print("Здравствуй небо в облаках..... А дальше петь будешь в казарме")
