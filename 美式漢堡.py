from PIL import Image, ImageDraw, ImageFont
import random

# 載入漢堡素材圖片
bun_top = Image.open('bun_top.png').convert('RGBA')
bun_bottom = Image.open('bun_bottom.png').convert('RGBA')
beef_patty = Image.open('beef_patty.png').convert('RGBA')
cheese = Image.open('cheese.png').convert('RGBA')
lettuce = Image.open('lettuce.png').convert('RGBA')
tomato = Image.open('tomato.png').convert('RGBA')

# 創建一個新的500x500的透明圖像
img = Image.new('RGBA', (500, 500), (0, 0, 0, 0))

# 創建一個ImageDraw對象，以便繪製形狀和文字
draw = ImageDraw.Draw(img)

# 繪製漢堡素材
x, y = 100, 50
img.paste(bun_top, (x, y), bun_top)
y += bun_top.size[1]
img.paste(beef_patty, (x, y), beef_patty)
y += beef_patty.size[1]
img.paste(cheese, (x, y), cheese)
y += cheese.size[1]
img.paste(lettuce, (x, y), lettuce)
y += lettuce.size[1]
img.paste(tomato, (x, y), tomato)
y += tomato.size[1]
img.paste(bun_bottom, (x, y), bun_bottom)

# 繪製文字
text = 'Delicious Burger'
font = ImageFont.truetype('arial.ttf', 36)
bbox = draw.textbbox((0, 0), text, font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
x = (img.width - w) // 2
y = img.height - h - 20
draw.text((x, y), text, font=font, fill='black')

# 顯示生成的圖像
img.show()
