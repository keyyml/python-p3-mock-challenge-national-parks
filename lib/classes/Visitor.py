class Visitor:

    def __init__(self, name):
        self._name = name
        
    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 < len(name) < 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters")
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass