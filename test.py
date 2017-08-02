# -*- coding: utf-8 -*-

import urllib2

def main():
	url = 'http://192.240.120.35//mp43/102470.mp4?st=RV6DbcuOBHlC7u6IuZNl_Q&e=1501683762'
	req = urllib2.Request(url)
	req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	response = urllib2.urlopen(req)
	data = response.read()
	with open('test.mp4','wb') as fd:
		fd.write(data)

if __name__ == '__main__':
	main()
