import appdeamon.plugins.hass.hassapi as hass

class Verisure(hass.hass)


    def initialize(self):
        self.listen_event(self.alarm, alarm)