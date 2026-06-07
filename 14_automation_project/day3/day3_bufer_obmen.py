import time
import pyperclip

TARGET = "B21234567890"
TARGET1 = "MYCODE"

POLL_INTERVAL = 0.3  # секунды между проверками
last_seen = None


def main():
    global last_seen
    print("Clipboard monitor started", flush=True)

    while True:
        try:
            text = pyperclip.paste()
        except pyperclip.PyperclipException:
            time.sleep(POLL_INTERVAL)
            continue

        if not isinstance(text, str):
            time.sleep(POLL_INTERVAL)
            continue

        # не реагировать на тот же текст снова
        if text == last_seen:
            time.sleep(POLL_INTERVAL)
            continue

        if len(text) == 12 and text.startswith("A1"):
            pyperclip.copy(TARGET)
            last_seen = TARGET
            print(f"Replaced A1* -> {TARGET}", flush=True)

        elif len(text) == 6 and text.startswith("BB"):
            pyperclip.copy(TARGET1)
            last_seen = TARGET1
            print(f"Replaced BB* -> {TARGET1}", flush=True)

        else:
            last_seen = text

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
