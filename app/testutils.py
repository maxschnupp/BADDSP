import re
import os
def file_in_folder_matches_regex(folder_path, regex):
        pattern = re.compile(regex)
        for filepath in os.listdir(folder_path):
            print(filepath)
            return pattern.match(filepath)