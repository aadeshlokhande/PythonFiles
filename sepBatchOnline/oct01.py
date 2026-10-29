# Importing the PIL library
from PIL import Image, ImageDraw, ImageFont

# Open an Image
img = Image.open('memes.jpg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

myFont = ImageFont.truetype('font/Oswald-DemiBold.ttf', 30)

# Add Text to an image
I1.text((72, 107), "dear students,", fill=(0, 0, 255), font=myFont)
I1.text((72, 111), "dear students,", fill=(0, 0, 255), font=myFont)
I1.text((75, 109), "dear students,", fill=(0, 0, 255), font=myFont)
I1.text((70, 109), "dear students,", fill=(0, 0, 255), font=myFont)
I1.text((72, 109), "dear students,", fill=(255, 0, 0), font=myFont)
# I1.text((72, 130), "plz join Btech", fill=(255, 0, 0), font=myFont)
# Save the edited image
img.save("memes2.jpg")

# homework100.txt----> 98

# ╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩╦╩