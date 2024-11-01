from PIL import Image
import os

# 画布大小
canvas_width = 1419
canvas_height = 2796

# 遮罩图片路径
mask_path = './main/iPhone.png'

# 输入图片文件夹路径
input_folder = './main/rounded'

# 输出文件夹路径
output_folder = './output'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 打开遮罩图像
mask = Image.open(mask_path)

# 获取输入文件夹中所有png格式图片的文件名
input_image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

# 查看目标文件夹中png格式图片的数量
print(f"输入文件夹中png格式图片的数量为: {len(input_image_files)}")

# 处理图片
for img_name in input_image_files:
    img_path = os.path.join(input_folder, img_name)
    img = Image.open(img_path)
    new_img = Image.new('RGBA', (canvas_width, canvas_height))
    # 计算居中位置
    x_offset = (canvas_width - img.width) // 2
    y_offset = (canvas_height - img.height) // 2
    new_img.paste(img, (x_offset, y_offset))
    new_img.paste(mask, (0, 0), mask)
    output_path = os.path.join(output_folder, os.path.splitext(img_name)[0] + '.png')
    new_img.save(output_path)