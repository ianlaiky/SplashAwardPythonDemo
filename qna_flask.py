# pip install flask if not installed
# don't name your file as flask.py !
from flask import Flask,redirect,url_for,request,render_template
from bs4 import BeautifulSoup as bs
import requests

# create a Flask object
app = Flask(__name__)

# function to access website to get the answer given the quesiton
def response(question):    
    
    try:
      question = "_".join(question.split())  
      url = 'http://www.answers.com/Q/' + question
      response = requests.get(url)
      soup = bs(response.text, 'html.parser')    
      ans = soup.find('div', {'class' : 'answer_text'}).text.strip().replace('\n', " ").replace('/', " ")
    except:
      ans = "I don't know. Please ask another question."
    
    return ans

# load the question webpage
@app.route('/')
def load_webpage():
    return render_template('qna.html')  

# get the answer
@app.route('/question', methods = ['POST'])
def question():    
    if request.method == 'POST':
        question=request.form['ques']
        reply = response(question)
        return redirect(url_for('ans',  answer = reply))

# display the answer 
@app.route('/ans/<answer>')
def ans(answer):
    return ('Answer : %s' % answer)

# run the app
if __name__ == '__main__':
    app.run(debug = True)