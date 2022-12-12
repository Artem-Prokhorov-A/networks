import sys
import subprocess
import platform

def check_ping(hostname, m):
    if platform.system() == 'Darwin':
        request = 'ping -D do -s ' + str(m) + ' ' + hostname + ' -c 1' 
    elif platform.system() == 'Windows':
        request = 'ping ' + hostname + ' -l ' + str(m) + ' -n 1' 
    else:
        request = 'ping -M do -s ' + str(m) + ' ' + hostname + ' -c 1'
    request = request.split(' ')
    response = subprocess.call(request, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response

def main(argv):
    if len(argv) < 2:
        raise "no ips?"
    hostname = argv[1]
    print(hostname)
    if check_ping(hostname, 0):
        raise "bad ip"
    l = 1
    r = 4000
    while r - l > 1:
        m = (r + l) // 2
        if check_ping(hostname, m):
            r = m
        else:
            l = m
    print('MTU:', l)

if __name__ == '__main__':
    main(sys.argv)