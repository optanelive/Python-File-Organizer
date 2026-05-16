# 🧹 Simple Python File Organizer

An automated script to clean up your messy directories (like your Downloads or Desktop folders) instantly. It scans a target folder, identifies files by their extensions, and routes them into structured subdirectories (Images, Documents, Videos, etc.) using Python's built-in `os` and `shutil` libraries.

## 📺 Watch the Tutorial

I built and explained this script step-by-step in a quick video. If you want to see how it works visually or want to build it yourself from scratch, check it out here:

👉 **[Watch the YouTube Video Tutorial Here](https://youtu.be/7uWK6N-m_Gc?si=TszDcb6Pmhulp2nA)**

---

## ⚙️ How It Works

1. **Scans the Target Folder:** Looks at all the files in the directory you specify.
2. **Checks Extensions:** Reads the file type (e.g., `.pdf`, `.png`) while safely ignoring existing subfolders.
3. **Automated Routing:** Groups files into designated folders based on an extension map.

## 🚀 How to Run It

1. Clone this repository or download the `file_organizer.py` file.
2. Open the script and modify the `TRACKED_DIR` path to point to the folder you want to clean up:
   ```python
   TRACKED_DIR = r"C:\Users\YourName\Downloads"
