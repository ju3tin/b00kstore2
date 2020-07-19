#!/usr/local/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)
tasks = []


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append({'title': task['title'], 'description': task['description'], 'id': task['id']})
    return jsonify({'tasks': task_list})


@app.route('/api/create-task', methods=['GET'])
def create_task():
    new_task = {"id": len(tasks), "title": "Learn Heroku", "description": "Start with Flask ", "done": False}
    tasks.append(new_task)
    for task in tasks:
        task_list.append({'title': task['title'], 'description': task['description'], 'id': task['id']})
    return jsonify({'tasks': task_list})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        task = tasks[task_id]
    except:
        return jsonify({"text": "Error, task not found"})
    return jsonify({'title': task['title'], 'description': task['description'], 'id': task['id']})


@app.route('/', methods=['GET'])
def home():
    return jsonify({'msg': 'This is the Home'})


@app.route('/test', methods=['GET'])
def test():
    return jsonify({'msg': 'This is a Test'})


if __name__ == '__main__':
    app.run(debug=True)
