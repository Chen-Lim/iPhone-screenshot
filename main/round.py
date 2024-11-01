from PIL import Image, ImageDraw
import os


def create_rounded_image(image_path, output_path):
    # 1. 创建一个大小为1179*2556像素的画布
    canvas = Image.new('RGBA', (1179, 2556), (0, 0, 0, 0))

    # 2. 按照顺序插入一张图片
    img = Image.open(image_path).convert("RGBA")
    canvas.paste(img)

    # 3. 创建一个大小为1179*2556像素，圆角为100像素的圆角矩形蒙版遮罩
    mask = Image.new('L', (1179, 2556), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, 1179, 2556), radius=100, fill=255)

    # 4. 图片保留遮罩覆盖的部分，其他部分变成透明像素
    result = Image.new('RGBA', canvas.size)
    result.paste(canvas, (0, 0), mask)

    # 5. 输出为png格式图像
    result.save(output_path, "PNG")


if __name__ == "__main__":
    images_folder = "./images"
    output_folder = "./main/rounded"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(1, len(os.listdir(images_folder)) + 1):
        image_filename = f"IMG_{i}.png"
        image_path = os.path.join(images_folder, image_filename)
        output_filename = f"rounded_{i}.png"
        output_path = os.path.join(output_folder, output_filename)

        if os.path.exists(image_path):
            create_rounded_image(image_path, output_path)