from decorator import logger
import os

@logger('Logs\logger.log')
def sortted_files(dir):
    list_sorted = {}
    FILE_LOG_DIR = dir
    BASE_PATH = os.getcwd()
    list_files = os.listdir(FILE_LOG_DIR)
    for files in list_files:
        files_path = os.path.join(BASE_PATH, FILE_LOG_DIR, files)
        # print(files_path)
        with open(files_path, encoding='utf-8') as file:
            data = file.read()
        with open(files_path, encoding='utf-8') as file:
            line_file = sum(1 for line in file)
        list_sorted[line_file] = [files, data]
        sort_list_sorted = sorted(list_sorted)
    with open('sort_files.txt', 'w') as sort_file:
        for sort in sort_list_sorted:
            sort_file.write(f'{list_sorted[sort][0]}\n{sort}\n{list_sorted[sort][1]}\n')

sortted_files('sorted')