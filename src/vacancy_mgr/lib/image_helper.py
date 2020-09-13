"""
System Name: Vasyworks
Project Name: vacancy_mgr
Encoding: UTF-8
Copyright (C) 2020 Yasuhiro Yamamoto
"""
import os
import shutil
import qrcode
from PIL import Image, ImageDraw, ImageFont


class ImageHelper:
    """ 画像ヘルパークラス"""
    @staticmethod
    def save_image(image: Image, file_path, max_size=1280):
        """画像の保存"""
        file_basename = os.path.basename(file_path)
        file_dir = file_path.replace(file_basename, '')
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)

        image_tmp = ImageHelper.rotate_image(image)

        w, h = image_tmp.size
        if w > max_size or h > max_size:
            if w < h:
                image_cnv = image_tmp.resize((int(w / h * max_size), max_size)).convert('RGB')
            else:
                image_cnv = image_tmp.resize((max_size, int(h / w * max_size))).convert('RGB')
        else:
            image_cnv = image_tmp.convert('RGB')

        image_cnv.save(file_path, quality=95, optimize=True)

    @staticmethod
    def copy_image_file(src, dest):
        """画像ファイルのコピー"""
        ans = False

        if os.path.exists(src) and not os.path.exists(dest):
            try:
                shutil.copy2(src, dest)
                ans = True
            except:
                ans = False

        return ans

    @staticmethod
    def delete_image(file_path):
        """画像の削除"""
        if os.path.exists(file_path):
            os.remove(file_path)

    @staticmethod
    def make_qrcode(data, file_path, force=False):
        """QRコード画像の作成"""
        if os.path.exists(file_path):
            if force:
                os.remove(file_path)
            else:
                return

        file_dir = os.path.dirname(file_path)
        if not os.path.isdir(file_dir):
            os.makedirs(file_dir)

        img = qrcode.make(data)
        img.save(file_path)

    @staticmethod
    def rotate_image(image: Image):
        """
        画像ファイルをEXIF情報に合わせて回転
        """
        if image is None:
            raise ValueError

        orientation = 1
        exif_info = image._getexif()
        if exif_info:
            orientation = exif_info.get(0x112, 1)

        ans = image

        if orientation == 2:
            # 左右反転
            ans = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif orientation == 3:
            # 180度回転
            ans = image.transpose(Image.ROTATE_180)
        elif orientation == 4:
            # 上下反転
            ans = image.transpose(Image.FLIP_TOP_BOTTOM)
        elif orientation == 5:
            # 左右反転して90度回転
            ans = image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
        elif orientation == 6:
            # 270度回転
            ans = image.transpose(Image.ROTATE_270)
        elif orientation == 7:
            # 左右反転して270度回転
            ans = image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
        elif orientation == 8:
            # 90度回転
            ans = image.transpose(Image.ROTATE_90)

        return ans
