table = 'tabela'
conditions = {'category':'dev'}


zmienna = f"SELECT * FROM {table} WHERE {' and '.join([f'{condition}=?' for condition in conditions])} "
print(zmienna)