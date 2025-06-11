from flask import Flask, render_template, jsonify, request
from fake_store_analyzer import main_analyzer
import threading
import time

app = Flask(__name__)

latest_results = None
interval_minutes = 0.5  # by default 0.5 minutes
service_thread = None
running = True  # Start running

def analyzer_task():
    global latest_results, running
    while running:
        # Replace with your actual analyzer call
        latest_results = main_analyzer()
        time.sleep(interval_minutes * 60)

@app.route('/results')
def results():
    return jsonify({'results': latest_results})

@app.route('/stop', methods=['POST'])
def stop():
    global running
    running = False
    return jsonify({'status': 'stopped'})

@app.route('/start', methods=['POST'])
def start():
    analyzer_task()
    return jsonify({'status': 'started'})

@app.route('/set_interval', methods=['POST'])
def set_interval():
    global interval_minutes
    data = request.json
    interval_minutes = float(data.get('interval', 0.5))
    return jsonify({'interval': interval_minutes})

if __name__ == "__main__": 
    app.run(debug=True)