import os
from flask_cors import CORS, cross_origin

import openai

import requests
from bs4 import BeautifulSoup

api = ""
# Make a GET request to the website
url = 'https://talkai.info/chat/'

import os
from flask import Flask, render_template, redirect, request


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = "krishna4704"
#Replace XXXX with the values you get from __Secure-1PSID 
# os.environ['_BARD_API_KEY']="YAhFIXuWe-TopFGMi-R3sCrDuE850kV09CECqWx-b3ZDzKN48dz_YpXdSe1Hy2ZnQibwiQ."
# token = environ.get("BARD_TOKEN")

# chatbot = Chatbot("YAhFIXuWe-TopFGMi-R3sCrDuE850kV09CECqWx-b3ZDzKN48dz_YpXdSe1Hy2ZnQibwiQ.")


__title__ = 'Narad AI'

def chk():
    global api
    response = requests.get(url)
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with the attribute data-api-key
    elements = soup.find_all(attrs={'data-api-key': True})

    # Extract the values of data-api-key attribute
    api_keys = [element['data-api-key'] for element in elements]

    # Print the extracted API keys
    for api_key in api_keys:
        api = api_key   

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/image/')
def image():
    chk()

    return render_template('chat1.html')
@app.route('/chat/')
def chat():
    chk()


    return render_template('chat2.html')


@app.route('/anim')
def anim():
    return render_template('anim.html')
@app.route('/api', methods = ['POST','GET'])
def api():
    chk()
    if request.method == 'POST':
        try:
            msg = request.form['msg']
            message = msg
            if api != "":
                openai.api_key = api
                messages = [ {"role": "system", "content": "You are a GPT4 intelligent assistant."} ]
                if message:
                    messages.append(
                        {"role": "user", "content": message},
                    )
                    chat = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo", messages=messages
                    )
                
                data = chat.choices[0].message.content
                messages.append({"role": "assistant", "content": data})

            # data = chatbot.ask(msg)
            # data1 = data['content']
            data1 = data
            # data = Bard().get_answer(msg)['content']

            data1 = data1.replace('developed by OpenAI called GPT-4.', 'developed by Krishna Sharma called NaradAI.')
            m = 0
            while True:
                try:
                    img_tag = f"<img src='{data['images'][m]}' style='height: 155px; width:auto;'>"
                    area = int(data1.find('['))
                    area2 = int(data1.find(']'))
                    data1 = data1.replace(data1[area:area2+1], img_tag)
                    m = m + 1
                except:
                    break


            real_data = data1
            print(real_data)
            # data = "{'msg':' " + data + " '}"
            return real_data
        except:
            return "<span class='error'>Oops! Something went wrong while retrieving the response. Please try again.M </span>"
        
    else:
        return redirect('/')
    

@app.route('/img', methods = ['POST','GET'])
def img():
    chk()
    if request.method == 'POST':
        try:
            msg = request.form['msgs']
            openai.api_key = api

            response = openai.Image.create(
                prompt=msg,
                n=1,
                size="1024x1024",
            )

            image_url = response["data"][0]["url"]
            # print(image_url)
            # data = chatbot.ask(msg)
            # data1 = data['content']
            print(image_url)
            data1 = f"<img src='{image_url}' style='height: 355px; width:auto;'>"

            # data1 = data1.replace('developed by OpenAI called GPT-4.', 'developed by Krishna Sharma called NaradAI.')
            # m = 0
            # while True:
            #     try:
            #         img_tag = f"<img src='{data['images'][m]}' style='height: 155px; width:auto;'>"
            #         area = int(data1.find('['))
            #         area2 = int(data1.find(']'))
            #         data1 = data1.replace(data1[area:area2+1], img_tag)
            #         m = m + 1
            #     except:
            #         break


            real_data = data1
            return real_data
        except:
            return "<span class='error'>Oops! Something went wrong while retrieving the response. Please try again.M </span>"
        
    else:
        return redirect('/')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
