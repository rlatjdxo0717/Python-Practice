import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/running/current.nhn"
result = requests.get(url)
# print(result.content)

content = BeautifulSoup(result.content, "html.parser")

dt_list = content.findAll("dt",{"class":"tit"})

print(dt_list[0])
