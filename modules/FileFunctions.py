import os
from glob import glob


class FileFunctions(object):
    def __init__(self, root_path="/"):
        """
        :param root_path: Root of the folder where the certificates are.
        """
        self.root_path = root_path

    def get_certification_documents(self, file_type='jpg'):
        """
        :param file_type: Type of file that you want to return documents
        :return: Return all files listed on root_path directory (children
        include) with file_type type, default is return all .jpg files
        """
        glob_path = self.root_path + f"/**/*.{file_type}"
        full_items = glob(glob_path, recursive=True)
        return full_items

    @staticmethod
    def get_filename(file_path):
        """
        :param file_path: Path of file that you want know only name.
        :return: Name of the file_path file.
        """
        name = os.path.basename(file_path)
        return name.rsplit('.', 1)[0]
