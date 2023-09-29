from pathlib import Path
from django.conf import settings
from PIL import Image
import os



def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_widht, original_height = img_pil.size

        if original_widht <= new_width:
            img_pil.close()
            return
        new_height = round((new_width * original_height) / original_widht)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        return new_img