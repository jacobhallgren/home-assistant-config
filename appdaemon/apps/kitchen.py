import appdaemon.plugins.hass.hassapi as hass  

class KitchenToggle(hass.Hass):

  def initialize(self):
    self.listen_event(self.light_toggle, "zwave.scene_activated", entity_id = "zwave.kitchen_lamp", scene_id = 26)
    self.listen_event(self.light_toggle, "zwave.scene_activated", entity_id = "zwave.fibaro_kitchen_spots", scene_id = 26)
    self.listen_event(self.set_brightness, "zwave.scene_activated", entity_id = "zwave.kitchen_lamp", scene_id = 22)
    self.listen_event(self.set_brightness, "zwave.scene_activated", entity_id = "zwave.fibaro_kitchen_spots", scene_id = 22)
  
  def get_status(self, entity, attribute, kwargs):
    self.state = self.get_state("light.kitchen_bench", attribute="brightness")
    
  def light_toggle(self, entity, attribute, kwargs):
    self.toggle("light.kitchen_bench")

  def set_brightness(self, entity, attribute, kwargs):
    self.get_status(entity, attribute, kwargs)
    if self.state >=  128:
      self.turn_on(entity_id='light.kitchen_bench', brightness='127')
      self.log(f"setting brightness to: 50, last value: {self.state}")
    elif self.state >  0 and self.state <=127:
      self.turn_on(entity_id='light.kitchen_bench', brightness='254')
      self.log(f"setting brightness to: 100%, last value {self.state}")
    else: self.log("Something went wrong")
    #
    