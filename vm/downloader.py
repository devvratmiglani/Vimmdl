import re
import subprocess
import requests
import click
from bs4 import BeautifulSoup

def aria_download(dl_urls):
    if len(dl_urls) != 0:
            click.echo("\nDownload Starting:")
    for x in dl_urls:
        click.echo(x.split('/')[-1])
        arg = ["aria2c","--dir",".","-j1","-Z",'--referer="https://vimm.net/vault/"',"-U","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"]
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
            r = requests.get(url)
        except:
            print("Skipping Url! - Cannot retrieve webpage.")
            continue
        soup = BeautifulSoup(r.text,"html.parser")
        try:
            dl_form = soup.find('form',{'id':'download_form'})
            dl_urls.append("https:" + dl_form['action'] + "?mediaId="+dl_form.input['value'])
        except:
            print("Skipping Url! - Cannot retrieve doenload information.")
            continue
    return dl_urls

def start_download(dl_urls):
    command = ["aria2c", "--version"]
    try:
        # Try to execute the command and capture the return code
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        if result.returncode == 0:
            print("aria2c requirement is satisfied")
            aria_download(dl_urls)
        else:
            print("aria2c is not installed")
            default_download(dl_urls)
    except subprocess.CalledProcessError:
        print("aria2c is not installed")
        default_download(dl_urls)
    except FileNotFoundError:
        print("aria2c is not installed")
        default_download(dl_urls)
