#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 
import json
#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#


def sorting(expense):
    return int(expense[1])


expenses = []
print(''''
   _____                                       _____               _             
  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
             |_|                                                                      
      ''')
# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)

expense_file = open('expenses.json') 
expenses = json.load(expense_file) 
expense_file.close()


while True:
    command = input("\nChoose command:")
    if command == "1":
        nosaukums=input("Nosaukums: ")
        summa=int(input("summa: "))
        kategorija=input("Kategorija: ")
        expenses.append([nosaukums , summa , kategorija])
        
    
    if command == "2":
        for expense in expenses:
            print(expense)

    if command == "+":
        expenses.sort(key = sorting , reverse = True )
        print(expenses[0:10])
    if command == "-":
        expenses.sort(key = sorting ,)
        print(expenses[0:10])
    if command =="v":
        total = 0
        total_nr=0
        for expense in expenses:
            total = total + expense[1]
            total_nr=total_nr+1
        print("Vidējā summa: ",total/total_nr)

    if command == "e":
        print("Exiting...")
        break

with open("expenses.json", "w") as outfile:
    json.dump(expenses, outfile)

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)


