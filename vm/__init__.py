import click
from tabulate import tabulate
from . import console_list
from . import search
from . import downloader

@click.group()
def cli():
    pass

@cli.command("consoles")
def consoles():
    print(search.string_forer(tabulate(console_list.consolex,headers='keys')))

def get_console(ctx, param, value):
    try:
        console_code = console_list.consoles[value]
    except:
        click.echo("Bad Console! Use argument \'consoles\'")
        raise click.Abort()
    return console_code

def validate_query(ctx, param, value):
    return value or ("",)

@cli.command("search")
@click.argument('console',nargs=1,callback=get_console)
@click.argument('query',nargs=-1, type=click.UNPROCESSED,callback=validate_query)
def _search(console,query):
    for q in query:
        result =  search.search(console,q)

@cli.command("download")
@click.argument("urls", nargs=-1, type=click.UNPROCESSED, required=False, callback=downloader.validate_urls)
def _download(urls):
    dl_urls = downloader.retrieve_download_urls(urls)
    downloader.start_download(dl_urls)
    
# cli()