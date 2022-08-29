from flask import Flask, render_template, redirect
from readfile import ReadFile
from writefile import WriteFile

app = Flask(__name__)

filename = "task.txt"

@app.route('/', methods=['GET'])
def index():
    tasks = ReadFile()
    file_contents = tasks.read_file(filename)

    return render_template('index.html', tasks = file_contents)


@app.route('/submit', methods=['POST'])
def submit():
    save = WriteFile()
    save.write_file(filename)

    return redirect('/')


@app.route('/clear')
def clear():
    open(filename, 'w').close()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)