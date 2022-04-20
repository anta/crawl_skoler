from __future__ import print_function
import requests
import re
import sys

from bs4 import BeautifulSoup as bs

request = requests.get('https://politiken.dk/indland/art7082537/S%C3%A5dan-er-karaktergennemsnittet-p%C3%A5-landets-fri-og-privatskoler')

content = request.content

soup = bs(content, 'html.parser')  

table = soup.findChildren('table')[1]

rows = table.findChildren('tr')

f = open(str(sys.argv[1]), "w")
f.write("name;location\n")
count = 1
for row in rows:
  cells = row.findChildren('td')
  rank = count
  count = count + 1
  name = cells[0].getText()
  kommune = cells[1].getText()
  score = cells[2].getText()
  f.write(str(rank) + " - " + name + " at " + kommune + " (" + score + ");" + name)
  f.write("\n")
  if float(score.replace(",", ".")) < 7.5:
    break
