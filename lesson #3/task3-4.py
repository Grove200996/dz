# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.

def thesaurus(*names):
    arr = {}
    for name in names:
        letter = name[0].capitalize()
        if letter not in arr:
            arr[letter] = []
            arr[letter].append(name)

    return arr

###################

def thesaurus_adv(*names_surnames):
    arr = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        arr.setdefault(surname[0], {})
        arr[surname[0]].setdefault(name[0], [])
        arr[surname[0]][name[0]].append(name_surname)
    return arr



