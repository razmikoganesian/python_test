import os
import shutil
from watchdog.events import (
    DirCreatedEvent,
    FileCreatedEvent,
    FileSystemEventHandler,
)
from watchdog.observers import Observer

WATCH_FOLDER = os.path.expanduser("~/Downloads")
FILE_DESTINATION = {".pdf": "PDFs", ".jpg": "images", ".png": "pngs"}


class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event: DirCreatedEvent | FileCreatedEvent) -> None:
        if event.is_directory:
            return

        file_path = event.src_path
        extension = os.path.splitext(file_path[1].lower())
        dest_folder = FILE_DESTINATION.get(extension, "Others")
        full_destinantion = os.path.join(WATCH_FOLDER, dest_folder)
        os.makedirs(full_destinantion, exist_ok=True)
        move_to_destinantion = os.path.join(
            full_destinantion, os.path.basename(file_path)
        )

        try:
            shutil.move(file_path, move_to_destinantion)
            print("Moved")
        except:
            print("Failed to move")


if __name__ == "__main__":
    print(f"Watching folder {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=False)
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
