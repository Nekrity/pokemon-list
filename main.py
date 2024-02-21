
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)
pokemon_sort=pokemons.copy()
a=0
b=0
print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by text in name")
    print("5. Search by length of name")
    print("6. Print first ten pokemon names")
    print("7. Print last ten pokemon names")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        num=int(input("Write down pokemon sequence number "))
        num=num-1
        print(pokemons[num])
        pass
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemon_sort.sort()
        print(pokemon_sort)
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pokemon_sort.sort(reverse = True)
        print(pokemon_sort)
        pass
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        
        text=input("input text ")
        pokemon_search=[x for x in pokemons if x.startswith(text)]
        print(pokemon_search)
        pass
    elif choice == '5':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        text=int(input("input length "))
        pokemon_length=[x for x in pokemons if len(x)==text]
        print(pokemon_length)
        pass
    elif choice == '6':
        print(pokemons[a:a+10])
        a+=10
        pass
    elif choice == '7':
        if (b==0):
            print(pokemons[-10:])
        else:
            print(pokemons[b-10:b])
        b+=-10
        pass
    elif choice == '8':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 8")

    print("==========================")
