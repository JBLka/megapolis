import csv


def paste_sort(file):
    for i in range(1, len(file)):
        x = file[i]
        j = i
        while j > 0 and float(file[j - 1]["Count"]) > float(x["Count"]):
            file[j] = file[j - 1]
            j -= 1
        file[j] = x
    return file[::-1]


with open('products.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=';'))
    reader = paste_sort(reader)
    # new_reader = reader[:10][::-1]
    new_reader = {}
    for i in reader[:10][::-1]:
        if i["Category"] not in new_reader.keys():
            new_reader[i["Category"]] = float(i["Count"])
        else:
            new_reader[i["Category"]] = new_reader[i["Category"]] + float(i["Count"])
    reader = []
    for i in new_reader:
        reader.append({"Category": i, 'Count': new_reader[i]})

with open('few_products.txt', "w", encoding='utf-8', newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['Category', 'Count'], delimiter=';')
    writer.writeheader()
    writer.writerows(reader)
    # Я понял задачу так, что все количества продуктов, относящихся к одной категории, нужно сложить,
    # отнести и записать в эту категорию
