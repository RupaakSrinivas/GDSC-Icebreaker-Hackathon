from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods =['POST'])
def submit():
    personality = request.form.get('personality')
    query = request.form.get('dish')

    print(personality)
    print(query)

    return 'Form submitted successfully'

if __name__ == '__main__':
    app.run()