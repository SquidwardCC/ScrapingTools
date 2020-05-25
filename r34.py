import rule34
import os
import time
from tqdm import tqdm
import PIL
from PIL import Image

#dir where all the funny little sub dirs go
data_dir = "C:\\Users\\MemeMaster\\Desktop\\r34_bot"
included_types = {".png", ".jpg", ".jpeg"}

rule34 = rule34.Sync()

#Downloads images from a tag
def getImages(tag):
    total_images = rule34.totalImages(tag)
    print("Total Images for " + tag + " : " + str(total_images))
    if total_images == 0:
        print("No images found...")
        return -1


    posts = rule34.getImageURLS(tag, singlePage=False, randomPID=True)

    tag_dir = data_dir + "/" + tag.replace("/", ".")

    try:
        os.mkdir(tag_dir)
    except:
        print("Directory Already there, renard")

    os.chdir(tag_dir)
    for post in tqdm(posts):
        if any(ext in post for ext in included_types):
            name = rule34.download(post)
            try:
                Image.open(name)
            except:
                print("Downloaded file corrupted... deleting")
                os.remove(name)
            time.sleep(.5)

#tags = {"sonic", "astolfo", "astolfo_(fate)", "shuten_douji", "artoria_pendragon_(all)"}
tags = {"mordred_(fate)", "kiyohime_(fate/grand_order)", "jeanne_d&#039;arc_(fate)", "jeanne_d&#039;arc_(fate)", "jack_the_ripper_(fate/apocrypha)"}

for tag in tags:
    getImages(tag)