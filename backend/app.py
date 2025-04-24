from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Audio Transcription API is running"})

@app.route('/api/transcribe', methods=['POST'])
def transcribe_audio():
    # Here we will implement the transcription logic
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    return jsonify({
        "message": "Audio received",
        "status": "processing"
    })

@app.route('/api/transcriptions', methods=['GET'])
def get_transcriptions():
    # Here we will implement the retrieval of transcription history
    return jsonify({
        "transcriptions": []
    })

if __name__ == '__main__':
    app.run(debug=True)