#!/usr/bin/env python3
import re
import click
from bs4 import BeautifulSoup
import requests

@click.command()
@click.option('-u', help="Enter target url to crawl")
@click.option('-o', help="The output file to save crawl results.", default="results.txt")
def main(u, o):
    """Simple reconnoisance tool to harvest comments in webpages"""
    click.echo(f"Web crawling on {u} started successfully...")

    comment_regex = re.compile('<!--(.*?-->)')

    with requests.Session() as session:
        resp = session.get(u)
        soup = BeautifulSoup(resp.text, 'lxml')
        #TODO: search for hidden attributes, may be useful
        comments = soup.find_all(text=comment_regex)
        print(comments)

if __name__ == "__main__":
    main()