import os

from fastapi import UploadFile

from config import static_folder_root, image_folder_root


class ImageService:

    def __init__(self) -> None:
        self.__folder_path = str(os.path.join(static_folder_root, image_folder_root))

    def upload_image(self, image: UploadFile, filename: str):
        _, extension = os.path.splitext(image.filename)
        folder_path = os.path.join(self.__folder_path, filename + extension)

        existing_files = self.find_file_by_name(filename)
        for file in existing_files:
            os.remove(file)

        try:
            image_contents = image.file.read()
            with open(folder_path, "wb") as file:
                file.write(image_contents)
        except Exception:
            raise
        finally:
            image.close()

    def get_image_path(self, filename: str):
        files = self.find_file_by_name(filename)
        if len(files) > 0:
            return files[0]
        return None

    def find_file_by_name(self, filename: str):
        matches = []
        for root, _, files in os.walk(self.__folder_path):
            for name in files:
                # Extract the filename without extension
                file_name_without_ext = os.path.splitext(name)[0]
                if file_name_without_ext == filename:
                    matches.append(os.path.join(root, name))
        return matches


if __name__ == '__main__':
    service = ImageService()
    service.find_file_by_name("bfhgd")
