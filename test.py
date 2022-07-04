from http import client
import http.client
from urllib import response
import requests
from values import *
from run import *
import base64
import email.parser
from bs4 import BeautifulSoup

headers = {
    'Authorization': f"Bearer {token}",
}

params = {
    'max_results': 1
}
file_name = 'New_banner.jpg'
# res = requests.get('https://api.twitter.com/2/users/858147288/followers', params=params, headers=headers)
# print(res.json())

def cvt_2_base64(file_name):
    with open(file_name , "rb") as image_file :
        data = base64.b64encode(image_file.read())
        filee = data.decode('utf-8')
    # print(data.decode('utf-8'))
    # print(filee)
    response = requests.post('https://api.twitter.com/1.1/account/update_profile_banner.json?banner='+filee, headers=headers)
    print(response)
    

cvt_2_base64(file_name)