# Zadanie 13

def pokemon_text(text):
    new_string = ''
    for i in text:
        if text.index(i) % 2==0:
            new_string += i.upper()
        else:
            new_string += i
    return new_string

print(pokemon_text('jbjwqbejbwqe'))

# Zadanie 14

def divide_or_not_divide(by, not_by, max):
    lista = []
    for i in range(max+1):
        if i % by ==0 and i % not_by != 0:
            lista.append(i)
    return lista

print(divide_or_not_divide(3, 4, 15))

# Zadanie 15

def dividers(number):
    divider = []
    for i in range(1,number+1):
        if number % i == 0:
            divider.append(i)
    return divider

print(dividers(24))


# Zadanie 16

def total_shopping_card(shopping_list):
    sum = 0
    for i in range(len(shopping_list)):
        print(f"{shopping_list[i][0]}({shopping_list[i][1]})\t x "
              f"{shopping_list[i][2]}\t{round((shopping_list[i][1]*shopping_list[i][2]),2)}")
        value = round((shopping_list[i][1]*shopping_list[i][2]),2)
        sum += value

    print("Do zapłaty: ", sum)

shopping_list = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3),
    ('ziemniaki', 0.99, 1.3)
    ]

total_shopping_card(shopping_list)

# Zadanie 17

def total_shopping_card_change(shopping_list, paid):
    sum = 0
    for i in range(len(shopping_list)):
        print(f"{shopping_list[i][0]}({shopping_list[i][1]})\t x "
              f"{shopping_list[i][2]}\t{round((shopping_list[i][1]*shopping_list[i][2]),2)}")
        value = round((shopping_list[i][1]*shopping_list[i][2]),2)
        sum += value

    print("Do zapłaty: ", sum)
    print("Zapłacono:", paid)
    print("Reszta:", paid - sum)

shopping_list = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3),
    ('ziemniaki', 0.99, 1.3)
    ]

total_shopping_card_change(shopping_list, 100)
