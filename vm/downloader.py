import re
import subprocess
import requests
import click
from colorama import Fore, Style
from bs4 import BeautifulSoup
import certifi
# import truststore
import os

verification = certifi.where()
if os.name != "nt":
    verification = False

# truststore.inject_into_ssl()

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

def aria_download(dl_urls):
    if len(dl_urls) != 0:
            click.echo("\nDownload Starting:")
    for x in dl_urls:
        click.echo(x.split('/')[-1])
        arg = ["aria2c","--dir","/downloads","-j1","-Z",'--referer="https://vimm.net/vault/"',"-U","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"]
        arg.extend(dl_urls)
    subprocess.run(arg)
    # add user agent and referer and your download will work like a charm
def default_download(dl_urls):
    pass



def validate_urls(ctx,param,urls):
    validated_urls = []
    for url in urls:
        if bool(re.match("^https://vimm.net/vault/[0-9]+$",url)) == True:
            validated_urls.append(url)
        else:
            print(f"Skipping bad url -> {url}")
    return validated_urls

def retrieve_download_urls(urls):
    dl_urls = []
    for url in urls:
        try:
            r = requests.get(url,headers=headers,verify=verification)
        except:
            print("Skipping Url! - Cannot retrieve webpage.")
            continue
        soup = BeautifulSoup(r.text,"html.parser")
        try:
            dl_form = soup.find('form',{'id':'dl_form'})
            if dl_form.parent.div != None:
                print(Style.BRIGHT+Fore.RED+"Some Downloads Maybe Not Available!"+Style.BRIGHT+Fore.WHITE)
                print(Style.BRIGHT+Fore.YELLOW+"Reason: "+Style.BRIGHT+Fore.WHITE+dl_form.parent.text)
            dl_urls.append("https:" + dl_form['action'] + "?mediaId="+dl_form.input['value'])
        except:
            print("Skipping Url! - Cannot retrieve download information.")
            continue
    return dl_urls

def start_download(dl_urls):
    if len(dl_urls) == 0:
        raise ValueError(Style.BRIGHT+Fore.RED+"Download List is Empty")
    command = ["aria2c", "--version"]
    try:
        # Try to execute the command and capture the return code
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if result.returncode == 0:
            print(Style.BRIGHT+Fore.GREEN+"Aria2c "+Style.BRIGHT+Fore.WHITE+"requirement is satisfied")
            aria_download(dl_urls)
        else:
            print(Style.BRIGHT+Fore.RED+"Aria2c"+Style.BRIGHT+Fore.WHITE+" is not installed")
            default_download(dl_urls)
    except subprocess.CalledProcessError:
        print(Style.BRIGHT+Fore.RED+"Aria2c"+Style.BRIGHT+Fore.WHITE+" is not installed")
        default_download(dl_urls)
    except FileNotFoundError:
        print(Style.BRIGHT+Fore.RED+"Aria2c"+Style.BRIGHT+Fore.WHITE+" is not installed")
        default_download(dl_urls)
