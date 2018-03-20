from flask import Flask, request, render_template
import random
from flask_wtf import FlaskForm
from wtforms import BooleanField

class MyForm(FlaskForm):
    creature = BooleanField()



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/roll/", methods=['POST'])
def roll():
    # for rollsMade in range(0, diceToRoll):
    #     print('rolling again')
    value = random.randint(1, 6)
    print(text_box_value)
    return render_template('home.html', value=value);

@app.route("/string/", methods=['GET', 'POST']) # part A
def get_critters():
    form = MyForm() # part B
    if form.validate_on_submit():
        print(yoo)
        # do something with form.creature, or form.whatever
        return render_template("home.html", form=form) # part C

if __name__ == '__main__':
    app.run(debug=True)
