class National_Park:

    all = []

    def __init__(self, name):
        self._name = name

        self._trips = []
        self._visitors = []

        National_Park.all.append(self)

    @classmethod
    def most_visited(cls):
        curr_park = None
        curr_max_visits = 0

        for national_park in cls.all:
            if len(national_park.trips) > curr_max_visits:
                curr_park = national_park
                curr_max_visits = len(national_park.trips)

        return curr_park

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
        return self._trips
    
    def visitors(self):
        return list(set(self._visitors))
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if len(self._visitors) == 0:
            return None
        
        visitor_frequencies = {}

        for visitor in self._visitors:

            if visitor not in visitor_frequencies:
                visitor_frequencies[visitor] = 0
            else: 
                visitor_frequencies[visitor] += 1

        return max(visitor_frequencies, key = visitor_frequencies.get)
    

        return max(self._visitors, key = self.visitors.count)
