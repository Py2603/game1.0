from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initial balance
balance = 1000

@app.route('/')
def home():
    return render_template('index.html', balance=balance)

@app.route('/bet', methods=['POST'])
def bet():
    global balance
    data = request.json
    choice = data['choice']
    bet = int(data['bet'])
    guess = data.get('guess')

    if bet > balance or bet <= 0:
        return jsonify({'error': 'Invalid bet amount!'})

    if choice == 'coin_flip':
        result = random.choice(['heads', 'tails'])
        if guess.lower() == result:
            balance += bet * 2
            return jsonify({'result': result, 'balance': balance, 'message': f'✅ You won ${bet * 2}!'})
        else:
            balance -= bet
            return jsonify({'result': result, 'balance': balance, 'message': f'❌ You lost ${bet}.'})

    elif choice == 'dice_roll':
        result = random.randint(1, 6)
        if int(guess) == result:
            balance += bet * 6
            return jsonify({'result': result, 'balance': balance, 'message': f'✅ You won ${bet * 6}!'})
        else:
            balance -= bet
            return jsonify({'result': result, 'balance': balance, 'message': f'❌ You lost ${bet}.'})

    return jsonify({'error': 'Invalid choice!'})

if __name__ == '__main__':
    app.run(debug=True)
