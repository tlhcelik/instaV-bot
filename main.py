import mechanize
import os
import time
import urllib2
import sys
from plyer import notification


def get(username, password, target_username):
    time.sleep(7)  # Waiting for 7 second. Because instagram mean to this program

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = []
    try:
        br.open(url='https://www.instagram.com/accounts/login/?force_classic_login')
        br.select_form(nr=0)
        br.form['username'] = username
        br.form['password'] = password
        br.submit()
    except:
        # set proxy
        print '\nDont Submitting...\n'
        pass

    html_codes = br.open('https://www.instagram.com/{0}'.format(target_username)).read()

    who = br.title()

    f = open('output.txt', 'w')
    f.write(html_codes)
    f.close()

    rd = open('output.txt', 'r')
    reads = rd.read()

    _find_start_index = reads.find('thumbnail_src')  # last shared photo in first char index
    _img_url = ' '

    for i in range(_find_start_index, _find_start_index + len('thumbnail_src') + 150):
        if reads[i] == '?':
            break
        _img_url += reads[i]

    rd.close()

    clear_photo_url = _img_url[18:]

    sizes_list = ['s640x640','s750x750', 's480x480', 's320x320']

    for size in sizes_list:
        resize_index_start = clear_photo_url.find(str(size))
        if resize_index_start != -1:
            max_size_img_url = clear_photo_url[:resize_index_start]
            max_size_img_url += clear_photo_url[resize_index_start + 9:]
            break
        else:
            max_size_img_url = clear_photo_url

    photo_name_index = clear_photo_url.rfind('/')  # finding last / index
    photo_name = clear_photo_url[photo_name_index + 1:]

    print '#' * 70
    print who
    """

    print '_find_start_index    :  ', _find_start_index  # return to thumbnail_src char index
    print '_img_url             : ', _img_url
    print 'resize_index_start   :  ', resize_index_start
    print 'clear_photo_url      :  ', clear_photo_url
    print 'max_size_img_url     :  ', max_size_img_url
    print 'photo_name           :  ', photo_name

	"""

    if not os.path.isfile(photo_name):
        image_response = br.open_novisit(url=max_size_img_url)

        path = os.getcwd()
        if os.name == 'nt':
            path += '\\'
        else:
            path += '/'
        path += photo_name

        with open(path, 'wb') as f:
            f.write(image_response.read())

        f.close()
        if os.name() != 'nt':
            print ('{0}{1} Have a new photo.{2}\n{3}'.format('\033[92m', target_username, '\033[0m', time_now()))
            display_notify(target_username)
        else:
            print ('{0} Have a new photo.\n{1}'.format(target_username,time_now()))
            display_notify(target_username)
    br.open('https://www.instagram.com/accounts/logout')
    br.close()

    print 'Exiting...'
    print '#' * 70

    pass  # get END


def set_proxy():
    _proxy_list = {'114.6.135.179': '8080',
                   '200.75.9.36': '3128',
                   '58.176.221.18': '8998',
                   '197.218.196.70': '8080',
                   }
    try:

        proxy = urllib2.ProxyHandler({'https': '197.218.196.70:8080'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        return True
    except:
        return False


def time_now():
    times = time.ctime()
    return times


def get_minute():
    minute = sys.argv[1]
    minute = int(minute)

    if minute < 5:
        print 'Example Usage : python instagram.py [ minute > 5 ]'
        sys.exit(0)

    else:
        return minute

def display_notify(uname):
    notification.notify(
        message = '{0}. Have a new photo'.format(uname),
        title='InstaV'
    )
    return



if __name__ == '__main__':
    u = 'instagram_username'
    p = 'instagram_password'

    minute = get_minute()
    minute = minute * 60

    u_list = ['tlh.celik'']

    while True:
        try:
            for target in u_list:
                control=get(u, p, target)

            print  'Waiting for {0} minute...'.format(minute/60)
            time.sleep(minute)
        except:
            pass
