import appdaemon.plugins.hass.hassapi as hass  

class Shelly(hass.Hass):

  def initialize(self):
    self.listen_event(self.light_on, "shelly_switch_click", entity_id = "switch.shelly_shsw_1_770a37", click_cnt = 4)

  def light_on(self, entity, attribute, kwargs):
    self.toggle("switch.shelly_shplg_s_7ae3b7")

  #test