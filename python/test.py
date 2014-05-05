import urllib2

html2 = urllib2.urlopen('http://www.memoirstream.com/rhmorris/memoirs/memoirs1945.html#.U2f5TfldVe8').read()


from bs4 import BeautifulSoup
soup = BeautifulSoup(html2)


z = soup.select('div#item1 > p.style8 > strong > span.style15')
z1 = z[0]
print z
print z1.string
y = soup.select('div#item1 > ul.style8 > li')
y1 =y[0]

for x in y:

	if z1.string == "What was happening in the world:":
		print x.string
	else:
		print 'false'

	


f = open('test.html', 'w')

f.write('<p>'+z1.string+'</p>')

f.close

