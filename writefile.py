from flask import request

class WriteFile:

    def __init__(self):
        self.a = "Hi"

    def write_file(self, filename):

        task = request.form['task']
        email = request.form['email']
        priority = request.form['priority']

        with open(filename, 'a') as f:
            f.write(str(task + ", " + email + ", " + priority + "\n"))