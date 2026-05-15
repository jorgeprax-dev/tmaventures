from PIL import Image, ImageDraw, ImageFont
   
   # Create a 32x32 image with a black background
   img = Image.new('RGB', (32, 32), color = 'black')
   
   # Create a drawing context
   draw = ImageDraw.Draw(img)
   
   # Define the font and size
   font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 24)
   
   # Draw the "TMA" text in the center of the image
   draw.text((5, 0), "TMA", font=font, fill=(255, 255, 255))
   
   # Save the image as favicon.ico
   img.save('/mnt/user-data/outputs/favicon.ico', sizes=[(32, 32)])