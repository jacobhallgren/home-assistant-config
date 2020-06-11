import appdaemon.plugins.hass.hassapi as hass  

class MotionLights(hass.Hass):
    
    def initialize(self):
        self.motion_sensor = self.args['motion_sensor']
        self.light = self.args['light']
        self.timeout = self.args['timeout']

        self.timer = False
        self.listen_state(self.motion_callback, self.motion_sensor, new = "on")
        self.listen_state(self.set_timer, self.motion_sensor, new = "off")

    def set_timer(self, entity, attribute, old, new, kwargs):
        self.timer = self.run_in(self.timeout_callback, self.timeout)

    def motion_callback(self, entity, attribute, old, new, kwargs):
        self.turn_on(self.light)
        if self.timer != False:
            self.cancel_timer(self.timer)

    def timeout_callback(self, kwargs):
        self.timer = False
        self.turn_off(self.light)