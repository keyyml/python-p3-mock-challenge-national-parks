class NationalPark:

    def __init__(self, name):
        self._name = name


    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else: 
            raise Exception("Name must be a string.")
        
    def trips(self):
        pass
    
    def visitors(self):
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass
