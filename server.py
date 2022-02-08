from datetime import datetime
from random import randint
from flask import Flask,render_template,session,redirect,request
app = Flask(__name__)
app.secret_key = 'lamelo ball'
arr = []
@app.route('/')
def index():
    return render_template('index.html', arr = arr)
@app.route('/process_money', methods=['POST', 'GET'])
def money():
    farm_num = randint(10,20)
    cave_num = randint(5,10)
    house_num = randint(2,5)
    casino_num= randint(-50,50)
    today = datetime.now()
    if request.form['gold'] == 'cave' and 'gold' in session:
        session['gold'] += cave_num
        arr.append(f'Earned {cave_num} from the cave! {today}')
    elif request.form['gold'] == 'farm' and 'gold' in session:
        session['gold'] += farm_num
        arr.append(f'Earned {farm_num} from the farm! {today}')
    elif request.form['gold'] == 'house'and 'gold' in session:
        session['gold'] += house_num
        arr.append(f'Earned {house_num} from the house! {today}')
    elif request.form['gold'] == 'casino'and 'gold' in session:
        session['gold'] += casino_num
        if casino_num > 0:
            arr.append(f'Earned {casino_num} from the casino! {today}')
        else:
            arr.append(f'Entered a casino and lost {casino_num} gold! {today}')
    else:
        session['gold'] = farm_num + cave_num + house_num + casino_num
        arr.append(f'Oh look it here I have money now! {today}')
    return redirect('/')
if __name__ =="__main__":
    app.run(debug=True)