import copy
class Course:
    
    def __init__(self,name):
        self.name = name
        self._classes = []
        self.professors = []
        self.studentGroups = []
    def addClass(self,req,duration):
        """stores tuple(req,duration) in classes list"""
        tupl = (req,duration)
        self._classes.append(tupl)
    
    def getClasses(self):
        return copy.deepcopy(self._classes)
    
    def __repr__(self):
        return "<Course {} classes {}>".format(self.name,str(self._classes))
    