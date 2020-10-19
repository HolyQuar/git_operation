"""
 -urllib.request for retrieving data from URLs
 -smtplib for sending mail

 --->more msg-learning before knowledge
"""
from urllib.request import urlopen
with urlopen('https://www.hao123.com/') as response:
    print('response:{}'.format(response.readlines()))
    print('----------------------------')
    for line in response:
        # Decoding the binary data to text
        line = line.decode('utf-8')
        if 'Set-Cookie' in line or 'Content' in line:
            # look for Eastern Time
            print('current_line:{}'.format(line))

# smtplib--detail->第五章 Email warning<python 爬虫开发与项目实战>
# send the mail
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()