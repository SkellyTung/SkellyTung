from PIL import Image, ImageDraw
import random

# 創建一個新的200x200的白色圖像
img = Image.new('RGB', (200, 200), 'white')

# 創建一個ImageDraw對象，以便繪製形狀
draw = ImageDraw.Draw(img)

# 食物形狀列表
shapes = ['circle', 'rectangle', 'triangle']

# 食物顏色列表
colors = [(255, 165, 0), (255, 192, 203), (218, 165, 32), (138, 43, 226), (255, 0, 0)]

# 繪製5個不同的食物形狀
for i in range(5):
    # 隨機選擇形狀和顏色
    shape = random.choice(shapes)
    color = random.choice(colors)

    # 隨機生成形狀的位置和大小
    x1, y1 = random.randint(0, 150), random.randint(0, 150)
    x2, y2 = x1 + random.randint(20, 50), y1 + random.randint(20, 50)

    # 根據選擇的形狀繪製
    if shape == 'circle':
        draw.ellipse((x1, y1, x2, y2), fill=color)
    elif shape == 'rectangle':
        draw.rectangle((x1, y1, x2, y2), fill=color)
    elif shape == 'triangle':
        draw.polygon([(x1, y2), (x2, y2), ((x1 + x2) // 2, y1)], fill=color)

# 顯示生成的圖像
img.show()
