# 安裝 Tesseract 與套件
!sudo apt update
!sudo apt install -y tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-chi-tra
!pip install pytesseract Pillow

# 導入套件
from PIL import Image
import pytesseract
from google.colab import files
from IPython.display import display

# 上傳圖片
uploaded = files.upload()
image_path = list(uploaded.keys())[0]

# 打開並顯示圖片
image = Image.open(image_path)
print("上傳的圖片如下：")
display(image)

# OCR 辨識中英文
# lang 可以同時指定多個語言，用 '+' 連接
text = pytesseract.image_to_string(image, lang='eng+chi_tra', config='--psm 6')

print("OCR 辨識結果:")
print("-" * 40)
print(text.strip())
