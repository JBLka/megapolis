import csv


def paste_sort(file):
    for i in range(1, len(file)):
        x = file[i]
        j = i
        while j > 0 and file[j - 1]["Category"] > x["Category"]:
            file[j] = file[j - 1]
            j -= 1
        file[j] = x
    return file


with open('products.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    reader = paste_sort(reader)
    first_category = reader[0]['Category']
    max_price = 0
    for i in reader:
        if i['Category'] == first_category and float(i['Price per unit']) > max_price:
            max_price = float(i['Price per unit'])
            product = i['product']
    print(
        f"В категории: {first_category} самый дорогой товар: {product} его цена за единицу товара составляет {max_price}")

with open('expensive_product.txt', "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'product', 'Date', 'Price per unit', 'Count'],
                            delimiter=';')
    writer.writeheader()
    writer.writerows(reader)
