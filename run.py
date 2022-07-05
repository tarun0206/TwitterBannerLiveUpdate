import requests
import os
from values import *
from ImageUpdate import *
from downloadPFP import *
from ImageUpdate import *
import time
import tweepy 

followers = 0
userid = '858147288'

auth = tweepy.OAuth1UserHandler(API_key,API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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

if __name__ == "__main__":
    while True:    
        file = open('oldFollower.txt','r+')
        count = int(file.readline())
        getFollowerCount()
        if followers == count:
            print("No change")
            time.sleep(60)
        else:
            downloadPfp()
            print("New pfp")
            update_image()
            print("New banner")
            api.update_profile_banner('Edited.jpg')
            print("New banner updated")
            file = open("oldFollower.txt","w")
            file.write(str(followers))
            file.close()
            os.remove("Edited.jpg")
            os.remove("pp1.jpg")
            time.sleep(60)
