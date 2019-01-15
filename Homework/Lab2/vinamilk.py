from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
com = urlopen(url)
rawdata = com.read()
content = rawdata.decode('utf8')
soup = BeautifulSoup(content,'html.parser')
table = soup.find('table',id='tableContent')
tr_list = table.find_all('tr')
cont = ['Mục','Quý 4-2016','Quý 1-2017','Quý 2-2017','Quý 3-2017',]
data = []
vl = {}
for tr in tr_list:
    td_list = tr.find_all('td')
    if len(td_list)>7:
        for i in range(5):
            a = td_list[i].string
            a = str(a).lstrip()
            vl[cont[i]]= a
        data.append(OrderedDict(vl))
import pyexcel
pyexcel.save_as(records=data, dest_file_name="vinamilk.xlsx")
