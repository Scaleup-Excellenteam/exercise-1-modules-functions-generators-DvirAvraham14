import constant
import os

def find_deep_files(folder_path):
    """
    Returns a list of files in the given folder that start with the letters "deep".
    Parameters:
        folder_path (str): The path to the folder to search.
    Returns:
        A list of file names (strings) that start with the letters "deep".
    Example:
        >>> find_deep_files('/home/user/images')
        ['deep1.jpg', 'deep2.png']
    """
    files = [] # list to save the files name
    for filename in os.listdir(folder_path):
        if filename.startswith(constant.START_WITH):
            files.append(filename)
    return files


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    files = find_deep_files(r"/Users/dviravraham/PycharmProjects/pythonProject2/test")
    print(files)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
