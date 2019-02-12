import re



ips = {}
files = open('access.log', 'r')

for line in files:
    r = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)

    ip = r.group()

    subnet = '.'.join(ip.split('.')[:3])

    if subnet in ips:
        ips[subnet].add(ip) 
    else:
        ips[subnet] = {ip}

for subnet in ips.keys():
    print(ips[subnet])



    
files.close()
