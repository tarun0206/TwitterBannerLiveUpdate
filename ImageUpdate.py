from PIL import Image, ImageDraw, ImageFont


# print(tar.replace("normal","bigger"))


def update_image():
    img1 = Image.open("New_banner.jpg")
    img = Image.open('pp1.jpg')
    img2 = img.resize((114,114))
    back_im = img1.copy()
    back_im.paste(img2,(1292,318))
    back_im.save('Edited.jpg', quality=95)
    img1.close()
    img2.close()