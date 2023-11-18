from PIL import Image, ImageDraw, ImageFont
import datetime
import os
import shutil
import fnmatch

print("请将所有待修改图片以*.jpg 扩展名格式放在 input_images 目录下")
input_image_folder = "./input_images"
extension = "*.jpg"
input_images = [file for file in os.listdir(input_image_folder) if fnmatch.fnmatch(file, extension)]

year = input("<请用英文输入法输入年，例如 2023>: ")
if not (year.isdigit() and len(year) == 4):
    print("年份为4位数字，注意输入法为英文半角")
    exit()
    
month = input("<请用英文输入法输入2位数字月，例如 02>: ")
if not (month.isdigit() and len(month) == 2 and int(month) < 13):
    print("月份为2位数字，注意输入法为英文半角")
    exit()

day = input("<请用英文输入法输入两位数字日，例如 09>: ")
if not (day.isdigit() and len(day) == 2 and int(day) < 32):
    print("日应为2位数字，注意输入法为英文半角")
    exit()
# Create a new image with white background
text_size = (88, 17)
text_img = Image.new('RGB', text_size, (240,238,251))


# Initialize the drawing context
# d = ImageDraw.Draw(img)
d = ImageDraw.Draw(text_img)

# Load a font (or use a default one)
font = ImageFont.load_default(16)

# Get current date and time
time = datetime.datetime(int(year), int(month), int(day)).strftime("%Y-%m-%d")

# Position for the text (e.g., bottom-right corner)
position = (2,1)

# Add text to the text image
d.text(position, time, fill=(0,0,0), font=font)

# Overlay the text image on the JPEG image
# combined = Image.alpha_composite(background.convert('RGBA'), text_img)
position = (46, 19)


# Save the image
#combined_rgb = combined.convert('RGB')
output_folder = "./output_images"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
else:
    print(f"删除'{output_folder}'")
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)

for image in input_images:
    background = Image.open(f"{input_image_folder}/{image}")
    background.paste(text_img, position)
    background.save(f"{output_folder}/{image}_updated.jpg")
    print(f"更新{image}完成...")
print(f"全部处理完成！请检查 {output_folder}")

