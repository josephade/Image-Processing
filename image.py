from PIL import Image, ImageFilter

img = Image.open('pikachu.jpg')

# filtered_img = img.convert('L')
# filtered_img.save("greyscale.png", "png")
img.show()
# print(img.size)