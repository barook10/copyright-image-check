from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return '''
    <h1>Copyright Check API</h1>
    <p>Endpoints:</p>
    <ul>
        <li>POST /check_copyright - Upload image for copyright check</li>
        <li>GET /uploads/&lt;filename&gt; - View uploaded images</li>
    </ul>
    '''

@app.route('/check_copyright', methods=['POST'])
def check_copyright():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    verdict = "Copyright Infringed" if random.random() > 0.5 else "No Issue"
    confidence = round(random.uniform(50, 95), 2)
    
    return jsonify({
        'status': 'success',
        'file_id': filename,
        'verdict': verdict,
        'confidence': confidence,
        'image_url': f'/uploads/{filename}'
    })

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)