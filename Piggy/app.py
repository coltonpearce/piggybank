from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity
savings = {
    "goal": 0.0,
    "current": 0.0
}

@app.route('/')
def index():
    percentage_filled = 0
    if savings["goal"] > 0:
        percentage_filled = (savings["current"] / savings["goal"]) * 100
    return render_template('index.html', savings=savings, percentage_filled=percentage_filled)

@app.route('/set_goal', methods=['POST'])
def set_goal():
    try:
        goal = float(request.form['goal'])
        savings["goal"] = goal
        savings["current"] = 0.0
    except ValueError:
        pass
    return redirect(url_for('index'))

@app.route('/add_money', methods=['POST'])
def add_money():
    try:
        amount = float(request.form['amount'])
        savings["current"] += amount
        if savings["current"] > savings["goal"]:
            savings["current"] = savings["goal"]
    except ValueError:
        pass
    return redirect(url_for('index'))

@app.route('/remove_money', methods=['POST'])
def remove_money():
    try:
        amount = float(request.form['amount'])
        savings["current"] -= amount
        if savings["current"] < 0:
            savings["current"] = 0.0
    except ValueError:
        pass
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
