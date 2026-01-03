from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = pd.read_json("data/processed/output.json")
    anomalies = df[df["is_anomaly"] == True]
    return render_template("dashboard.html", anomalies=anomalies.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
