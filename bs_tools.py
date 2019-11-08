import requests
from bs4 import BeautifulSoup
import re
def InstaStats(username):
	try:
		request=requests.get("https://instagram.com/{}".format(username))
		if request.status_code==404:
			return "Аккаунт не существует"
		soup=BeautifulSoup(request.text,"html.parser")
		meta=soup.findAll("meta")[-2]
		followers=re.findall("([0-9k.m]+) Followers",str(meta))[0]
		following=re.findall("([0-9k.m]+) Following",str(meta))[0]
		posts=re.findall("([0-9k.m]+) Posts",str(meta))[0]
		return (followers,following,posts)
	except:
		return "Что то пошло не так"