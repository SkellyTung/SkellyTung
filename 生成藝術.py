from PIL import Image

# 創建一個新的圖像，大小為200x200，背景為黑色
img = Image.new('RGB', (200, 200), 'black')

# 在圖像上繪製一個綠色的矩形，左上角座標為(50, 50)，右下角座標為(150, 150)
for x in range(50, 150):
    for y in range(50, 150):
        img.putpixel((x, y), (0, 255, 0))

# 保存圖像
img.save('generated_image.png')
# 顯示生成的圖像
img.show()