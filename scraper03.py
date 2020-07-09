from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

match = html.find('#footer', first=True)
print(match.text)


#Output Footer Information