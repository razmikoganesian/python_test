import os
import shutil

EXTENSION_MAP = {
    "PDFs": [".pdf"],
    "IMAGEs": [".png", ".jpg", ".jpeg", ".gif"],
    "DOCs": [".txt"],
}


def get_destination_folder(file_name):
    extension = os.path.splitext(file_name)[1].lower()

    for folder, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return folder

    return "Others"


def sort_files(folder_path):

    script_dir = os.path.dirname(os.path.abspath(__file__))

    for file in os.listdir(folder_path):

        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):

            dest_folder = get_destination_folder(file)

            dest_path = os.path.join(script_dir, dest_folder)

            os.makedirs(dest_path, exist_ok=True)

            shutil.move(full_path, os.path.join(dest_path, file))

            print(f"Moved: {file} -> {dest_folder}/")


if __name__ == "__main__":

    folder = input("Enter folder path: ").strip()

    if not folder:

        script_dir = os.path.dirname(os.path.abspath(__file__))

        # уровень выше
        project_root = os.path.dirname(script_dir)

        folder = os.path.join(project_root, "different_files")

    print("Using folder:", folder)

    if not os.path.isdir(folder):
        print("Invalid directory!")
    else:
        sort_files(folder)
        print("Sorting is finished")
