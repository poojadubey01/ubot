_M='link-holder'
_L='entry-title'
_K='title'
_J='\rLOADING URLS: '
_I='Accept'
_H='User-Agent'
_G='||'
_F='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
_E='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
_D='div'
_C='html.parser'
_B='href'
_A=False
import random,sys
from urllib.parse import urlparse
import requests,urllib3
from bs4 import BeautifulSoup
from.constants import*
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def random_col():listt=['green','yellow','white'];return random.choice(listt)
def learnviral(page):
	links_ls=[];head={'user-agent':_E,'accept':_F,'sec-fetch-site':'none','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document'};r=requests.get(LEARNVIR+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);first=soup.find_all(_D,class_='content-box')
	for content_box in first:
		soup1=BeautifulSoup(str(content_box),_C);title_all=soup1.find_all('h3',class_=_L);links=soup1.find_all(_D,class_=_M)
		for(index,lk)in enumerate(links):title=title_all[index].text;links_ls.append(title+_G+lk.a[_B])
	return links_ls
def real_disc(page):
	A='style';links_ls=[];head={_H:_E,_I:_F};r=requests.get(REALDISC+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);udd=soup.find_all(_D,attrs={A:'margin-top:-274px;z-index:9;position: absolute; left: 0; margin-left: 15px; color: #fff; background: rgba(0,0,0,0.5); padding: 2px 4px; font-weight: 700;'});content=soup.find_all(_D,class_='white-block-content',attrs={A:';background-color: #333333;height: 160px;   overflow: hidden;'})
	for(index,i)in enumerate(content):
		sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush()
		if udd[index].text.replace('\n','')=='Udemy':url2=i.a[_B];r2=requests.get(url=url2,headers=head,verify=_A);soup1=BeautifulSoup(r2.content,_C);title=soup1.find(_K).text.replace(' Udemy Coupon - Real Discount','');links_ls.append(title+_G+soup1.find(_D,class_='col-sm-6 col-xs-6 letshover').a[_B])
	return links_ls
def udemy_freebies(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(UDEMYFREEBIES+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all(_D,'theme-block')
	for(index,items)in enumerate(all):title=items.img[_K];url2=items.a[_B];sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();r2=requests.get(url2,headers=head,verify=_A);soup1=BeautifulSoup(r2.content,_C);url3=soup1.find('a',class_='button-icon')[_B];link=requests.get(url3,verify=_A).url;links_ls.append(title+_G+link)
	return links_ls
def udemy_coupons_me(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(UDEMYCOUPONS+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all(_D,'td_module_1 td_module_wrap td-animation-stack')
	if page==1:all=all[2:]
	for(index,items)in enumerate(all):
		title=items.a[_K];url2=items.a[_B];sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();r2=requests.get(url2,headers=head,verify=_A);soup1=BeautifulSoup(r2.content,_C)
		try:ll=soup1.find('span',class_='td_text_highlight_marker_green td_text_highlight_marker').a[_B];links_ls.append(title+_G+ll)
		except:ll=''
	return links_ls
def discudemy(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(DISCUD+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all('section','card')
	for(index,items)in enumerate(all):
		try:title=items.a.text;url2=items.a[_B]
		except:title='';url2=''
		if url2!='':r2=requests.get(url2,headers=head,verify=_A);soup1=BeautifulSoup(r2.content,_C);next=soup1.find(_D,'ui center aligned basic segment');url3=next.a[_B];r3=requests.get(url3,headers=head,verify=_A);sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();soup3=BeautifulSoup(r3.content,_C);links_ls.append(title+_G+soup3.find(_D,'ui segment').a[_B])
	return links_ls
def tricksinfo(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(TRICKSINF+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all('a',class_='post-thumb')
	for(index,items)in enumerate(all):title=items['aria-label'];url2=items[_B];r2=requests.get(url2,headers=head,verify=_A);sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();soup1=BeautifulSoup(r2.content,_C);link=soup1.find(_D,'wp-block-button').a[_B];links_ls.append(title+_G+link)
	return links_ls
def freewebcart(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(WEBCART+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all('h2',class_=_K)
	for(index,items)in enumerate(all):title=items.text;url2=items.a[_B];r2=requests.get(url2,headers=head,verify=_A);sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();soup1=BeautifulSoup(r2.content,_C);link=soup1.find('a',class_='btn btn-default btn-lg')[_B];links_ls.append(title+_G+link)
	return links_ls
def course_mania(page):
	links_ls=[];head={_H:_E,'Referer':'https://coursemania.xyz/','Origin':'https://coursemania.xyz',_I:_F};r=requests.get(COURSEMANIA,headers=head,verify=_A);js=r.json()
	for items in js:title=items['courseName'];link=items['url'];links_ls.append(title+_G+link)
	return links_ls
def helpcovid(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(HELPCOV,headers=head,verify=_A);js=r.json()
	for items in js['courses']:title=items[_K];link=items['url'];links_ls.append(title+_G+link)
	return links_ls
def jojocoupons(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(JOJOCP+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all('h2',class_='font130 mt0 mb10 mobfont110 lineheight20')
	for(index,items)in enumerate(all):
		title=items.text;url2=items.a[_B];r2=requests.get(url2,headers=head,verify=_A);sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();soup1=BeautifulSoup(r2.content,_C);link=soup1.find(_D,class_='rh-post-wrapper')
		for tag in soup1.find_all('a'):
			try:
				if urlparse(tag[_B]).netloc=='www.udemy.com'or urlparse(tag[_B]).netloc=='udemy.com':links_ls.append(title+_G+tag[_B]);break
			except:r=''
	return links_ls
def onlinetutorials(page):
	links_ls=[];head={_H:_E,_I:_F};r=requests.get(ONLINETUT+str(page),headers=head,verify=_A);soup=BeautifulSoup(r.content,_C);all=soup.find_all('h3',class_=_L)
	for(index,items)in enumerate(all):title=items.text;url2=items.a[_B];r2=requests.get(url2,headers=head,verify=_A);sys.stdout.write(_J+animation[index%len(animation)]);sys.stdout.flush();soup1=BeautifulSoup(r2.content,_C);link=soup1.find(_D,class_=_M).a[_B];links_ls.append(title+_G+link)
	return links_ls