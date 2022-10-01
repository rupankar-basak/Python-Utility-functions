def get_all_files_in_dir(dir_path, file_ext):
    """
    Get all files in a directory with a specific extension
    :param dir_path: Directory path
    :param file_ext: File extension
    :return: List of files
    """
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f)) and f.endswith(file_ext)]