from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista zadań
tasks = []

# Wczytaj zadania z pliku
def load_tasks(file_name="zadania.txt"):
    try:
        with open(file_name, "r") as file:
            for line in file:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "done": status == "DONE"})
    except FileNotFoundError:
        pass  # Plik nie istnieje, zaczynamy od pustej listy

# Zapisz zadania do pliku
def save_tasks(file_name="zadania.txt"):
    with open(file_name, "w") as file:
        for task in tasks:
            status = "DONE" if task["done"] else "TODO"
            file.write(f"{task['task']} | {status}\n")

# Główna strona z listą zadań
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

# Dodaj nowe zadanie
@app.route("/add", methods=["POST"])
def add_task():
    new_task = request.form.get("task")
    if new_task:
        tasks.append({"task": new_task, "done": False})
        save_tasks()
    return redirect("/")

# Oznacz zadanie jako ukończone
@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
        save_tasks()
    return redirect("/")

# Usuń zadanie
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks()
    return redirect("/")

# Uruchomienie aplikacji
if __name__ == "__main__":
    load_tasks()
app.run(host='0.0.0.0', port=5000, debug=True)
