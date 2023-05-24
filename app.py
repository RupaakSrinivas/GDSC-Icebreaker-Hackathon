from flask import Flask, request, render_template
from aiapi import get_message
import asyncio


app=Flask(__name__)

async def send_message(personality, query):
    try:
        response = get_message(personality, query)
        print(personality)
        return render_template('index1.html', message=response, person=personality)
    except Exception as e:
        print(e)

#declaring inputs

personality = ""
#defining routes

@app.route('/')
def front():
    return render_template('front_page.html')

@app.route('/feeling')
def feeling():
    return render_template('feeling.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

# def post(output):
#     message = output
#     return render_template('index.html', message=message)

@app.route('/submit_personality', methods=['POST'])
def submit_personality():
    global personality
    personality = request.form.get('personality')
    print(personality)
    return render_template('index1.html', person=personality)

@app.route('/submit_advanced', methods=['POST'])
async def submit_advanced():
    query = 

@app.route('/submit', methods =['POST'])
async def submit():
    global personality
    query = request.form.get('dish')
    reply = await send_message(personality, query)
    return str(reply)

if __name__ == '__main__':
    asyncio.run(app.run(debug="True"))
