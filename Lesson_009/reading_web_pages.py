import urllib.request

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page2.htm')
for line in fhand:
    print(line.decode().strip())
