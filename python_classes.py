class LatLong:
    '''Creates an object of the type 'LatLong' that corresponds to the geographic longitude/latitude in\
 degrees/minutes/seconds.'''
    def __init__(self, degrees = 0, minutes = 0, seconds = 0):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds
    
    
    #We force 'degrees' to be either integers or floats. We adjust our degrees to lie within the set [0,360)
    def auto_degrees(self):
        return self._deg
    
    def set_degrees(self, value):
        if type(value) not in [int,float]:
            if type(value) == complex:
                raise ValueError("Numbers of complex type are not valid for degree assignment.")
            raise ValueError("Geographic degrees must be numbers.")
        mod_degree = value%360
        if value < 0 or value >= 360:
            print("Degree input truncated to '{}' to lie within the standard [0,360).".format(mod_degree))
        self._deg = mod_degree
            
    degrees = property(auto_degrees,set_degrees)


    #We force 'minutes' to be either integers or floats within the set [0,60)
    def auto_minutes(self):
        return self._min
    
    def set_minutes(self, value):
        if type(value) not in [int,float]:
            if type(value) == complex:
                raise ValueError("Numbers of complex type are not valid for minute assignment.")
            else:
                raise ValueError("Geographic minutes must be numbers.")
        else:
            if value < 0 or value >=60:
                raise ValueError("Geographic minutes should be between 0 and 60.")
            else:
                self._min = value
                
    minutes = property(auto_minutes,set_minutes)
                
     
    #We force 'seconds' to be either integers or floats within the set [0,60)           
    def auto_seconds(self):
        return self._sec
    
    def set_seconds(self, value):
        if type(value) not in [int,float]:
            if type(value) == complex:
                raise ValueError("Numbers of complex type are not valid for second assignment.")
            else:
                raise ValueError("Geographic seconds must be numbers.")
        else:
            if value < 0 or value >=60:
                raise ValueError("Geographic seconds should be between 0 and 60.")
            else:
                self._sec = value
                
    seconds = property(auto_seconds, set_seconds)
