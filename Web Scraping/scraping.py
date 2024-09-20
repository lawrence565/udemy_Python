from bs4 import BeautifulSoup
import requests
import re

# 模擬獲得的資訊
res = requests.get("https://zh.wikipedia.org/zh-tw/%E5%93%88%E5%88%A9%C2%B7%E6%B3%A2%E7%89%B9")
soup = BeautifulSoup(res.text, "lxml")
result = soup.select("img.mw-file-element")
regex = r"Platform"
count = 0
for img in result:
  count += 1
  src = str(img.get("srcset"))
  if re.findall(regex, src):
    src = src.split(" ")[0]
    print("https:" + src)
    image = requests.get("https:" + src)
    try:
      with open("./platform_img.jpg", "wb") as img_file:
        img_file.write(image.content)
        img_file.close()
    except:
      print("Store failed")
    