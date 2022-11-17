import click
import requests

def isLink(str):
    return str.startswith("https://") or str.startswith("http://") or str.startswith("www.")

def printUrlStatus(url):
    response = requests.get(url)
    print(str(response.status_code) + ": " + url)

def printUrlStatusWithCode(url, status_code):
    response = requests.get(url)
    if (response.status_code == status_code):
        print(str(response.status_code) + ": " + url)

@click.command()
@click.option('--status_code', type=click.INT, help='Specify what HTTP status code a response needs to be for link to be printed out')
@click.argument('input_file', type=click.Path(dir_okay=False))
def checkUrlsFromFile(input_file, status_code):
    """This script checks GitHub links from an input file to see if they are valid. It prints out the HTTP status code for web requests made on each link."""

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for url in lines:
        url = url.strip()
        if isLink(url):
            if (status_code):
                printUrlStatusWithCode(url, status_code)
            else:
                printUrlStatus(url)

if __name__ == "__main__":
    checkUrlsFromFile()