<h1>🌸 Iris Flower Prediction API</h1>

<p>
A <strong>Machine Learning REST API</strong> built with
<strong>FastAPI</strong> and <strong>Scikit-learn</strong> to predict
the species of an Iris flower using a
<strong>Decision Tree Classifier</strong>.
</p>

<hr />

<h2>🚀 Features</h2>
<ul>
  <li>FastAPI backend</li>
  <li>Decision Tree ML model</li>
  <li>Iris dataset (Seaborn)</li>
  <li>REST API (JSON)</li>
  <li>Swagger UI documentation</li>
  <li>Confusion matrix endpoint</li>
</ul>

<hr />

<h2>🧠 Machine Learning Model</h2>
<ul>
  <li><strong>Algorithm:</strong> Decision Tree Classifier</li>
  <li><strong>Dataset:</strong> Iris Dataset</li>
  <li><strong>Features:</strong>
    <ul>
      <li>Sepal Length</li>
      <li>Sepal Width</li>
      <li>Petal Length</li>
      <li>Petal Width</li>
    </ul>
  </li>
  <li><strong>Target:</strong> Species (setosa, versicolor, virginica)</li>
</ul>

<hr />

<h2>📁 Project Structure</h2>
<pre>
project/
 ├── main.py
 ├── model.py
 ├── requirements.txt
 └── README.md
</pre>

<hr />

<h2>⚙️ Installation & Setup</h2>

<h3>1️⃣ Clone the repository</h3>
<pre>
git clone https://github.com/your-username/iris-fastapi-ml.git
cd iris-fastapi-ml
</pre>

<h3>2️⃣ Create virtual environment (recommended)</h3>
<pre>
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
</pre>

<h3>3️⃣ Install dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<hr />

<h2>▶️ Run the Application</h2>
<pre>
uvicorn main:app --reload
</pre>

<p>
App will run at:
<br />
<code>http://127.0.0.1:8000</code>
</p>

<hr />

<h2>📖 API Documentation</h2>
<p>
Swagger UI:
<br />
<code>http://127.0.0.1:8000/docs</code>
</p>

<hr />

<h2>🔮 Prediction API</h2>

<h3>POST /predict</h3>

<h4>Request Body</h4>
<pre>
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
</pre>

<h4>Response</h4>
<pre>
{
  "species": "setosa"
}
</pre>

<hr />

<h2>📊 Confusion Matrix</h2>

<h3>GET /confusion-matrix</h3>

<pre>
{
  "confusion_matrix": [
    [50, 0, 0],
    [0, 47, 3],
    [0, 1, 49]
  ]
}
</pre>

<hr />

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>Uvicorn</li>
  <li>Scikit-learn</li>
  <li>Pandas</li>
  <li>Seaborn</li>
</ul>

<hr />

<h2>📌 Future Improvements</h2>
<ul>
  <li>Save & load trained model (pickle/joblib)</li>
  <li>Docker support</li>
  <li>Cloud deployment</li>
  <li>Authentication & rate limiting</li>
</ul>

<hr />

<h2>👤 Author</h2>
<p>
<strong>Sajib Saha</strong><br />
GitHub:
<a href="https://github.com/your-username">
https://github.com/SajibSaha3
</a>
</p>

<hr />

<h2>📜 License</h2>
<p>
This project is licensed under the <strong>MIT License</strong>.
</p>
