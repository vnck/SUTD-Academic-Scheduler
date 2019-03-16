class Room:
    def __init__(self,name,req):
        self.name = name
        self.req = req
    def __repr__(self):
        return "<Room: {} type:{}>".format(self.name,self.req)