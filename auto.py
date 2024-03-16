import os
import subprocess
import time

def open_folder_in_explorer(folder_path):
    # Open folder in File Explorer
    subprocess.Popen(f'explorer "{folder_path}"')

# Change folder path to desired path
folder_path = r'C:\folder_path'
open_folder_in_explorer(folder_path)

