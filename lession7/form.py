
import urllib
import urllib2
import cookielib	
from io import BytesIO
import lxml.html
from PIL import Image

REGISTER_URL = 'http://example.webscraping.com/user/register'


def extract_image(html):
	tree = lxml.html.fromstring(html)
	