from PIL import Image
import pytesseract
from google.colab import files
from IPython.display import display  # 用來顯示圖片

# 上傳圖片
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# 打開圖片
image = Image.open(image_path)

# 顯示圖片
print("上傳的圖片如下：")
display(image)

# OCR 辨識英文文字
text = pytesseract.image_to_string(image, lang='eng', config='--psm 6')

# 顯示辨識結果
print("OCR 辨識結果:")
print("-" * 40)
print(text.strip())
