from PIL import Image, ImageDraw

# 創建空白圖像
burger = Image.new('RGBA', (600, 600), (255, 255, 255, 255))

# 加載素材圖像
bun_top = Image.open('bun_top.png').convert('RGBA')
bun_bottom = Image.open('bun_bottom.png').convert('RGBA')
beef_patty = Image.open('beef_patty.png').convert('RGBA')
cheese = Image.open('cheese.png').convert('RGBA')
lettuce = Image.open('lettuce.png').convert('RGBA')
tomato = Image.open('tomato.png').convert('RGBA')

# 繪製漢堡素材
burger.paste(bun_top, (0, 0), bun_top)
burger.paste(beef_patty, (0, 100), beef_patty)
burger.paste(cheese, (0, 150), cheese)
burger.paste(lettuce, (0, 200), lettuce)
burger.paste(tomato, (0, 250), tomato)
burger.paste(bun_bottom, (0, 400), bun_bottom)

# 保存生成的漢堡圖像
burger.save('burger.png')
# 顯示生成的圖像
burger.show()