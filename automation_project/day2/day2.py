import os


def batch_rename(folder, base_name, extension):
    files = [
        file for file in os.listdir(folder) if file.lower().endswith(extension.lower())
    ]

    if not files:
        print("No such files in directory")
        return

    for index, file in enumerate(files):
        new_name = f"{base_name}_{index}{extension}"
        print(f"{file} => {new_name}")

    confirm = input('Press "y" to confirm or (n) to reject').strip().lower()
    if confirm != "y":
        print("Cancelled!")
        return

    for index, file in enumerate(files, start=1):
        src = os.path.join(folder, file)
        new_name = f"{base_name}_{index}{extension}"
        destination = os.path.join(folder, new_name)
        os.rename(src, destination)
    print(f"Renamed {len(files)} successfully")


if __name__ == "__main__":
    folder = (
        input("Enter folder path or leave blank for current folder:  ").strip()
        or os.getcwd()
    )

    if not os.path.isdir(folder):
        print("Invalid folder")

    else:
        base_name = input("Entre base name for files:  ").strip()
        extension = input("Entre extension name for files:  ").strip()

        batch_rename(folder, base_name, extension)
