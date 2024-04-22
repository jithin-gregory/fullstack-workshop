import os
from fastapi import UploadFile

from config import static_folder_root, image_folder_root


class ImageService:

    def upload_image(self, image: UploadFile,filename: str):
        _, extension = os.path.splitext(image.filename)
        folder_path = os.path.join(static_folder_root, image_folder_root, filename + extension)
        try:
            image_contents = image.file.read()
            with open(folder_path, 'wb') as file:
                file.write(image_contents)
        except Exception:
            raise
        finally:
            image.close()


