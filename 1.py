import csv

with open('products.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    zak = 0
    for i in reader:
        if i["Category"] == "Закуски":
            zak += float(i["Price per unit"]) * float(i["Count"])
        i["total"] = float(i["Price per unit"]) * float(i["Count"])
    print(int(zak))

with open("products_new.csv", "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'total'],
                            delimiter=';')
    writer.writeheader()
    writer.writerows(reader)
