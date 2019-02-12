import re,requests


LINKS = set()
EMAILS = set()



def func(url, domain=None, step=0):
    if step > 3:
        return



    LINKS2 = set()
    url_ = re.search('(?P<protocol>http[s]?)://(?P<domain>[^:/ ]+)', url)

    if domain is None:
        domain = url_.group('domain')
    protocol = url_.group('protocol')

    response = requests.get(url)
    links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
 
    EMAILS.update(re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b', response.text))

   

    for link in links:
        if link[0] == '#' or link.split('.')[-1].lower() in ('doc','png','gif','djvu', 'jpg', 'pdf','jpeg','doc','docx'):
            continue

       

        if link[:2] == '//':
            link = '{}:{}'.format(protocol, link)

        elif link[0] == '/':
            link = '{}://{}{}'.format(protocol, domain, link)
     
        elif link[:7] != 'http://' and link[:8] != 'https://':
            link = '{}://{}/{}'.format(protocol, domain, link)

        url_ = re.search('(?P<protocol>http[s]?)://(?P<domain>[^:/ ]+)', link)


        if domain != url_.group('domain'):
            continue

        LINKS2.add(link)

    LINKS2 = LINKS2 - LINKS
    LINKS.update(LINKS2)
   

    for link in LINKS2:
        func(link, domain, step+1)






func("https://kosmoskom.ru/")
print('\n\n{}'.format('\n'.join(EMAILS)))
print('\n')
print('\n'.join(LINKS))
