from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    with open("task.txt","r") as f:
        tasks_file_contents = f.read().strip()
        tasks_list = tasks_file_contents.split('\n')
        tasks_mother_list = []

        for task in tasks_list:
            task_item_list = task.split(', ')
            tasks_mother_list.append(task_item_list)
        print(tasks_mother_list)

    return render_template('index.html', tasks = tasks_mother_list)


@app.route('/submit', methods=['POST'])
def submit():

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    with open('task.txt', 'a') as f:
        f.write(str(task + ", " + email + ", " + priority + "\n"))

    return redirect('/')


@app.route('/clear')
def clear():
    open('task.txt', 'w').close()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)