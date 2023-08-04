# подсчет суммы налога

def print_tax_document(tax, *args, **kwargs): # *-неизвестное количество
    price_sum = 0
    for i in args:
        price_sum = price_sum + i * tax / 100
    print('Сумма налога: ', price_sum)

    for i_info, i_value in kwargs.items(): #имен. арг. передаются как словарь(имя=значение)
       print('{}: {}'.format(i_info, i_value)) 



my_tax = int(input('Величина налога: '))
print_tax_document(my_tax, 1000, 950, 880, 920, 990,  #налог и цены на товары (позиционные арг)
                   year=1997, 
                   doc_type='Report', 
                   operation_id=1110034)            # именнованные аргументы 