import appdaemon.plugins.hass.hassapi as hass

class FibaroKeyfob(hass.Hass):

  def initialize(self):
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 1, scene_data = 7680)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 3, scene_data = 7680)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 2, scene_data = 7680)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 5, scene_data = 7800)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 6, scene_data = 7800)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 5, scene_data = 7860)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 1, scene_data = 7860)
    self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.fibaro_keyfob", scene_id = 2, scene_data = 7860)


  def execute_action(self, kwargs, scene_id, scene_data):
    if scene_data["scene_data"] == 7680 and scene_id["scene_id"] == 1:
      self.toggle("switch.shelly_sofa_left")
    elif scene_data["scene_data"] == 7680 and scene_id["scene_id"] == 2:
      self.toggle("switch.shelly_sofa_right")
    elif scene_data["scene_data"] == 7800 and scene_id["scene_id"] == 5:
      self.turn_on("scene.movie")
    elif scene_data["scene_data"] == 7800 and scene_id["scene_id"] == 6:
      self.turn_on("scene.onscene")
    elif scene_data["scene_data"] == 7860 and scene_id["scene_id"] == 5:
      self.turn_on("scene.offscene")
    elif scene_data["scene_data"] == 7860 and scene_id["scene_id"] == 1:
      self.toggle("light.matsal_celing_level")
    elif scene_data["scene_data"] == 7860 and scene_id["scene_id"] == 2:
      self.toggle("light.ceiling_livingroom_level")
    elif scene_data["scene_data"] == 7680 and scene_id["scene_id"] == 3:
      self.toggle("light.tv_bench_level")
    else: self.log(scene_data)   
    #else: self.log(scene_data["scene_data"])
