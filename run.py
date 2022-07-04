import os
import requests
from values import *
from ImageUpdate import *
import tweepy 

followers = 0
userid = '858147288'

headers = {
    'Authorization': f"Bearer {token}",
}

# params = {
#     'user_id': userid,
#     'profile_image_url': 'normal',
# }
def getFollowerCount():
    global followers
    url = "https://api.twitter.com/1.1/users/show.json?user_id="+userid
    res = requests.get(url, headers=headers)
    followers = res.json()['followers_count']
    print(followers)
# response = requests.get('http://api.twitter.com/1.1/users/show.json?user_id=858147288', headers=headers)
# fd=response.json()
# print(fd['followers_count'])
# response = requests.get('https://api.twitter.com/2/users/'+userid+'/followers', params=params, headers=headers)
# response2 = requests.get('https://api.twitter.com/1.1/users/show.json',params = params, headers=headers)
# gat = response2.json()
# print(gat['profile_image_url_https'])
# print(response2.json())
# auth = tweepy.OAuth2BearerHandler(token)
# api = tweepy.API(auth)
# userid = 'tarun0206'
# print(api.get_followers())

# def get_list_of_followers(api, user_id):
#     MAX_FOLLOWERS = 2
#     followers = []
    

# get_list_of_followers(api,userid)

if __name__ == "__main__":
    file = open('oldFollower.txt','r+')
    count = int(file.readline())
    getFollowerCount()
    if followers > count:
        print("New follower")
        
        file = open("oldFollower.txt","w")
        file.write(str(followers))
        file.close()
    else:
        print("No new follower")