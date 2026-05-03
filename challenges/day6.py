import datetime

entry = input("what did you learned today?  ").strip()
rating = input("Please rat your productivity for today  ").strip()

now = datetime.datetime.now()
date_str  = now.strftime("%Y-%m-%d - %I:%M %p")

journal_entry = f"\n 📅 {date_str}\n{entry}"
if rating:
    journal_entry += f"\n Procutivityrating is {rating}/5 ⭐️"
journal_entry += "\n" + "-" * 50

with open("Learning journal.txt", "a", encoding="utf_8") as f: # a - append mode
    f.write(journal_entry)