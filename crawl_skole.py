from __future__ import print_function
import requests
import re
import sys

from bs4 import BeautifulSoup as bs

request = requests.get(str(sys.argv[1]))

content = request.content

soup = bs(content, 'html.parser')  

table = soup.findChildren('table')[1]

rows = table.findChildren('tr')

f = open(str(sys.argv[2]), "w")
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
