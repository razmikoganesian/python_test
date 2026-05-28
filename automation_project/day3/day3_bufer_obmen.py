import time
import pyperclip

TARGET = "B21234567890"
TARGET1 = "MYCODE"

while True:
    text = pyperclip.paste()

    if isinstance(text, str) and len(text) == 12 and text.startswith("A1"):
        pyperclip.copy(TARGET)

    elif isinstance(text, str) and len(text) == 6 and text.startswith("BB"):
        pyperclip.copy(TARGET1)

    time.sleep(0.2)
