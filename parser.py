
class Parser:
    def __init__(self):
        pass
    def parse_title(self):
        pass
    def parse_link(self):
        pass

    def parse_price(self, price):
        return price[1:]

    def parse_datetime(self, time):
        return time.split()

    def parse_numberOfBedroom(self, bedroom):
        result = [None, None]
        if (bedroom == None): return result
        for x in bedroom.split('\n'):
            if 'br' in x:
                result[0] = x.split()[:-1][0][:-2]
            if 'ft2' in x:
                result[1] = x.split()[:-1][0][:-3]

        return result