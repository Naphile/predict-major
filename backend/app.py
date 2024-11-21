from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import data_analysis

app = Flask(__name__, static_folder='../frontend/static', template_folder='../frontend/templates')
CORS(app)

# Endpoint untuk menampilkan form
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint untuk menerima data dan mengembalikan prediksi
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    major = data_analysis.predict_major(data)
    
    # Jika hasilnya "Jurusan Umum", tambahkan rekomendasi berdasarkan minat
    if major == "Jurusan Umum":
        recommended_majors = data_analysis.recommend_major_based_on_interest(data.get('interest', '').lower())
        return jsonify({"major": major, "recommended_majors": recommended_majors})
    
    return jsonify({"major": major})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
