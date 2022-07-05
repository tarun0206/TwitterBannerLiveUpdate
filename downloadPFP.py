import requests # request img from web
import requests
from values import *
import shutil # save img locally

# file_name = "pp1.jpg" #prompt user for file_name
headers = {
    'Authorization': f"Bearer {token}",
}

def downloadPfp():
    params = {
    'max_results': 1
    }
    res = requests.get('https://api.twitter.com/2/users/858147288/followers', params=params, headers=headers)
    id = res.json()['data'][0]['id']
    res2 = requests.get('https://api.twitter.com/1.1/users/show.json?user_id='+id, headers=headers)
    url = res2.json()['profile_image_url_https']
    print(url)
    url2 = url.replace("normal","bigger")
    res = requests.get(url2, stream = True)# res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open('pp1.jpg','wb') as f:
            shutil.copyfileobj(res.raw, f)
        # print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

# downloadPfp(file_name, headers)