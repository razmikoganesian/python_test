# NUMERATION!!!!!

menu = ["Green tea", "Lemon tea", "Garlik tea", "Blood tea"]

for i, item in enumerate(menu, start=1):
    print(f"Tea number {i} is : {item}")

def generate_numbered_tasks(tasks: list[str]) -> list[str]:
    numbered_tasks = []
    for index, task in enumerate(tasks, start=1):
        numbered_tasks.append(f"{index}. {task}")
    return numbered_tasks