import os

def samples_path():
    path_exist = os.path.isdir(path)
    if path_exist is False:
        print("Path does not exist")
        time.sleep(2)
        exit()