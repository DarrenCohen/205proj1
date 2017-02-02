
im = Image.open('Project1Images\Project1Images\1.png')
rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

print r, g, b
