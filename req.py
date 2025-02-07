import requests
import time
import random

# Bing API
BING_API = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1612409408851&pid=hp&FORM=BEHPTB&uhd=1&uhdwidth=3840&uhdheight=2160"
BING_URL = "https://cn.bing.com"

def main():
    # 发送 HTTP 请求获取 Bing 壁纸数据
    response = requests.get(BING_API)
    response.raise_for_status()  # 检查请求是否成功
    data = response.json()

    # 解析 JSON 数据并获取图片 URL
    images = data["images"]
    url = BING_URL + images[0]["url"]
    url = url.split("&")[0]  # 去除 URL 中的多余参数

    # show_message("成功获取URL", url)
    print("Request the wallpaper URL, " + url)

    time.sleep(random.randint(1, 3))

    # 将结果写入文本文档  "url.txt"
    with open("url.txt", "w") as file:
        file.write(url)

    # show_message("成功写入到文件", url)
    print("Successfully wrote to file, url.txt")

if __name__ == "__main__":
    main()