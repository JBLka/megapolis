import csv

with open('products.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    for i in reader:
        date = i["Date"].split(".")
        product = i["product"]
        i["promocode"] = product[:2].upper() + date[0] + product[:-3:-1].upper() + date[1][::-1]
        # Генерируем промокод


with open("product_promo.csv", "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count', 'promocode'],
                            delimiter=';')
    writer.writeheader()
    writer.writerows(reader)
