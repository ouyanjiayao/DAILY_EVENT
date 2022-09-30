#!/usr/bin/env python
# coding: utf-8
import os,traceback
from PIL import Image


# 获取文件夹图片
def get_folder(fpath,wm_file,save_path):
    try:
        img_suffix_list = ['png', 'jpg', 'bmp']
        for i in os.listdir(path):
            if i.split('.')[-1] in img_suffix_list:
                img_path = path + '/' + i
                img_water_mark(img_file=img_path,wm_file=wm_file,save_path=save_path)
    except Exception as e:
        print(traceback.print_exc())


# 右下角
def img_water_mark(img_file, wm_file,save_path):
    try:
        img = Image.open(img_file)  # 打开图片
        watermark = Image.open(wm_file)  # 打开水印
        img_size = img.size
        wm_size = watermark.size
        # 如果图片大小小于水印大小
        if img_size[0] < wm_size[0]:
            watermark.resize(tuple(map(lambda x: int(x * 0.5), watermark.size)))
        print('图片大小：', img_size)
        wm_position = (img_size[0]-wm_size[0],img_size[1]-wm_size[1]) # 默认设定水印位置为右下角
        layer = Image.new('RGBA', img.size)  # 新建一个图层
        layer.paste(watermark, wm_position)  # 将水印图片添加到图层上
        mark_img = Image.composite(layer, img, layer)
        new_file_name = '/new_'+img_file.split('/')[-1]
        mark_img.save(save_path + new_file_name)
    except Exception as e:
        print(traceback.print_exc())








# 平铺
from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image, text):
    font = ImageFont.truetype('C:\Windows\Fonts\STXINGKA.TTF', 36)

    # 添加背景
    new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # 添加水印
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(0, rgba_image.size[0], font_len*10+100):
        for j in range(0, rgba_image.size[1], 100):
            image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 50))
    text_overlay = text_overlay.rotate(-15)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    # 裁切图片
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text




 
if __name__ == "__main__":
    # 右下角
    save_path = 'C:\\Users\\ADMIN\\Downloads'
    wm_file = "C:\\Users\\ADMIN\\Downloads\\454564.jpg"
    get_folder(r'C:\\Users\\ADMIN\\Downloads\\454564.jpg',wm_file,save_path)

    # 平铺
    img = Image.open("E:\\DeskTop\\123.png")
    im_after = add_text_to_image(img, u'20211209')
    im_after.save(u'154.png')











