graph = {
    'Biratnagar': [('Itahari', 22), ('Rangeli', 25),('Biratchowk', 30)],
    'Itahari': [('Biratnagar', 22), ('Dharan', 20), ('Biratchowk', 11)],
    'Dharan': [('Itahari', 20)],
    'Biratchowk': [('Itahari', 11), ('Kanepokhari', 10), ('Biratnagar', 30)],
    'Rangeli': [('Biratnagar', 25), ('Kanepokhari', 25), ('Urlabari', 40)],
    'Kanepokhari': [('Rangeli', 25), ('Biratchowk', 10), ('Urlabari', 12)],
    'Urlabari': [('Kanepokhari', 12), ('Damak', 6),('Rangeli',40)],
    'Damak': [('Urlabari', 6)]
}

print(graph)
