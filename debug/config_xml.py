from BeautifulSoup import BeautifulSoup

file_name='config.xml'
with open(file_name) as f:
    content=f.read()

y=BeautifulSoup(content)
print y.host.contents[0]

for tag in y.other.preprocessing_queue:
    print tag
