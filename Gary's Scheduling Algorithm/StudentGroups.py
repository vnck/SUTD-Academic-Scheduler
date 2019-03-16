class StudentGroup:
    def __init__(self,name,course):
        """
        attr:name,isFreshmore,course
        note course is a list of course objects
        """
        self.name = name
        if name[0:2] == "CC":
            self.isFreshmore = True
        else:
            self.isFreshmore = False
        self.course = course