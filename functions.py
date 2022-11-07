documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
# ___________________________________________________________________
def find_name(doc):
    n_doc = input('Введите номер документа: ')
    n = 0
    for i in doc:
        if i["number"] == n_doc:
            print(f'Имя и фамилия по номеру документа: {i["name"]}')
            n = n + 1
    if n == 0:
        print(f'Такого номера документа не существует.')
        return find_name(doc)
# ___________________________________________________________________
def find_shelf(dir):
    n_doc = input('Введите номер документа: ')
    n = 0
    for polka, list_dok in dir.items():
        if n_doc in list_dok:
            print(f'Документ {n_doc} на полке {polka} ')
            n = n + 1
    if n == 0:
        print(f'Такого номера документа не существует.')
        return find_shelf(dir)
# ___________________________________________________________________
def list_doc(doc):
    print()
    for i in doc:
        print(i['type'], i['number'], i['name'])
# ___________________________________________________________________
def sl_dir(dir):
    print()
    for i, z in dir.items():
        print(f'Полка {i} - {z}')
# ___________________________________________________________________
def as_dir(dir):
    new_dir = input('Введите номер новый полки: ')
    if new_dir not in dir:
        dir[new_dir] = []
    else:
        a = []
        for i in dir.keys():
            a.append(int(i))
        print(f'Номер такой полки уже есть! \nСписок уже существующих полок: {a}')
        while new_dir in dir:
            new_dir = input('\nВведите номер новый полки: ')
        dir[new_dir] = []

    print(f'Вы завели полку № {new_dir}.')
#____________________________________________________________________
def add_doc(doc,dir):
    print('Создайте новый документ!')
    new_doc_type = input('Введите тип нового документа: ')
    new_doc_number = input('Введите номер нового документа: ')
    for i in doc:
        if new_doc_number in i["number"]:
            print('Документ с таким номером уже есть!')
            return add_doc(doc,dir)

    new_doc_name = input('Введите имя и фамилия для нового документа: ')
    new_doc_dir = input('Введите номер полки для нового документа: ')

    while new_doc_dir not in dir:
        print('Такой полки не существует!')

        list_dir = []
        for i in dir.keys():
            list_dir.append(int(i))
        print('Список существующих полок: ', list_dir)

        new_doc_dir = input('Введите номер полки: ')

    dir[new_doc_dir].append(new_doc_number)

    doc.append({})
    doc[-1]["type"] = new_doc_type
    doc[-1]["number"] = new_doc_number
    doc[-1]["name"] = new_doc_name

    print('Вы добавили документ!')
# ___________________________________________________________________
def del_doc(doc, dir):
    print('Удалять документ?')
    doc_type = input('Введите номер документа: ')
    n = 0
    for i in doc:
        if doc_type in i["number"]:
            doc.remove(i)
            n += 1
    for list in dir.values():
        if doc_type in list:
            list.remove(doc_type)

    print('Вы удалили документ!')

    if n==0:
        print('Такого номера документа не существует!')
        return del_doc(doc, dir)
#_____________________________________________________________________________________________
def m_dir(dir):
    doc_dir_old = input('Введите номер документа: ')
    n = 0
    for key, valio in dir.items():
        if doc_dir_old in valio:
            n += 1
            print(f'Документ сейчас на полке {key}')

    if n == 0:
        print('Такого номера документа не существует!')
        return m_dir(dir)

    list3 = []
    for i in dir.keys():
        list3.append(int(i))
    print(f'Список существующих полок: {list3}')

    dir_new = input('На какую полку вы хотите переместить?: ')

    while dir_new not in dir:
        print('Номера такой полки нет!')
        dir_new = input('На какую полку вы хотите переместить?: ')

    for value in dir.values():
        if doc_dir_old in value:
            value.remove(doc_dir_old)

    if dir_new in dir:
        dir[dir_new].append(doc_dir_old)

def read_write():
    with open('info.txt', 'a', encoding='UTF-8') as f:
        f.write(documents)
#____________________________________________________________________________________________________

def com(documents, directories):
    n = 1
    while n < 20:
        print()
        print('______________________________________________________________________________________')
        print('\t\t\tВЫБЕРИТЕ КОМАНДУ: \ndl-list     выведет список всех документов в определенном формате'
              '\nsl-list     выведет список всех полок в определенном формате'
              '\nad-add      добавить новый документ в каталог и в перечень полок\nas–add      создаст новую полку'
              '\nm-move      по номеру документа переместит с текущей полки на полку которую вы укажете'
              '\np-people    по номеру документа выведет имя человека \ns-shelf     по номеру документа выведет полку'
              '\nd–delete    по номеру документа удалит его из каталога и из перечня полок'
              '\nq-exit      выход')
        print('______________________________________________________________________________________')
        print(f'Запрос №{n}')
        commanda = input('Введите БУКВУ нужной команды: ')
        if commanda == 'p':
            find_name(documents)
        elif commanda == 's':
            find_shelf(directories)
        elif commanda == 'dl':
            list_doc(documents)
        elif commanda == 'ad':
            add_doc(documents, directories)
        elif commanda == 'd':
            del_doc(documents, directories)
        elif commanda == 'as':
            as_dir(directories)
        elif commanda == 'm':
            m_dir(directories)
        elif commanda == 'sl':
            sl_dir(directories)
        elif commanda == 'q':
            break
        n += 1

com(documents, directories)

