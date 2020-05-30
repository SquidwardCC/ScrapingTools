import requests
import os
import wget
import time
from tqdm import tqdm
from PIL import Image

data_dir = 'C:\\Users\\MemeMaster\\Desktop\\r34_bot'
included_types = {".png", ".jpg", ".jpeg"}

#API URL
URL = "https://gelbooru.com/index.php?page=dapi&s=post&q=index"

def getImages(tag):
    PARAMS = {'tags': tag, 'json': 1, 'limit': 100}

    r = requests.get(url=URL, params=PARAMS)
    posts = r.json()

    tag_dir = data_dir + "\\" + tag.replace("/", ".")

    try:
        os.mkdir(tag_dir)
    except:
        print("Directory Already there, renard")

    os.chdir(tag_dir)

    for post in tqdm(posts):
        if any(ext in post['file_url'] for ext in included_types):
            name = wget.download(post['file_url'])
            time.sleep(.5)

            # TODO: Probably a better way to do this error check
            try:
                Image.open(name)
            except:
                print("Downloaded file corrupted... deleting")
                os.remove(name)

