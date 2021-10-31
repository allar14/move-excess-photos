import os
import pathlib
import shutil

ORIGINAL_FILE_EXTENSION = '.CR2'
SELECTED_FILE_EXTENSION = '.jpg'

ORIGINAL_FILES_PATH = 'photos'
SELECTED_FILES_PATH = 'photos/selected'
BACKUP_FILES_PATH = 'photos/backups'


# There are 2 folders with photos. One folder contains all taken photos (Original folder),
# another one - selected from first folder and processed (Selected folder).
# The goal is to compare files from all and selected folders by their names without extension
# and move non-matching files to the Backup folder.
def main():
    original_files_list = get_original_files_list()
    selected_file_list = get_selected_file_list()
    non_match_file_name_list = get_difference(original_files_list, selected_file_list)
    move_files_to_backup(non_match_file_name_list)


# Generates the list of file names without extension from the Original folder,
# and sorts in an alphanumeric/ascending order.

def get_original_files_list():
    list_original_files = []
    original_files = os.listdir(ORIGINAL_FILES_PATH)
    for file in original_files:
        file_extension = pathlib.Path(file).suffix  # function to return the file extension
        if file_extension == ORIGINAL_FILE_EXTENSION:
            original_file_name = pathlib.Path(file).stem
            list_original_files.append(original_file_name)
    list_original_files.sort()
    return list_original_files


# Generates the list of file names without extension from the Selected folder,
# and sorts in an alphanumeric/ascending order.

def get_selected_file_list():
    list_selected_files = []
    selected_files = os.listdir(SELECTED_FILES_PATH)
    for file in selected_files:
        file_extension = pathlib.Path(file).suffix
        if file_extension == SELECTED_FILE_EXTENSION:
            selected_file_name = pathlib.Path(file).stem
            list_selected_files.append(selected_file_name)
    list_selected_files.sort()
    return list_selected_files


# Compares original and selected lists of files and returns the difference
# between them (file names from the Original folder that missing in the Selected folder).

def get_difference(original_files_list, selected_file_list):
    non_match_file_name_list = set(original_files_list) - set(selected_file_list)
    return non_match_file_name_list


# Moves files listed in the non_match_file_name_list from the Original folder to the Backup folder.

def move_files_to_backup(non_match_file_name_list):
    for file in non_match_file_name_list:
        original_file = ORIGINAL_FILES_PATH + str("/") + file + ORIGINAL_FILE_EXTENSION
        backup_file = BACKUP_FILES_PATH + str("/") + file + ORIGINAL_FILE_EXTENSION
        shutil.move(original_file, backup_file)


if __name__ == '__main__':
    main()
