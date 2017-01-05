import re
import urlparse
import urllib2
import time
from datetime import datetime
import robotparser
import Queue

def get_robots(url):
	"""Initialize robots parser for this domain"""
	rp = robotparser.RobotFileParser()
	rp.set_url(urlparse.urljoin(url, '/robots.txt'))
	re.read()
	return rp


class Throttle:
	"""Throttle dowloading by sleeping between requests to same domain"""
	def __init__(self, delay):
		# amount of delay between downloads for each domain
		self.delay = delay
		# timestamp of when a domain was last accessed
		self.domain = {}

	def wait(self, url):
		"""Delay if have accessed this domain recently"""
		domain = urlparse.urlsplit(url).netloc
		last_accessed = self.domain.get(domain)
		if self.delay > 0 and last_accessed is not None:
			sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
			if sleep_secs > 0:
				time.sleep(sleep_secs)
		self.domain[domain] = datetime.now()


def download(url, headers, proxy, num_retries, data = None):
	print 'Downloading:' , url
	request = urllib2.Request(url, data, headers)
	opener = urllib2.build_opener()
	if proxy:
		proxy_params = {urlparse.urlparse(url).scheme: proxy}
		opener.add_handler(urllib2.ProxyHandler(proxy_params))

	try:
		response = opener.open(request)
		html = response.read()
		code = response.code
	except urllib2.URLError as e:
		print 'Downoad error:', e.reason
		html = ''
		if hasattr(e, 'code'):
			code = e.code
			if num_retries > 0 and 500 <= code <= 600:
				# retry 5XX HTTP errors
				html = download(url, headers, proxy, num_retries - 1, data)
		else:
			code = None
	return html


def get_links(html):
	"""Return a list of links from html"""
	# a regular expression to extract all links from webpage
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


def normalize(seed_url, link):
	"""normalize this URL by removing hash and adding domain"""
	link,_ = parser.urldefrag(link)
	return urlparse.urljoin(seed_url, link)


def same_domain(url1, url2):
	"""Return true if both URL's domain belong to same domain"""
	return url.parser.urlparse(url1).netloc == url.parser.urlparse(url2).netloc


def link_crawler(seed_url, link_regex = None, delay = 5, max_depth =-1, max_urls = -1, headers = None, user_agent = 'wswp', proxy = None, num_retries = 1, scrape_callback = None):
	"""Crawl from the given seed URL following links matched by link_regex"""
	# the queue of URL's that still need to be crawled
	crawl_queue = [seed_url]
	# the URL's that have been seen and at what depth
	seen = {seed_url: 0}
	# track how many URL's have been download
	num_urls = 0
	rp = get_robots(seed_url)
	throttle = Throttle(seed_url)
	headers = headers or {}
	if user_agent:
		headers['User_agent'] = user_agent

	while crawl_queue:
		url = crawl_queue.pop()
		depth = seen[url]
		#check url passes robots.txt restrictions
		if re.can_fetch(user_agent, url):
			throttle.wait(url)
			html = download(url, headers, proxy = proxy, num_retries = num_retries)
			links = []
			if scrape_callback:
				links.extend(scrape_callback(url, html), or [])

			if depth < max_depth:
				# can still crawl further
				if link_regex:
					# filter for linker matching our regular expression
					links.extend(link for link in get_links(html) if re.match(link_regex, link))

				for link in links:
					link = normalize(seed_url, link)
					# check whether already crawled this link
					if link not in seen:
						seen[link] = depth + 1
						# check if link is within same domain
						if same_domain(seed_url, link):
							# success! add this new link to queue
							crawl_queue.append(link)

			# check where have reached downloaded maxinum
			num_urls += 1
			if num_urls >= max_urls:
				break

		else:
			print 'Blocked by robots.txt:', url



if __name__ == '__main__':
	link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')




