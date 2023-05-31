from PIL import Image, ImageDraw

# Generate bun_top
bun_top = Image.new('RGBA', (200, 200), '#FDB813')
draw = ImageDraw.Draw(bun_top)
draw.ellipse((25, 25, 175, 175), fill='white', outline='black')
bun_top.save('bun_top.png')

# Generate bun_bottom
bun_bottom = Image.new('RGBA', (200, 200), '#FDB813')
bun_bottom.save('bun_bottom.png')

# Generate beef_patty
beef_patty = Image.new('RGBA', (200, 200), '#703C1F')
beef_patty.save('beef_patty.png')

# Generate cheese
cheese = Image.new('RGBA', (150, 150), '#FFE72D')
draw = ImageDraw.Draw(cheese)
draw.rectangle((0, 50, 150, 100), fill='#FDB813')
cheese.save('cheese.png')

# Generate lettuce
lettuce = Image.new('RGBA', (150, 150), '#50C878')
draw = ImageDraw.Draw(lettuce)
draw.rectangle((0, 50, 150, 100), fill='#FDB813')
lettuce.save('lettuce.png')

# Generate tomato
tomato = Image.new('RGBA', (150, 150), '#50C878')
draw = ImageDraw.Draw(tomato)
draw.rectangle((0, 50, 150, 100), fill='#FDB813')
tomato.save('tomato.png')

