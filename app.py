from flask import Flask, render_template, request
from stock_invest_advisor.crew import StockInvestAdvisor
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    company = request.form["company"]
    result = StockInvestAdvisor().crew().kickoff(inputs={"company_name": company})
    return render_template("result.html", company=company, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


