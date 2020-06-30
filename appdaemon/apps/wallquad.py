import appdaemon.plugins.hass.hassapi as hass

class AeotecQuad(hass.Hass):
    
    
    def initialize(self):
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 1, scene_data = 0)
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 2, scene_data = 0)
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 3, scene_data = 0)
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 4, scene_data = 0)
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 1, scene_data = 2)
        self.listen_event(self.execute_action, "zwave.scene_activated", entity_id = "zwave.aeon_wallmote_quad", scene_id = 2, scene_data = 2)

    def execute_action(self, kwargs, scene_id, scene_data):
        if scene_data["scene_data"] == 0 and scene_id["scene_id"] == 1:
            self.toggle("light.shelly_ceiling_bedroom")
        elif scene_data["scene_data"] == 0 and scene_id["scene_id"] == 2:
            self.toggle("switch.shelly_elfa")
        elif scene_data["scene_data"] == 0 and scene_id["scene_id"] == 3:
            self.toggle("light.shelly_window_bedroom")
        elif scene_data["scene_data"] == 0 and scene_id["scene_id"] == 4:
            self.toggle("cover.rollerblind")
        elif scene_data["scene_data"] == 2 and scene_id["scene_id"] == 1:
            self.turn_on("scene.offscene")
        elif scene_data["scene_data"] == 2 and scene_id["scene_id"] == 2:
            self.turn_on("scene.onscene")
        else: self.log(scene_data)