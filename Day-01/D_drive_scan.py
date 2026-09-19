import os


def get_folder_size(folder_path):
    total_size = 0

    # Folder ke andar recursively har folder/file par jayega
    for root, folders, files in os.walk(folder_path):

        # Current folder ki har file check karo
        for file in files:

            # File ka complete path banao
            file_path = os.path.join(root, file)

            try:
                # File ka size bytes mein nikalo
                file_size = os.path.getsize(file_path)

                # Total mein add karo
                total_size = total_size + file_size

            except (PermissionError, FileNotFoundError):
                # Agar kisi file ka access nahi mila to skip karo
                pass

    return total_size


def bytes_to_gb(size):
    # Bytes ko GB mein convert karo
    return size / (1024 ** 3)


drive_path = "D:\\"

results = []

print("Scanning D: drive...")
print("This may take some time.\n")


# D:\ ke andar jo items hain unko check karo
for item in os.listdir(drive_path):

    # Example:
    # item = "Movies"
    # folder_path = "D:\\Movies"
    folder_path = os.path.join(drive_path, item)

    # Sirf folders scan karne hain
    if os.path.isdir(folder_path):

        print(f"Scanning: {item}")

        # Folder ka complete size calculate karo
        size = get_folder_size(folder_path)

        # Folder name aur size list mein save karo
        results.append((item, size))


# Sabse bade folder ko pehle dikhane ke liye sorting
results.sort(key=lambda x: x[1], reverse=True)


print("\n========== D DRIVE SPACE REPORT ==========\n")

for folder_name, size in results:

    size_gb = bytes_to_gb(size)

    print(f"{folder_name:<40} {size_gb:>10.2f} GB")