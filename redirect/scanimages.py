import os
import json
import struct

# 定義圖片資料夾
image_folder = "img"

# 初始化清單
horizontal_images = []
vertical_images = []

def get_image_size(file_path):
    with open(file_path, 'rb') as f:
        header = f.read(24)
        
        # 判斷 JPEG 格式
        if header[0:2] == b'\xff\xd8':
            f.seek(0)
            size = 2
            ftype = 0
            while not 0xc0 <= ftype <= 0xcf:
                f.seek(size, 1)
                byte = f.read(1)
                while ord(byte) == 0xff:
                    byte = f.read(1)
                ftype = ord(byte)
                size = struct.unpack('>H', f.read(2))[0] - 2
            f.seek(1, 1)
            height, width = struct.unpack('>HH', f.read(4))
            return width, height

        # 判斷 PNG 格式
        elif header[0:8] == b'\x89PNG\r\n\x1a\n':
            width, height = struct.unpack('>II', header[16:24])
            return width, height

    return None, None  # 無法識別格式

# 遍歷資料夾內的所有圖片
for file in os.listdir(image_folder):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join("img/", file)
        
        # 取得圖片寬高
        width, height = get_image_size(image_path)
        
        # 判斷方向
        if width and height:
            if width >= height:
                horizontal_images.append(image_path)  # 橫向圖片
            else:
                vertical_images.append(image_path)    # 直向圖片

# 將清單輸出為 JSON 檔案
with open("images.json", "w") as f:
    json.dump(horizontal_images, f)

with open("images_vertical.json", "w") as f:
    json.dump(vertical_images, f)

print("images.json and images_vertical.json have been created!")