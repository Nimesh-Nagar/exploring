import os
import shutil
import logging

def setup_logging(log_file="file_organizer.log"):
    """Set up logging to a file."""

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def get_category(file_extension):
    """Return the category for a given file extension."""

    categories = {
        "Documents": {".pdf", ".docx", ".txt", ".pptx", ".xls"},
        "Images": {".jpg", ".jpeg", ".png", ".gif", ".svg"},
        "Videos": {".mp4", ".mkv", ".avi", ".mov"},
        "Music": {".mp3", ".wav", ".aac"},
        "Archives": {".zip", ".rar", ".7z", ".tar"},
        "Applications" : {".bin", ".exe", ".bat", ".sh"}
    }
    for category, extensions in categories.items():
        if file_extension in extensions:
            return category
    return "Others"

def ensure_directory(directory):
    """Create the directory if it does not exist."""
    os.makedirs(directory, exist_ok=True)

def move_file(file_path, dest_folder):
    """Move a file to the destination folder, handling duplicates by renaming."""

    filename = os.path.basename(file_path)
    destination = os.path.join(dest_folder, filename)
    
    if os.path.exists(destination):
        base, ext = os.path.splitext(filename)
        count = 1
        while os.path.exists(destination):
            new_filename = f"{base}_{count}{ext}"
            destination = os.path.join(dest_folder, new_filename)
            count += 1
    
    shutil.move(file_path, destination)
    logging.info(f"Moved: {file_path} -> {destination}")

def organize_files(directory):
    """Organize files in the given directory by their type/category."""

    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    # List all files in the directory (ignore subdirectories)
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("No files to organize.")
        return
    
    for file in files:
        file_path = os.path.join(directory, file)
        file_extension = os.path.splitext(file)[-1].lower()
        category = get_category(file_extension)
        category_folder = os.path.join(directory, category)
        
        ensure_directory(category_folder)
        move_file(file_path, category_folder)
    
    print("Files organized successfully.")
    logging.info("File organization completed.")

if __name__ == "__main__":
    setup_logging()
    target_directory = input("Enter the directory to organize: ").strip()
    organize_files(target_directory)
