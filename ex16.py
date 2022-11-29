def total_shopping_card(shopping_list):
    max=0
    max_a=0
    max_s=0
    for i in shopping_list:
        len_name=len(i[0])
        if len_name>max:
            max=len_name
        len_amount=len(str(i[2]))
        if len_amount>max_a:
            max_a=len_amount
        s=round((i[1]*i[2]),2)
        len_sum=len(str(s))
        if len_sum>max_s:
            max_s=len_sum

    total=0
    for i in shopping_list:
        name=i[0]
        price=i[1]
        amount=i[2]
        sum=round(price*amount,2)
        total+=sum
        len_name = len(name)
        len_amount=len(str(amount))
        len_sum=len(str(sum))
        sum_string1="x {}"

        if len_name<max:
            r = max - len_name
            name_string="{}({})"+r*" "+2*"\t"
        else:
            name_string="{}({})"+2*"\t"



        if len_sum<max_s and len_amount<max_a:
            r2 = max_s - len_sum
            sum_string2=2*"\t"+r2*" "
            amount_string = "{}"
        elif len_sum==max_s and len_amount<max_a:
            r3 = max_a - len_amount
            sum_string2 = "\t"+2*r3*" "
            amount_string = "{}"
        elif len_sum<max_s and len_amount==max_a:
            t = "\t"
            ile_t=len(t.expandtabs())
            c=ile_t-2*(max_a-1)
            sum_string2 = +c*" "
            amount_string = "{}"



        p=name_string+sum_string1+sum_string2+amount_string
        print(p.format(name, price, amount, sum))
    print("Do zapłaty:\t\t\t\t\t{}".format(round(total,2)))


shopping_list = [
    ('mleko', 1.99, 2),
    ('chleb', 2.42, 3),
    ('masło', 5.99, 1),
    ('cola', 7.99, 3),
    ('ziemniaki', 0.99, 1.3)
    ]

total_shopping_card(shopping_list)
# Wypisze
# mleko(1.99)       x 2     3.98
# chleb(2.42)       x 3     7.26
# masło(5.99)       x 1     5.99
# cola(7.99)        x 3    23.97
# ziemniaki(0.99)   x 1.3   1.28
# Do zapłaty:              42.49
#