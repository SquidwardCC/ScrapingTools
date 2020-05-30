from psaw import PushshiftAPI
import os, requests
api = PushshiftAPI()

def saveImage(url, directory):
    if str(url).endswith((".jpg",".png",".jpeg")):
        imgData = requests.get(url).content
        saveAs = os.path.join(directory, url.split('/')[-1])
        with open(saveAs, "wb") as writer:
            writer.write(imgData)
        print("Wrote: ", saveAs)
    else:
        print("Not Image:", url)

sr = str(input("Subreddit:"))

writeDir = os.path.join("reddit_out", sr)
print(writeDir)
if not os.path.exists("reddit_out"):
    os.makedirs(sr)
if not os.path.exists(writeDir):
    os.makedirs(writeDir)

for entry in api.search_submissions(
                            subreddit=sr,
                            filter=['url'],
                            limit=None):
    saveImage(entry[1],writeDir)

