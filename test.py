import sys
from PIL import Image

# 將Pillow庫的安裝路徑加入到系統路徑中
sys.path.append('../Anaconda3/Lib/site-packages/PIL')

# 讀取示例圖像
im = Image.open('lena.png')
im.show()
