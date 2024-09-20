from PIL import Image, ImageDraw
import random


# # Изменение цвета картинки на негатив.
# image = Image.open("forest1.jpg")
# draw = ImageDraw.Draw(image)
# width = image.size[0]
# height = image.size[1]
# pix = image.load()
#
# for i in range(width):
#     for j in range(height):
#             a = pix[i, j][0]
#             b = pix[i, j][1]
#             c = pix[i, j][2]
#             draw.point((i, j), (255 - a, 255 - b, 255 - c))
# image.save("forest1.jpg", "JPEG")

# # Изменение размер картинки
# image_path = './forest2.jpg'
# img = Image.open(image_path)
# new_image = img.resize((200, 385))
# new_image.save('./forest2.jpg')
