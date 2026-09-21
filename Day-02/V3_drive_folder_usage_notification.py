##Import OS module & Plyer package -----------------------------------------------------------------

import os
from plyer import notification

#List of folders to monitor for size usage ---------------------------------------------------------

folders_to_monitor = [
    r"D:\Oracle",
    r"D:\Project",
    r"D:\Study Pack",
    r"D:\TOOLS-SOFTWARES"   
]

#fixed variable for threshold size in GB ----------------------------------------------------------- 

threshold_gb = 0.5

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

for folder in folders_to_monitor:
    size_bytes = get_folder_size(folder)
    size_gb = bytes_to_gb(size_bytes)

    print(f"{folder} : {size_gb: .2f} GB")

    if size_gb > threshold_gb:
        print(f"{folder} has exceeded the threshold of {threshold_gb} GB. Current size: {size_gb: .2f} GB")

        notification.notify(
            title="Folder Usage Alert",
            message=f"{folder} has reached {size_gb: .2f} GB, exceeding the threshold of {threshold_gb} GB.",
            timeout=10
        )
    else:
        print(f"{folder} is within limit.")
