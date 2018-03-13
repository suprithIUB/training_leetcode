class Codec:
    def __init__(self):
	self.url_map = dict()
        self.BASE_MAPPER = '0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.BASE = 62

    def convert_to_base62(self, number):
        result = ''
        temp = number
        while temp:
            c = self.BASE_MAPPER[temp % self.BASE]
            temp = temp // self.BASE
            result = c + result
        return result
    
    def get_hash(self, long_url):
        from hashlib import md5
        utf_8 = long_url.encode('utf-8')
        hex_digest = md5(utf_8).hexdigest()
        lsb_43_binary = bin(int(hex_digest, 16))[-43:]
        decimal = int('0b' + lsb_43_binary, 2)
        return decimal

    def encode(self, long_url):
        decimal_number = self.get_hash(long_url)
        tiny_url = self.convert_to_base62(decimal_number)
        item = self.url_map.get(tiny_url, None)
        if not item:
            self.url_map[tiny_url] = long_url
        return tiny_url

    def decode(self, short_url):
        
        item = self.url_map.get(short_url, None)
        return item

if __name__ == "__main__":
    tinyurl = Codec()
    print(tinyurl.convert_to_base62(4546386693657))
    print(tinyurl.encode('https://leetcode.com/problems/design-tinyurl'))
    print(tinyurl.decode(''))
    
