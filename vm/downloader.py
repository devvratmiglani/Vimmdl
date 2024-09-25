import re
import subprocess
import requests
import click
from colorama import Fore, Style
from bs4 import BeautifulSoup

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
            r = requests.get(url,headers={"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"})
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
