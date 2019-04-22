# Defines the dictionary of the planets with orbital periods.
orbital = {
        "mercury": 0.2408467, "venus": 0.61519726, "earth": 1, 
        "mars": 1.8808158, "jupiter": 11.862615, "saturn": 29.447498, 
        "uranus": 84.016846, "neptune": 164.79132
        }

def sec_to_year(sec, planet):
    """ This function converts a value of sec, to age in years on a planet. """
    result = sec / (31557600 * orbital[planet])
    return round(result, 2)


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return sec_to_year(self.seconds, "mercury")
    def on_venus(self):
        return sec_to_year(self.seconds, "venus")
    def on_earth(self):
        return sec_to_year(self.seconds, "earth")
    def on_mars(self):
        return sec_to_year(self.seconds, "mars")
    def on_jupiter(self):
        return sec_to_year(self.seconds, "jupiter")
    def on_saturn(self):
        return sec_to_year(self.seconds, "saturn")
    def on_uranus(self):
        return sec_to_year(self.seconds, "uranus")
    def on_neptune(self):
        return sec_to_year(self.seconds, "neptune")