import req
import setw
import time
import random
import os

# 新建url.txt文件
with open("url.txt", "w") as file:
    file.write("")

req.main()
setw.main()

time.sleep(random.randint(1, 3))

# 删除url.txt, wallpaper.jpg文件
os.remove("url.txt")
os.remove("wallpaper.jpg")

print()
print("Process finished with exit code 0")
time.sleep(1)
a = input("Press enter to exit")