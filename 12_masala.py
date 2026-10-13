import csv
total=0
sales=[]
with open("sales.csv","r")as file:
    for mahsulot in csv.DictReader(file):
            quantity = int(mahsulot["quantity"])
price = int(mahsulot["price"])
daromad = quantity * price
total += daromad
sales.append([mahsulot["product"], quantity, daromad])
with open("report.txt", "w", encoding="utf-8") as file:
  file.write(f"Umumiy tushum: {total}\n")
  print(mahsulot)
  if sales:
       print("Umumiy tushum: ",sales)
       file.write(f"Eng ko'p sotilgan: {max(sales, key=lambda x: x[1])[0]} \n")