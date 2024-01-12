import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def search(console,q):
    r = requests.get(f"https://vimm.net/vault/?p=list&system={console}&q={q}")

    soup = BeautifulSoup(r.text,"html.parser")
    if console == '':
        list_of_dict = []
        try:
            tr_tags = soup.find('table',{'class':'rounded'}).find_all('tr')[1:]
        except:
            print(f"No results Found!\n---------------------\nConsole: {console}\nQuery: {q}")
            return None
        
        for tr in tr_tags:
            all_td = tr.find_all('td')
            region = ''
            try:
                for x in all_td[2].find_all('img'):
                    region += x['title'] + ' '
            except:
                region = ''
            try:
                system = all_td[0].text
            except:
                system = ""
            try:
                Title = all_td[1].a.text
            except:
                Title = ""
            try:
                version = all_td[3].text
            except:
                version = ""
            try:
                link = 'https://vimm.net'+all_td[1].a['href']
            except:
                link = ''
        
            list_of_dict.append({'System':system,'Title':Title,'Region':region,'Version':version,'Link':link})
        print(tabulate(list_of_dict,headers="keys"))

    elif console != '':
        list_of_dict = []
        try:
            tr_tags = soup.find('table',{'class':'rounded'}).find_all('tr')[1:]
        except:
            print(f"No results Found!\n---------------------\nConsole: {console}\nQuery: {q}")
            return None
        
        for tr in tr_tags:
            all_td = tr.find_all('td')
            region = ''
            try:
                for x in all_td[1].find_all('img'):
                    region += x['title'] + ' '
            except:
                region = ''
            try:
                Title = all_td[0].a.text
            except:
                Title = ""
            try:
                version = all_td[2].text
            except:
                version = ""
            try:
                link = 'https://vimm.net'+all_td[0].a['href']
            except:
                link = ''
            try:
                langs = all_td[3].text
            except:
                langs = '-'
            try:
                ratings = all_td[4].a.text
            except:
                ratings = '-'
        
            list_of_dict.append({'Title':Title,'Region':region,'Version':version,'Languages':langs,'Rating':ratings,'Link':link})
        print(tabulate(list_of_dict,headers="keys"))