import os
import json

# 定義圖片資料夾
image_folder = "img"

# 遍歷資料夾內的所有圖片
images = [os.path.join("img/", file) for file in os.listdir(image_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# 將清單輸出為 JSON 檔案
with open("images.json", "w") as f:
    json.dump(images, f)

print("images.json has been created!")