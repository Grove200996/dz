# 1

import requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
content = requests.get(url)

with open('file.txt','r',encoding='utf-8') as f:
    my_list = []
    for line in f:
        info_split = line.replace('"', '').split(" ")
        info = info_split[0],info_split[5],info_split[6]
        my_list.append(info)

    print(*my_list,sep='\n')

# 2 

with open('text.txt', 'r+', encoding='utf-8') as f:
    f.write(content.text)
    r = {}
    for line in f:
        info_split = line.replace('"', '').split(' ')
        r.setdefault(info_split[0], 0)
        r[info_split[0]] += 1
    print(max(r.values()))
    print(max(r, key=r.get))
