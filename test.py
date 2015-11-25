from flask import Flask, render_template, request, session, redirect, url_for
import google, bs4, urllib2, re

url = urllib2.urlopen("https://en.wikipedia.org/wiki/Spider-Man")
page = url.read()
soup = bs4.BeautifulSoup(page, 'html')
raw = soup.get_text()
#Setup a regular expression to filter names out
pattern = "(([A-Z]{1})([a-z]*) ([A-Z]{1})([a-z]*))"
result = re.findall(pattern,raw)
print(result)
