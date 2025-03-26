from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# List to store tasks
tasks = []

# Route to display tasks
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

# Route to add a task
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")  # Get the task from the form
    if task:
        tasks.append({"id": len(tasks) + 1, "name": task})  # Add task with an ID
    return redirect(url_for("index"))

# Route to delete a task
@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]  # Remove task by ID
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
