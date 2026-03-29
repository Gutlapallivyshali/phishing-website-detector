from flask import Flask, request, render_template
import pickle

# Load your model and vectorizer
model = pickle.load(open('phishing_mnb.pkl', 'rb'))  # or phishing.pkl if you want
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    data = vectorizer.transform([url])
    prediction = model.predict(data)[0]
    result = "⚠️ Phishing Website" if prediction == 1 else "✅ Safe Website"
    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)