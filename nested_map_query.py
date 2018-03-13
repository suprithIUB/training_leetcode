from html.parser import HTMLParser

class PyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = dict()
        self.processing = list()
    
    def handle_starttag(self, tag, attrs):
        print("Start", tag, attrs)

    def handle_endtag(self, tag):
        print("End", tag)
    
    def handle_data(self, data):
        print('Data', data)

if __name__ == "__main__":
    p = PyParser()
    p.feed('<tag1 attr1=value1 attr2=value2></tag1>')
    

