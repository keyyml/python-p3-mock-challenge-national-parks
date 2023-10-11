class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        visitor._trips.append(self)
        visitor._national_parks.append(national_park)
        national_park._trips.append(self)
        national_park._visitors.append(visitor)

        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) == str and len(start_date) >= 7:
            self._start_date = start_date
        else:
            raise Exception
        
    @property
    def end_date(self, end_date):
        if type(end_date) == str and len(end_date) >= 7:
            self._end_date = end_date
        else:
            raise Exception
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        from classes.Visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor 
        else: 
            raise Exception
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        from classes.National_Park import National_Park
        if isinstance(national_park, National_Park):
            self._national_park = national_park 
        else: 
            raise Exception
