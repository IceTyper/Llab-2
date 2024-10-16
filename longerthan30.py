import csv
DATASET_PATH = 'books.csv'


#Берёт самую первую строку и превращает её в список
def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(";")
    title = [col.strip() for col in title]
    return title


#Превращает строку в список, учитывая все кавычки и точки с запятыми
#Возвращает словарь, где ключами выступают элементы списка из get_title, а значением - элементы списка этой функции
def get_object(line, title):        
    fields = []
    value = ''
    in_complex = False

    for char in line:
        if in_complex:
            value += char
            if char == '"':
                value = value[:-1]
                fields.append(value)
                value = ''
                in_complex = False
        else:
            if char not in [';', '"']:
                value += char
                continue
            if char == ';':
                fields.append(value)
                value = ''
                continue
            if char == '"':
                in_complex = True
                continue

    return {col: f for col, f in zip(title, fields)}



with open(DATASET_PATH) as dataset:
    title = get_title(dataset)
    counter = 0
    for line in dataset:
        res = get_object(line, title)
        if len(res.get('Название')) > 30:
            counter += 1
    print(counter)




