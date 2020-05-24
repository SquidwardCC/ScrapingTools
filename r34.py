import rule34
import os
import time

#dir where all the funny little sub dirs go
data_dir = "r34_bot"
included_types = {".png", ".jpg", ".jpeg"}

if not os.path.exists(data_dir):
    os.mkdir(data_dir)
    
rule34 = rule34.Sync()

#Downloads images from a tag
def getImages(tag):
    print("Total Images for " + tag + " : " + str(rule34.totalImages(tag)))

    posts = rule34.getImageURLS(tag, singlePage=False, randomPID=True)
    tag_dir = data_dir + "/" + tag

    try:
        os.mkdir(tag_dir)
    except:
        print("Directory Already there, renard")

    os.chdir(tag_dir)
    for post in posts:
        if any(ext in post for ext in included_types):
            rule34.download(post)
            time.sleep(.5)

if __name__ == "__main__":
    getImages(input("Tag: "))