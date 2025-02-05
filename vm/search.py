import requests
from colorama import Fore, Style
from bs4 import BeautifulSoup
from tabulate import tabulate
import certifi
import truststore

truststore.inject_into_ssl()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection": "keep-alive",
    "Referer": "https://vimm.net/vault/?p=list&system=PS2&q=gta",
    "Cookie": "counted=1",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1"
}

def search(console,q):
    r = requests.get(f"https://vimm.net/vault/?p=list&system={console}&q={q}",headers=headers,verify=certifi.where())

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
        print(string_forer(tabulate(list_of_dict,headers="keys")))

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
        print(string_forer(tabulate(list_of_dict,headers="keys")))


def string_forer(table_string:str):
    lines = table_string.split('\n')
    table_string = ""
    table_string += Style.BRIGHT+Fore.RED + lines[0] +'\n'
    table_string += Style.BRIGHT+Fore.WHITE + lines[1] + '\n'
    for i,line in enumerate(lines[2:]):
        if i%2 == 0:
            table_string += Style.BRIGHT+Fore.GREEN + line + '\n'
        if i%2 != 0:
            table_string += Style.BRIGHT+Fore.WHITE + line + '\n'
    return table_string