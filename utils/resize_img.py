import os
from PIL import Image
from django.conf import settings

@staticmethod
def resize_image(img, new_width=500):
    img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
    img_pill = Image.open(img_full_path)
    # desempacotamento
    original_width, original_height = img_pill.size

    if original_width <= new_width:
        print("original > new_width")
        img_pill.close
        return

    new_height = round((new_width * original_height) / original_width)
    new_img = img_pill.resize((new_width, new_height), Image.LANCZOS )
    new_img.save(
        img_full_path,
        optimize=True,
        quality=50
    )