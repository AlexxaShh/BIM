user = ['Денис', 'Саша', 'Юлия', 'Денис', 'Саша', 'Людмила']
dictionary = {
    'Общее количество': 0,
    'Уникальные посещения': 0
}
dictionary['Общее количество'] = len(user)
dictionary['Уникальные посещения'] = len(set(user))
print(dictionary)
