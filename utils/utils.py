import unicodedata
import shutil
import os
from typing import List

from numpy.core.multiarray import ndarray
from skimage import io

class StringUtil:
    def __init__(self):
        """Constructor for StringUtil"""

    @staticmethod
    def underscore_and_lowercase(words: str) -> str:
        return words.lower().replace(" ", "_")

    @staticmethod
    def is_http_url(src) -> bool:
        result = unicodedata.normalize('NFKD', src).encode('ascii', 'ignore')
        return result[:4].decode() == "http"

class ProgressBarUtil:

    @staticmethod
    def update(progress: int, total: int):
        workdone = progress / total
        print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(workdone * 50), workdone * 100), end="", flush=True)


class FileUtil:
    image_extensions = ['.bmp', '.gif', '.jpeg', '.jpg', '.png', '.raw', '.tiff']

    def __init__(self):
        """Constructor for FileUtil"""

    @staticmethod
    def folder_total_size(folder_path: str) -> float:
        return sum([os.path.getsize(os.path.join(folder_path, f))
                    for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))
                    and FileUtil.is_image(os.path.join(folder_path, f))])

    # @staticmethod
    # def mean_folder_file_size(folder_path: str) -> float:
    #     return FileUtil.folder_total_size(folder_path) / FileUtil.nb_file_in_folder(folder_path)

    @staticmethod
    def nb_file_images_in_folder(folder_path: str) -> int:
        num_files = len(FileUtil.get_images_file_path_array(folder_path))
        return num_files

    @staticmethod
    def get_file_extension(path: str) -> str:
        return os.path.splitext(path)[1]

    @staticmethod
    def is_image(path: str) -> bool:
        return FileUtil.get_file_extension(path).lower() in FileUtil.image_extensions

    @staticmethod
    def get_images_file_path_array(folder_path) -> List[str]:
        return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                os.path.isfile(os.path.join(folder_path, f))
                and FileUtil.is_image(os.path.join(folder_path, f))]

    @staticmethod
    def open(path: str) -> ndarray:
        return io.imread(path)

    @staticmethod
    def create_folder(folder_path: str):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    @staticmethod
    def generate_next_file_path(folder_path: str, file_prefix: str):
        counter = len([i for i in os.listdir(folder_path) if file_prefix in i]) + 1
        
        file_name = file_prefix + "_" + str(counter) #+ extension
        return os.path.join(folder_path, file_name)

    @staticmethod
    def save_file(processed_image: ndarray, label_name: str, src_path: str, folder_path: str, file_prefix: str):
        FileUtil.create_folder(folder_path)
        full_destination = FileUtil.generate_next_file_path(folder_path, file_prefix)
        io.imsave(full_destination + ".jpg", processed_image)

        src_file = os.path.join(src_path, label_name)
        shutil.copy(src_file, folder_path)
        dst_file = os.path.join(folder_path,label_name)
        os.rename(dst_file, full_destination + ".txt")

    # @staticmethod
    # def save_txt_file(label_name: str, src_path: str, folder_path: str, file_prefix: str):
        
        
class NoImageFoundException(Exception):
    pass
