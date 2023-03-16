import constant
import os

""" 
function that receive folder path and return all the fills
that start with the constant {START_WITH} = "deep"
"""
def find_deep_files(folder_path):
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
