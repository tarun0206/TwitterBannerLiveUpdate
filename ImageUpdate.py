from PIL import Image, ImageDraw, ImageFont


tar = "https://pbs.twimg.com/profile_images/1542931751898869760/l39azKag_bigger.jpg"
# print(tar.replace("normal","bigger"))
image_path = "TwitterBannerLiveUpdate\edited.jpg"

def update_image(miage_path):
    img1 = Image.open("TwitterBannerLiveUpdate/New_banner.jpg")
    img = Image.open('TwitterBannerLiveUpdate\pp1.jpg')
    img2 = img.resize((115,115))
    back_im = img1.copy()
    back_im.paste(img2,(1292,318))
    back_im.save('rocket_pillow_paste_mask_circle.jpg', quality=95)
    img1.close()
    img2.close()
    # return image_path

update_image(image_path)