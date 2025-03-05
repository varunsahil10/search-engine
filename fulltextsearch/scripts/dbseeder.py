import csv
from fulltextsearch.models import Product

def run():
    with open('./myntra_products_catalog.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        c=0
        for lines in csvFile:
                if c==0:
                    c=1
                    continue
                
                Product.objects.create(
                    pid = int(lines[0]),
                    name = lines[1],
                    brand = lines[2],
                    gender = lines[3],
                    price = float(lines[4]),
                    description = lines[6],
                    color = lines[7],
                )
                print(lines)

