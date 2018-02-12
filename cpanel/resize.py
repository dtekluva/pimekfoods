from PIL import Image

basewidth = 540
baseheight = 326

def shrink(name):

    img = Image.open(name)
    print(img)
    if img.size[1] != 540:
        img = img.resize((basewidth,baseheight), Image.ANTIALIAS)
        img.save(name)
    print(img)