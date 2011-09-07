import urllib2
from PIL import Image

def process(url):
    try:
        request = urllib2.urlopen('http://' + url + '/favicon.ico')
    except urllib2.URLError, e:
        return {'result': 'error: ' + e.reason, 'size':(0,0), 'format': 'null'}

    try:
        outfile = './cache/' + url.replace('.', '_') + '.img'
        outstream = open(outfile, 'wb')
        outstream.write(request.read())
        outstream.close()
    except IOError, e:
        return {'result': 'error', 'size':(0,0), 'format': 'null'}

    img = Image.open(outfile)
    return {'result': 'success', 'size': img.size, 'format': img.format}

    
