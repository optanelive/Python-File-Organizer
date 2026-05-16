import os
import shutil

# 1. Define the correct directory path
TRACKED_DIR = os.path.expanduser("~/Downloads")

EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
}

def clean_folder():
    # 2. Ensure the destination folders exist
    for folder in EXTENSION_MAP.keys():
        folder_path = os.path.join(TRACKED_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

    # 3. Scan and move the files
    for filename in os.listdir(TRACKED_DIR):
        file_path = os.path.join(TRACKED_DIR, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find the correct folder and move the file
        for folder, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                dest_path = os.path.join(TRACKED_DIR, folder, filename)
                print(f"Moving: {filename} --> {folder}/")
                shutil.move(file_path, dest_path)
                break

if __name__ == "__main__":
    print("🧹 Starting folder cleanup...")
    clean_folder()
    print("✨ Folder cleanup completed.")
