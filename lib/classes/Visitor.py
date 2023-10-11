class Visitor:

    def __init__(self, name):
        self._name = name
        
        self._trips = []
        self._national_parks = []

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <=- len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters")
    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list(set(self._national_parks))
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self._trips if trip.national_park == park])
        