
import urllib
import urllib2
import glob
import sqlite3
import os
import cookielib
import json
import time
import lxml.html

LOGIN_EMAIL = 'example@webscraping.com'
LOGIN_PASSWORD = 'example'
LOGIN_URL = 'http://example.webscraping.com/user/login'


def parse_form(html):
	tree = lxml.html.fromstring(html)
	data = {}
	for e in tree.cssselect('form input'):
		if e.get('name'):
			data[e.get('name')] = e.get('value')
	return data



def login_basic():
	data = {'email': LOGIN_EMAIL, 'password': LOGIN_PASSWORD}
	encode_data = urllib.urlencode(data)
	request = urllib2.Request(LOGIN_URL, encode_data)
	response = urllib2.urlopen(request)
	print response.getUrl()


def login_formkey():
	html = urllib2.urlopen(LOGIN_URL).read()
	data = parse_form(html)
	data['email'] = LOGIN_EMAIL
	data['password'] = LOGIN_PASSWORD
	encode_data = urllib.urlencode(data)
	request = urllib2.Request(LOGIN_URL, encode_data)
	response = urllib2.urlopen(request)
	print response.getUrl()


def login_cookies():
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html = opener.open(LOGIN_URL).read()
	data = parse_form(html)
	data['email'] = LOGIN_EMAIL
	data['password'] = LOGIN_PASSWORD
	encode_data = urllib.urlencode(data)
	request = urllib2.Request(LOGIN_URL, encode_data)
	response = opener.open(request)
	print response.getUrl()
	return opener


def load_ff_sessions(session_filename):
	cj = cookielib.CookieJar()
	if os.path.exists(session_filename):
		try:
			json_data = json.loads(open(session_filename, 'rb').read())
		except ValueError as e:
			print 'Error parsing session JSON:', str(e)
		else:
			for window in json_data.get('windows', []):
				for cookie in window.get('cookies', []):
					import pprint; pprint.pprint(cookie)
					c = cookielib.Cookie(0, cookie.get('name', ''), cookie.get('value', ''), None, False, cookie.get('host', ''), cookie.get('host', '').startswith('.'), cookie.get('host', '').startswith('.'), cookie.get('path', ''), False, False, str(int(time.time()) + 3600 * 24 * 7), False, None, None, {})
					cj.set_cookie(c)
	else:
		print 'Session filename does not exist:', session_filename
	return cj


def find_ff_sessions():
	paths = [
        '~/.mozilla/firefox/*.default',
        '~/Library/Application Support/Firefox/Profiles/*.default',
        '%APPDATA%/Roaming/Mozilla/Firefox/Profiles/*.default'
    ]
    for path in paths:
    	filename = os.path.join(path, 'sessionstore.js')
    	matches = glob.glob(os.path.expanduser(filename))
    	if matches:
    		return matches[0]

def login_firefox():
	session_filename = find_ff_sessions()
	cj = load_ff_sessions(session_filename)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	html = opener.open(LOGIN_URL).read()

	tree = lxml.html.fromstring(html)
	print tree.cssselect('ul#navbar li a')[0].text_content()
	return opener













