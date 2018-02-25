import urllib.request

def check():
    website = 'http://bogans.uk'
    word = 'Instagram'

    result = urllib.request.urlopen(website).read().decode('utf-8')

    if word not in result:
        raise Exception('Failed to find specified string ' + word + ' on site ' + website)
