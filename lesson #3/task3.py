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