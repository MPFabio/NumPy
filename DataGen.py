from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate_data():
    params = request.json
    data_type = params.get('type', 'physical')
    if data_type == 'physical':
        # Simule des données physiques
        data = np.random.random(100)
    elif data_type == 'climate':
        # Simule des données climatiques
        data = np.random.random(100)
    else:
        # Simule des données biologiques
        data = np.random.random(100)
    return jsonify(data.tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
