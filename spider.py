import pandas as pd
import requests
import os


num = 0
dom = []
folder = 'D:/video/'
os.makedirs(folder)
df = pd.read_csv('douyin.csv', headers=None, names=['url'])

for i in df['url'][2:]:
    if i not in dom:
        dom.append(i)

for j in dom:
    url = j
    num += 1
    response = requests.get(url, stream=True)
    filename = str(num) + '.mp4'
    with open('D:\\video\\' + filename, 'ab+') as f:
        f.write(response.content)
        f.flush()
        print(filename + "下载完成")