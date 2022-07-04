import os
import requests
from values import *
import tweepy 


TOKEN = token
userid = '858147288'

headers = {
    'Authorization': f"Bearer {TOKEN}",
}

params = {
    'user_id': userid,
    'profile_image_url': 'normal',
}

response = requests.get('https://api.twitter.com/2/users/'+userid+'/followers', params=params, headers=headers)
response2 = requests.get('https://api.twitter.com/1.1/users/show.json',params = params, headers=headers)
gat = response2.json()
print(gat['profile_image_url_https'])
# print(response2.json())
# auth = tweepy.OAuth2BearerHandler(token)
# api = tweepy.API(auth)
# userid = 'tarun0206'
# print(api.get_followers())

# def get_list_of_followers(api, user_id):
#     MAX_FOLLOWERS = 2
#     followers = []
    

# get_list_of_followers(api,userid)