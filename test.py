import urllib2

def set_proxy():
    _proxy_list = {'114.6.135.179': '8080',
                   '200.75.9.36': '3128',
                   '58.176.221.18': '8998',
                   '197.218.196.70': '8080',
                   }
    try:

        proxy = urllib2.ProxyHandler({'https': '197.218.196.70:8080'})
        opener = urllib2.build_opener(SocksiPyHandler(socks.PROXY_TYPE_SOCKS4, '114.6.135.179', 8080))

        urllib2.install_opener(opener)
        ip = urllib2.urlopen('http://malc.hol.es/static_ip').read()
        print 'BEFORE : ',ip
        return True
    except:
        return False


ip = urllib2.urlopen('http://malc.hol.es/static_ip').read()
print 'AFTER : ',ip

set_proxy()