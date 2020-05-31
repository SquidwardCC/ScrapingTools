import requests
import os
import wget
import time
from tqdm import tqdm
from PIL import Image

data_dir = 'C:\\Users\\MemeMaster\\Desktop\\r34_bot\\gelbooru'
included_types = {".png", ".jpg", ".jpeg"}

#API URL
URL = "https://gelbooru.com/index.php?page=dapi&s=post&q=index"

pages = []
def getImages(tag):
    print("Getting Images for " + tag)

    i = 1
    post_len = 100
    while post_len == 100:
        PARAMS = {'tags': tag, 'json': 1, 'limit': 100, 'pid': i}
        r = requests.get(url=URL, params=PARAMS)
        json = r.json()
        post_len = len(json)
        pages.append(json)
        i+=1


    tag_dir = data_dir + "\\" + tag.replace("/", ".")

    try:
        os.mkdir(tag_dir)
    except:
        print("Directory Already there, renard")

    os.chdir(tag_dir)
    for page in tqdm(pages):
        for post in page:
            if any(ext in post['file_url'] for ext in included_types):
                name = wget.download(post['file_url'])
                time.sleep(.5)

                # TODO: Probably a better way to do this error check
                try:
                    Image.open(name)
                except:
                    print("Downloaded file corrupted... deleting")
                    os.remove(name)

tags = {"fate solo -male",
        "re:zero_kara_hajimeru_isekai_seikatsu solo -male",
        "gabriel_dropout solo",
        "boku_no_hero_academia solo -male",
        "kantai_collection solo"}

for tag in tags:
    getImages(tag)