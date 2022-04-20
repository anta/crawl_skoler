from __future__ import print_function
import requests
import re
import sys

from bs4 import BeautifulSoup as bs

if len(sys.argv) != 2 :
    print("Example usage: python " + sys.argv[0] + " public.csv")
    sys.exit()
request = requests.get('https://politiken.dk/indland/art7082486/S%C3%A5dan-er-karakter%C2%ADgennemsnittet-p%C3%A5-landets-folkeskoler')

content = request.content

soup = bs(content, 'html.parser')  

table = soup.findChildren('table')[1]

rows = table.findChildren('tr')

f = open(str(sys.argv[1]), "w")
f.write("name;location\n")
for row in rows:
  cells = row.findChildren('td')
  rank = cells[0].getText()
  name = cells[1].getText()
  kommune = cells[2].getText()
  score = cells[3].getText()
  f.write(rank[:len(rank)-1] + " - " + name + " at " + kommune + " (" + score + ");" + name)
  f.write("\n")
  if float(score.replace(",", ".")) < 7.5:
    break
