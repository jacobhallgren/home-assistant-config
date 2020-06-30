import appdaemon.plugins.hass.hassapi as hass

class AeotecQuad(hass.Hass):
    
    
    def initialize(self):
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 2, scene_data = 2)

    def execute_action(self, kwargs, scene_id, scene_data):
        if scene_data["scene_data"] == 2 and scene_id["scene_id"] == 2:
            self.toggle("cover.rollerblind")
            self.log(scene_data)
        else: self.log(scene_data)