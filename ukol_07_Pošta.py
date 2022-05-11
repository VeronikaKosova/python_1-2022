import re
from cgitb import html
from dataclasses import replace

import pandas

with open ("posta.html", encoding='utf-8') as vstup:
  posta = vstup.read()
print(posta)
posta.replace("\n", " ")
print(re.sub("\s+", " ", posta))
reg_vyr_posta = re.compile("\d{3}\s\d{2}\s\w*\s\w*\s\w*\s*")
print(reg_vyr_posta.findall(posta))


