import urllib2
from PIL import Image

def process(url):
    try:
        request = urllib2.urlopen(url)
    except URLError, e:
        return {'result': 'error: ' + e.reason, 'size':(0,0), 'format': 'null'}

    try:
        outfile = './cache/' + url.split('/')[2].replace('.', '_') + '.img'
        outstream = file.open(outfile, 'wb')
        outstream.write(request.read)
    except IOError, e:
        return {'result': 'error:' + e.reason, 'size':(0,0), 'format': 'null'}

    img = Image.open(outfile)
    return {'result': 'success', 'size': img.size, 'format': img.format}

    