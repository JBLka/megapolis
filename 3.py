import csv


with open('products.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    Category = input()
    while Category != "молоко":
        Count = 999999999999
        for i in reader:
            if i["Category"] == Category and float(i["Count"]) < Count:
                Count = float(i["Count"])
                product = i["product"]
        if Count != 999999999999:
            print(f"В категории: {Category} товар: {product} был куплен {Count} раз")
        else:
            print("Такой категории не существует в нашей БД")
        Category = input()