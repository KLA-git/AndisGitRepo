### Login Reqeust & co
#### Inspector copy cUrl --> https://curl.trillworks.com/
###### https://www.youtube.com/watch?v=ylSc5NLjmM0

```python

import requests
from bs4 import BeautifulSoup
 
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://awesome-flask-blog-app.herokuapp.com',
    'Connection': 'keep-alive',
    'Referer': 'https://awesome-flask-blog-app.herokuapp.com/auth/login/',
    'Upgrade-Insecure-Requests': '1',
}
 
data = {
    'csrf_token': '',
    'email': 'mexal98748@donmah.com',
    'password': 'password',
    'remember_me': 'y',
    'submit': 'Log In'
}
 
post_data = {
    'csrf_token': '',
    'title': 'This post has been created by python script!',
    'short_description': 'THIS is a demo post',
    'post': '<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>',
    'submit': 'Post'
}
 
with requests.Session() as s:
    login_url = 'https://awesome-flask-blog-app.herokuapp.com/auth/login/'
    r = s.get(login_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.find(id="csrf_token")['value']
    data['csrf_token'] = csrf_token
 
    s.post(login_url, data=data, headers=headers)
    
    ```
