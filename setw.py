import os
import platform
import requests
import time
from pathlib import Path

# 读取 url.txt 文件中的链接
def read_url_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            url = file.readline().strip()  # 读取第一行并去除空白字符
            if not url:
                print(f"No link found, {file_path}")
                return None
            return url
    except FileNotFoundError:
        print(f"No file found,, {file_path}")
        return None

# 下载图片到本地
def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"Image downloaded, {save_path}")
        return True
    except Exception as e:
        print(f"Failed to download image, {e}")
        return False

# 设置壁纸
def set_wallpaper(image_path):
    system = platform.system()
    try:
        if system == "Windows":
            # Windows 系统
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
            print("Wallpaper is set, Windows")
        elif system == "Darwin":
            # macOS 系统
            script = f"""
            tell application "System Events"
                set desktop picture to POSIX file "{image_path}"
            end tell
            """
            os.system(f"osascript -e '{script}'")
            print("Wallpaper is set, macOS")
        else:
            print(f"Unsupported operating system, {system}")
            return False
        return True
    except Exception as e:
        print(f"Failed to set wallpaper, {e}")
        return False

# 主函数
def main():
    # 文件路径
    url_file = "url.txt"
    image_path = "wallpaper.jpg"



    # 读取链接
    url = read_url_from_file(url_file)
    if not url:
        return

    # 下载图片
    if not download_image(url, image_path):
        return

    # 设置壁纸
    if not set_wallpaper(os.path.abspath(image_path)):
        return

if __name__ == "__main__":
    main()