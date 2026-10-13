balans = 500000
tarix = []

while True:
    tanlov = input("""
0. Chiqish
1. Balans
2. Pul qo'shish
3. Pul yechish
4. Tarix
5. Jami
6. Saqlash
Tanlang: """)

    match tanlov:
        case "1":
            print(f"""Balans: {balans} so'm""")

        case "2":
            miqdor = int(input("Miqdor: "))
            if miqdor <= 0:
                print("Manfiy yoki 0 mumkin emas!")
            else:
                balans += miqdor
                tarix.append(("kirim", miqdor))

        case "3":
            miqdor = int(input("Miqdor: "))
            if miqdor <= 0:
                print("Manfiy yoki 0 mumkin emas!")
            elif miqdor > balans:
                print("Pul yetarli emas!")
            else:
                balans -= miqdor
                tarix.append(("chiqim", miqdor))

        case "4":
            for turi, miqdor in tarix:
                print(f"""{turi}: {miqdor} so'm""")

        case "5":
            kirim = 0
            chiqim = 0
            for turi, miqdor in tarix:
                if turi == "kirim":
                    kirim += miqdor
                else:
                    chiqim += miqdor
            print(f"""Kiritilgan: {kirim} so'm, yechilgan: {chiqim} so'm""")

        case "6":
            with open("bank.txt", "w") as file:
                for turi, miqdor in tarix:
                    file.write(f"""{turi}: {miqdor} so'm\n""")
            print("Saqlandi!")

        case "0":
            break
        
        