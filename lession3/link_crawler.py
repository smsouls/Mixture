import re
import urlparse
import urllib2
import time
import datetime
import robotparse
from downloader import Downloader

def link_crawler(seed_url, link_regex = None, delay = 5, max_depath = 1, max_urls = -1, user_agent = 'wswp', proxies = None, num_retries = 1, scrap_callback = None, cache = None):
	crawl_queue = [seed_url]
	seen = {seed_url: 0}
	num_urls = 0
	rp = self.get_robots(seed_url)
	D = Downloader(delay = delay, user_agent=user_agent, proxies = proxies, num_retries =num_retries, cache = cache)

	while crawl_queue:
		url = crawl_queue.pop()
		depth = seen[url]
		if re.can_fetch(user_agent, url):
			html = D(url)
			links = []
			if scrap_callback:
				links.extend(scrap_callback(url, html) or [])

			if depth != max_depath:
				if link_regex:
					links.extend(link for link in get_links(html) if re.match(link_regex, link))

				for link in links:
					link = self.normalize(link)
					if link not in seen:
						seen[link] = depth + 1

						if self.same_domain(seed_url, link):
							crawl_queue.append(link)

			num_urls += 1
			if num_urls >= max_urls:
				break
		else:
			print 'Blocked by robots.txt:' , url


def get_robots(url):
	rp = robotparse.RobotFileParse()
	rp.set_url(urlparse.urljoin(url, '/robots.txt'))
	rp.read()
	return rp


def get_links(html):
	webpage_regex = re.complie('<a[^>]+href=["\'](.*?)["\'], re.IGNORECASE)
	return webpage_regex.findall(html)


def normalize(seed_url, link):
	link,_ = urlparse.urldefrag(link)
	return urlparse.urljoin(seed_url, link)


def same_domain(url1, url2):
	return urlparse.urlparse(url1).netloc == urlparse.urlparse(url2).netloc


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, user_agent='BadCrawler')
    link_crawler('http://example.webscraping.com', '/(index|view)', delay=0, num_retries=1, max_depth=1, user_agent='GoodCrawler')


