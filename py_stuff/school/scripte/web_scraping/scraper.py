from requests_html import HTMLSession
from config import data, headers
import pprint

url = 'https://neilo.webuntis.com/WebUntis/?school=fvsg-fulda#/basic/login'

session = HTMLSession()

r = session.get(url)
r.html.render(sleep=2, keep_page=True, scrolldown=1)

input_username = r.html.xpath('//input')[0]
input_pw = r.html.xpath('//input')[1]

params = (
    ('type', '2'),
    ('date', '2018-03-31'),
    ('isMyTimetableSelected', 'true'),
)

r = session.post('https://neilo.webuntis.com/WebUntis/j_spring_security_check', data=data)
r= session.get('https://neilo.webuntis.com/WebUntis/api/public/timetable/weekly/pageconfig?', params=params)
r.html.render(sleep=2, keep_page=True, scrolldown=1)

data = r.json()
storage_data=data['data']['elements']

lehrer_dict={} ##result Dict

for item in storage_data:
    lehrer_dict[item["name"]] = {
        'vorname': item['forename'],
        'nachname': item['longName'],
    }

pprint.pprint(lehrer_dict["WIE"])

session.close()