class Room:
    def __init__(self,name,req):
        self.name = name
        if name[0:2]=="CC":
            self.req = self.name
        else:
            self.req = req
    def __repr__(self):
        return "<Room: {} type:{}>".format(self.name,self.req)