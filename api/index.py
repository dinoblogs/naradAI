from bardapi import Bard
import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.secret_key = "krishna4704"
#Replace XXXX with the values you get from __Secure-1PSID 
os.environ['_BARD_API_KEY']="YAizMjUJbnOoezZf0MrT-yZ9qzT9IzFseBQXgea8KQ6h06bNWMJ7OVaEPZgWKfXLS7pvDA."

__title__ = 'Narad AI'
# # set your input text
# input_text = "Hi"

# while input_text != 'bye':
#     print(f"Chat GPT: {Bard().get_answer(input_text)['content']}")
#     input_text = input("Me: ")
    
@app.route('/')
def home():
    return redirect('/')
@app.route('/api', methods = ['POST'])
def api():
    if request.method == 'POST':
        msg = request.form['msg']
        data = Bard().get_answer(msg)['content']
        data = data.replace('bard', 'Narad')
        data = data.replace('Bard', 'Narad')
        data = data.replace('Google', 'Krishna Sharma')
        data = data.replace('google', 'Krishna Sharma')
        # data = "{'msg':' " + data + " '}"
        # return data
        return data
        
    else:
        return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
