##Import OS module ---------------------------------------------------------------------------------

import os

folders_to_monitor = [
    r"D:\Oracle",
    r"D:\Project",
    r"D:\Study Pack",
    r"D:\TOOLS-SOFTWARES"   
]

##Define a function to get the size of a folder in bytes -------------------------------------------

def get_folder_size(folder_path):
    total_size = 0

    for root, folders, files in os.walk(folder_path):

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size
    
    return total_size

##Define a function to convert size(bytes) in human readable format = GB ----------------------------

def bytes_to_gb(size):
    return size/(1024**3)

#loop through the list of folders and get their size in GB ------------------------------------------ 

for folder in folders_to_monitor:
    size_bytes = get_folder_size(folder)
    size_gb = bytes_to_gb(size_bytes)

    print(f"{folder} : {size_gb: .2f} GB")