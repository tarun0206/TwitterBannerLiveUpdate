import requests # request img from web
import shutil # save img locally
import wget

url = "https://pbs.twimg.com/profile_images/1542931751898869760/l39azKag_bigger.jpg" #prompt user for img url
file_name = "TwitterBannerLiveUpdate\pp1.jpg" #prompt user for file_name

res = requests.get(url, stream = True)# res = requests.get(url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')
