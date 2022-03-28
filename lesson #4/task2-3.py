import requests
from bs4 import BeautifulSoup
import time


eur = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&sxsrf=APq-WBvtlsFjF6IS3dInrc2gvf--bzG1cA%3A1648395311060&ei=L4RAYuWqA8ak3APcjKzIDg&ved=0ahUKEwil_tuHz-b2AhVGEncKHVwGC-kQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBDJAzIFCAAQkgM6BwgjELADECc6BwgAEEcQsAM6CggAEEcQsAMQyQM6CAgAEJIDELADOhIILhDHARDRAxDIAxCwAxBDGAE6CQgAEIAEEAoQKjoFCAAQgAQ6BAgjECc6EAgAEIAEEIcCELEDEIMBEBQ6DwgAELEDEIMBEAoQRhCCAjoKCAAQsQMQgwEQCjoHCAAQsQMQCjoHCAAQyQMQCkoECEEYAEoECEYYAFBKWNcPYL8RaANwAXgAgAHrAYgBpAWSAQU3LjAuMZgBAKABAcgBC8ABAdoBBAgBGAg&sclient=gws-wiz'
usd = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4&aqs=chrome.0.69i59j69i57j69i59l2j69i61l3.3304j0j4&sourceid=chrome&ie=UTF-8'
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}


def currency_rates(cur):
    if cur.upper():
        cur = cur.lower()
        if cur == 'usd':
            full_page = requests.get(usd, headers=headers)
            soup = BeautifulSoup(full_page.content, "html.parser")
            convert = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
            print(time.strftime("%Y.%m.%d\n%H:%M:%S"))
            print('Один доллар равен ' + convert[0].text + ' ₽')
        if cur == 'eur':
            full_page = requests.get(eur, headers=headers)
            soup = BeautifulSoup(full_page.content, "html.parser")
            convert = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
            print(time.strftime("%Y.%m.%d\n%H:%M:%S"))
            print('Один евро равен ' + convert[0].text + ' ₽')
    else:
        if cur == 'usd':
            full_page = requests.get(usd, headers=headers)
            soup = BeautifulSoup(full_page.content, "html.parser")
            convert = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
            print(time.strftime("%Y.%m.%d\n%H:%M:%S"))
            print('Один доллар равен' + convert[0].text + ' ₽')
        if cur == 'eur':
            full_page = requests.get(eur, headers=headers)
            soup = BeautifulSoup(full_page.content, "html.parser")
            convert = soup.findAll('span', {'class': 'DFlfde SwHCTb', 'data-precision': 2})
            print(time.strftime("%Y.%m.%d\n%H:%M:%S"))
            print('Один евро равен ' + convert[0].text + ' ₽')




currency_rates('eur')
