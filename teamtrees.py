from bs4 import BeautifulSoup
import re
import requests


page = requests.get("https://teamtrees.org/")

soup = BeautifulSoup(page.content, 'html.parser')
count = str(soup.find(id="totalTrees"))

p = re.compile('\d+').findall(count)
count = p[5]
count = list(count)

j=0
for i in range(len(count)-1, -1, -1):
    j = j +1
    if j == 3:
        count.insert(i, ',')
        j = 0

count = ''.join(count)
print(count, "Trees planted so far")

leader = soup.find_all('p', class_='text-spruce font-black text-lg')
trees_planted_by_peop = soup.find_all('div', class_='mt-0 md:mt-4 bg-lightMoss rounded-full text-white text-bold px-4 relative badge')

names = []
for name in leader:
    names.append(name.string)

i=0
trees_planted = []
for num in trees_planted_by_peop:
    trees_planted.append(num.string)
for planted in trees_planted[:10]:
    print(names[i].ljust(20, '-'), planted)
    i = i + 1

