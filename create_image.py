from PIL import Image, ImageDraw, ImageFilter
import glob
import random
import time
from datetime import datetime
from time import sleep

'''def circle_blur(file_name, count):
    im1 = Image.open(file_name)
    im1 = im1.resize((600, 600), Image.BICUBIC)
    im2 = Image.new("RGBA", im1.size, (0, 0, 0, 0))
    mask = Image.new("L", im1.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((25, 25, 575, 575), fill=255)
    im = Image.composite(im1, im2, mask)
    mask_blur = mask.filter(ImageFilter.GaussianBlur(15))
'''
def circle_blur(file_name, count):
    im1 = Image.open(file_name)
    im1 = im1.resize((600, 600), Image.BICUBIC)
    im2 = Image.new("RGBA", im1.size, (0, 0, 0, 0))
    mask = Image.new("L", im1.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((25, 25, 575, 575), fill=255)
    im = Image.composite(im1, im2, mask)
    mask_blur = mask.filter(ImageFilter.GaussianBlur(15))
    im = Image.composite(im1, im2, mask_blur)
    timestr = time.strftime('%Y%m%d-%H%M%S')
    save_directory = "junk"
    file_path = f"{save_directory}{timestr}{count + 1}X.png"
    im.save(file_path)
    return im
def get_images():
    directorylist =glob.glob("/mnt/HDD500/collections/Beautiful_Background1/*.jpg")
    directorylist =glob.glob("/mnt/HDD500/collections/Beautiful_Background1/*.jpg")
    directorylist =glob.glob("/mnt/HDD500/collections/Beautiful_Background1/*.jpg")
    M = random.sample(directorylist, 3)
    M1 = random.choice(glob.glob(M[0]))
    M2 = random.choice(glob.glob(M[1]))
    M3 = random.choice(glob.glob(M[2]))
    return M1, M2, M3

def save_file():
    save_directory = "junk/"
    now = datetime.now()
    timestr = time.strftime('%Y%m%d-%H%M%S')
    milliseconds = now.microsecond // 1000
    file_name = f"{save_directory}{timestr}{str(milliseconds).zfill(3)}__.png"
    return file_name


def create_image():
    M1, M2, M3 = get_images()
    img1 = Image.open(M1).convert("RGBA")
    img1 = img1.resize((640, 640), Image.BICUBIC)
    alpha = img1.split()[3]
    alpha = Image.eval(alpha, lambda a: 85)
    img1.putalpha(alpha)
    img2 = Image.open(M2).convert("RGBA")
    img2 = img2.resize((640, 640), Image.BICUBIC)
    alpha = img2.split()[3]
    alpha = Image.eval(alpha, lambda a: 85)
    img2.putalpha(alpha)
    img3 = Image.open(M3).convert("RGBA")
    img3 = img3.resize((640, 640), Image.BICUBIC)
    alpha = img3.split()[3]
    alpha = Image.eval(alpha, lambda a: 85)
    img3.putalpha(alpha)
    result = Image.alpha_composite(Image.alpha_composite(img1, img2), img3)
    im4 = Image.new("RGBA", img3.size, (255, 255, 255, 255))
    im4.paste(result, (0, 0))
    im4 =im4.convert("RGB")
    # Display the resulting image with no transparency
    #List0 = glob.glob("/home/jack/Desktop/HDD500/collections/art-nouveau/*.jpg")
    #List1 = glob.glob("/mnt/HDD500/collections/Prodia_640x640/*.jpg")
    List1 = glob.glob(DIRECTORY[3]+"/*.jpg")
    FILEname = random.choice(List1)
    img5 = Image.open(FILEname).convert("RGBA")
    saveDirectory = "junk/"
    count = 1
    print(FILEname)
    im = circle_blur(FILEname, count)
    #im = circle_blur(FILEname,saveDirectory,count)
    im = im.resize((250,250),Image.BICUBIC)
    loc = 640//2-250
    im4.paste(im, (loc, loc),im)
    Border = "/mnt/HDD500/YOUTUBE/assets/canvas-boarder.png"
    border = Image.open(Border)
    border = border.resize((im4.size),Image.BICUBIC).convert("RGBA")
    im4.paste(border, (0,0),border)
    im4.save(save_file())
    print("A copy of this image is saved as: ",save_file())
    return im4

create_image()
