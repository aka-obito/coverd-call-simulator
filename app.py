from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    stock_price = float(request.form['stock_price'])
    strike_price = float(request.form['strike_price'])
    premium = float(request.form['premium'])
    shares = int(request.form['shares'])
    expiration = request.form['expiration']

    # Simulation logic
    result = covered_call_simulation(stock_price, strike_price, premium, shares)

    return render_template('results.html', result=result)

def covered_call_simulation(stock_price, strike_price, premium, shares):
    potential_gain = (strike_price - stock_price) * shares + premium * shares
    max_profit = min(potential_gain, (premium * shares))

    if stock_price >= strike_price:
        return f"You earned {max_profit} by selling your stock and keeping the premium."
    else:
        return f"You kept your stock and earned {premium * shares} from the premium."

if __name__ == '__main__':
    app.run(debug=True)
