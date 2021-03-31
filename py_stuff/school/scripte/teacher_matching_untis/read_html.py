from bs4 import BeautifulSoup

all_untis_teachers ={}

with open("leher_untis.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    for link in soup.find_all('a'):
        kuerzel = link.text
        nname = link.get('title')
        # print(link.text)
        # print(link.get('title'))
        all_untis_teachers[kuerzel] = nname
        fp.close()

#print(all_untis_teachers)