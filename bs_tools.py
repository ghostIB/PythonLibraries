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
def Translate(w,l):
	try:
		cyrilic=("й","ц","у","к","е","н","г","ш","щ","з","х","ъ","ф","ы","в","а","п","р","о","л","д","ж","э","я","ч","с","м","и","т","ь","б","ю")
		url="https://google.com/search?q={}"
		r="перевод {0} на {1}".format(w,l[:-2]+"ом")
		request=requests.get(url.format(r))
		soup=BeautifulSoup(request.text,"html.parser")
		translate=soup.find("div",class_="AP7Wnd")
		if len(translate.text.split())>4 or translate.text=="Зображення" or translate.text[0] in cyrilic:
			raise Exception("Error")
		return translate.text
	except:
		return "Что то пошло не так"