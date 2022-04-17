import re

buffer = {'username': '', 'domain': ''}
RE_PRODUCTS = re.compile(r'^([a-z 0-9_]+)[@]([a-z]+[.][a-z]+)')


def email_parser(mail):
    link = RE_PRODUCTS.findall(mail.lower())
    if link:
        name, adr = link[0]
    else:
        msg = f'wrong email: {mail}'
        raise ValueError(msg)
    print(f'name:{name}, domain:{adr}')


email_parser('someone@geekbrains.ru')
email_parser('gunner_777@mail.ru')
email_parser('200_grove_096@mail.ru')
