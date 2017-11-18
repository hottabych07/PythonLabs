import re



ips = {}
files = open('access.log', 'r')

for line in files:
    r = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)

    #Берем IP    
    ip = r.group()

    #Выбираем из IP - подсеть
    subnet = '.'.join(ip.split('.')[:3])

    #Добавление в список
    if subnet in ips:
        ips[subnet].add(ip) #Если уже списке уже есть такая подсеть
    else:
        ips[subnet] = {ip} #Если в списке нет такой подсети

for subnet in ips.keys():
    print(ips[subnet])



    
files.close()
