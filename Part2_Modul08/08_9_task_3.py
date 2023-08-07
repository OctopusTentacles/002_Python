# Задача 3. Глубокое копирование
# Что нужно сделать
# Вы сделали для заказчика структуру сайта по продаже телефонов:

# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Куплю/продам телефон недорого'
# 		},
# 		'body': {
# 			'h2': 'У нас самая низкая цена на iPhone',
# 			'div': 'Купить',
# 			'p': 'Продать'
# 		}
# 	}
# }
# Заказчик рассказал своим коллегам на рынке, и они тоже захотели такой сайт, 
# только для своих товаров. Вы посчитали, что это лёгкая задача, 
# и быстро принялись за работу.

# Напишите программу, которая запрашивает у клиента, сколько будет сайтов, 
# а затем запрашивает название продукта и после каждого запроса 
# выводит на экран активные сайты.

# Условия: структуру сайта нужно описать один раз, копипасту никто не любит.
# Подсказка: используйте рекурсию.

# Пример:
# Сколько сайтов: 2
# Введите название продукта для нового сайта: iPhone
# Сайт для iPhone: 
# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Куплю/продам iPhone недорого'
# 		},
# 		'body': {
# 			'h2': 'У нас самая низкая цена на iPhone',
# 			'div': 'Купить',
# 			'p': ‘Продать'
# 		}
# 	}
# }

# Введите название продукта для нового сайта: Samsung
# Сайт для iPhone: 
# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Куплю/продам iPhone недорого'
# 		},
# 		'body': {
# 			'h2': 'У нас самая низкая цена на iPhone',
# 			'div': 'Купить',
# 			'p': ‘Продать'
# 		}
# 	}
# }

# Сайт для Samsung: 
# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Куплю/продам Samsung недорого'
# 		},
# 		'body': {
# 			'h2': 'У нас самая низкая цена на Samsung',
# 			'div': 'Купить',
# 			'p': ‘Продать'
# 		}
# 	}
# }



import copy


def create_sites(data, num):
    if num > 0:
        new_data = copy.deepcopy(data)
        
        site_name = input('\nВведите название продукта для нового сайта: ')
        new_data['html']['head']['title'] = f'Куплю/продам {site_name} недорого'
        new_data['html']['body']['h2'] = f'У нас самая низкая цена на {site_name}'
        
        list_sites[site_name] = new_data

        for key, value in list_sites.items():
            print(f'Сайт для {key}:'
                  f'\nsite = {value}')

        create_sites(data, num -1)


site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на телефон',
			'div': 'Купить',
			'p': 'Продать'
		}
	}
}

list_sites = dict()

sites_amt = int(input('Сколько сайтов: '))
create_sites(site, sites_amt)


# я не понимаю. хотел сделать через дополнительную функцию def search_element
# где менялось бы содержимое сайта, но не смог сохранить значения для возврата
# значение value не ложится в data_2
# в итоге тыкал - тыкал и вот так получилось, 
# все работает ))) походу я изначально не туда пошел и сильно заморочился


# def search_element(data_2, tag, change_1='title', change_2='h2'):
    
#     for key, value in data_2.items():
#         if key == change_1:
#             value = 'Куплю/продам {} недорого'.format(tag)
            
#         if key == change_2:
#             value = 'У нас самая низкая цена на {}'.format(tag)
            
#         if isinstance(value, dict):
#             search_element(value, tag)
#         list_sites[tag] = data_2
#         return 


# def create_sites(data, num):
#     if num > 0:
#         new_data = copy.deepcopy(data)
        
#         site_name = input('\nВведите название продукта для нового сайта: ')
#         search_element(new_data, site_name)
        
#         for key, value in list_sites.items():
#             print(f'Сайт для {key}:'
#                   f'\nsite = {value}')

#         create_sites(data, num -1)


# site = {
# 	'html': {
# 		'head': {
# 			'title': 'Куплю/продам телефон недорого'
# 		},
# 		'body': {
# 			'h2': 'У нас самая низкая цена на телефон',
# 			'div': 'Купить',
# 			'p': 'Продать'
# 		}
# 	}
# }

# list_sites = dict()

# sites_amt = int(input('Сколько сайтов: '))
# create_sites(site, sites_amt)
