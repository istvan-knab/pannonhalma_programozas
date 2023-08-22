"""
Knáb István Gellért
SZTAKI
2023.07.21.
"""

# Megjelenítés a konzolon
print("Adj meg egy számot")

# Adat beolvasása
my_data = input()

# adattípus lekérdezése
print("A típus:" + str(type(my_data)))

#változók castolása
data_to_cast = 1

data_to_cast = int(data_to_cast)
print(data_to_cast)
data_to_cast = str(data_to_cast)
print(data_to_cast)
data_to_cast = float(data_to_cast)
print(data_to_cast)
data_to_cast = bool(data_to_cast)
print(data_to_cast)

"""
Hasznos függvények listákhoz
"""
my_list = [0,1,2,3,4,5,6]

#Összeg
sum_of_numbers = sum(my_list)

#Lista hossza
list_size = len(my_list)

#Szélsőérték
maximum = max(my_list)
minimum = min(my_list)

#Hatványok
alap = 5
hatvany = 2
eredmeny = pow(alap, hatvany)
