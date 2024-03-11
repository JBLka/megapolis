import csv

with open('products.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    Category = input()
    while Category != "молоко":  # Пока мы не ввели "молоко"
        Count = 999999999999
        for i in reader:
            if i["Category"] == Category and float(i["Count"]) < Count:
                Count = float(i["Count"])  # Если категория та и количество купленных товаров меньше сохраненного
                product = i["product"]  # Записываем количество продаж и название продукта
        if Count != 999999999999:  # Если переменная поменялась, то мы нашли товары из этой категории
            print(f"В категории: {Category} товар: {product} был куплен {Count} раз")
        else:  # Если не поменялась - не нашли
            print("Такой категории не существует в нашей БД")
        Category = input()
