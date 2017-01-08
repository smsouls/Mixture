#coding=utf-8 
import os
import re
import urlparse
import shutil
import zlib
from datetime import datetime, timedelta

datetime.utcnow()
try:
	import cPickle as pickle
except ImportError:
	import pickle

from link_crawler import link_crawler

class DiskCache:
	"""docstring for DiskCache"""
	def __init__(self, cache_dir = 'cache', expires = timedelta(days = 30), compress = True):
		self.cache_dir = cache_dir
		self.expires = expires
		self.compress = compress

	def __getitem__(self, url):
		"""从一个路径中获取一个文件的内容"""
		path = self.url_to_path(url)
		if os.path.exists(path):
			with open(path, 'rb') as fp:
				data = fp.read()
				if self.compress:
					data = zlib.decompress(data)
					result, timestamp = pickle.loads(data)
				if self.has_expired(timestamp):
					raise KeyError(url + ' has expired')
				return result
		else:
			raise KeyError(url + ' does not exist')


	def __setitem__(self, url, result):
		"""存储一个文件"""
		path = self.url_to_path(url)
		folder = os.path.dirname(path)
		if not os.path.exists(folder):
			os.makedirs(folder)

		data = pickle.dumps((result, datetime.utcnow()))
		if self.compress:
			data = zlib.compress(data)
			with open(path, 'wb') as fp:
				fp.write(data)


	def __delitem__(self, url):
		"""将目录存储的文件删除"""
		path = self.url_to_path(url)
		try:
			os.remove(path)
			os.removedirs(os.path.dirname(path))
		except OSError:
			pass


	def url_to_path(self, url):
		"""获取一个文件的URL"""
		components = urlparse.urlsplit(url)
		path = components.path
		if not path:
			path = '/index.html'
		elif path.endswith('/'):
			path += 'index.html'

		filename = components.netloc + path + components.query

		filename = re.sub('[^/0-9z-zA-Z\-.,;_]', '_', filename)
		return os.path.join(self.cache_dir, filename)


	def has_expired(self, timestamp):
		"""判断文件是否过期"""
		return datetime.utcnow() > timestamp + self.expires


if __name__ == '__main__':
	link_crawler('http://example.webscraping.com/', '/(index|view)', cache=DiskCache())

