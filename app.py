from flask import Flask, request, render_template
from aiapi import get_message
import asyncio


app=Flask(__name__)

async def send_message(personality, query):
    try:
        response = get_message(personality, query)
        print("response : ",response)
        return response
    except Exception as e:
        print(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods =['POST'])
async def submit():
    personality = request.form.get('personality')
    query = request.form.get('dish')
    reply = await send_message(personality, query)
    return str(reply)

if __name__ == '__main__':
    asyncio.run(app.run(debug="True"))
