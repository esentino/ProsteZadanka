def zamiana(zdanko):

    zdanie = ""
    zdanko = list(zdanko)
    for i in range(len(zdanko)):
        if zdanko[i].islower():
            zdanie += zdanko[i]

    return "\t".join(zdanie)


zdanie1 = "I cóż, że ze Szwecji."
zdanie2 = "Król Karol kupił Królowej Karolinie coś tam coś tam"

male_litery1 = zamiana(zdanie1)
male_litery2 = zamiana(zdanie2)
print(male_litery1, male_litery2, sep='\n')
