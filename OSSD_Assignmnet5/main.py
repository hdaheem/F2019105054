import urllib.request
from selenium import webdriver
import random
driver=webdriver.Chrome()
driver.get("https://unsplash.com/s/photos/nature")
dr=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
im=dr.find_elements_by_tag_name("img")
a=0
for i in im:
     link=i.get_attribute("src")
     if i.get_attribute("class")=="YVj9w":
        path="nature/b"+str(random.random())+ ".jpg"
        urllib.request.urlretrieve(link,path)
        a=a+1
        if a==10:
            break

driver.get("https://unsplash.com/s/photos/spring")
dri=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
img=dri.find_elements_by_tag_name("img")
b=0
for j in img:
     link=j.get_attribute("src")
     if j.get_attribute("class")=="YVj9w":
        path="spring/b"+str(random.random())+ ".jpg"
        urllib.request.urlretrieve(link,path)
        b=b+1
        if b==10:
            break

driver.get("https://unsplash.com/s/photos/earth")
driv=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
imag=driv.find_elements_by_tag_name("img")
c=0
for k in imag:
     link=k.get_attribute("src")
     if k.get_attribute("class")=="YVj9w":
        path="earth/b"+str(random.random())+ ".jpg"
        urllib.request.urlretrieve(link,path)
        c=c+1
        if c==10:
            break

driver.get("https://unsplash.com/s/photos/yoga")
drive=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
image=drive.find_elements_by_tag_name("img")
d=0
for l in image:
     link=l.get_attribute("src")
     if l.get_attribute("class")=="YVj9w":
        path="yoga/b"+str(random.random())+ ".jpg"
        urllib.request.urlretrieve(link,path)
        d=d+1
        if d==10:
            break

driver.get("https://unsplash.com/s/photos/animal")
driverr=driver.find_element_by_css_selector("#app > div > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div > div")
imagee=driverr.find_elements_by_tag_name("img")
e=0
for m in imagee:
     link=m.get_attribute("src")
     if m.get_attribute("class")=="YVj9w":
        path="animal/b"+str(random.random())+ ".jpg"
        urllib.request.urlretrieve(link,path)
        e=e+1
        if e==10:
            break