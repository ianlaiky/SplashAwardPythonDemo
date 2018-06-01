
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup as bs
import requests


# In[2]:

question = input("Ask me anything : ")


# In[3]:

# format question to be input to url

question = question.split()
print(question)



# In[4]:

question = "_".join(question)
print(question)



# In[5]:

url = 'http://www.answers.com/Q/' + question


# In[6]:

# get the response page
response = requests.get(url)


# In[7]:

content = response.text
print(content)



# In[8]:

# parse the response page
soup = bs(content,"html.parser")
print(soup.prettify())


# In[9]:

print (soup.prettify())


# In[10]:

# identify and extract the required answer
ans = soup.find('div', {'class' : 'answer_text'})
print(ans)


# In[11]:

# clean the answer
ans = ans.text.strip()
print(ans)



# In[12]:

ans = ans.replace('\n', " ").replace('/', " ")
print(ans)


# ### A knowledgeable chatbot

# In[13]:

# combine above steps into a function
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


# In[ ]:

question = input("Ask me anything : ")


# In[ ]:

while question != "bye":
    reply = response(question)
    print (reply,'\n')
    question = input("Ask me anything : ")
    
print ('goodbye')


# In[ ]:



