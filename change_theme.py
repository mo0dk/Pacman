from datetime import datetime

from store_settings import TextureSetting


class ThemeApi:
    def __init__(self):
        self._textures_mode: TextureSetting = TextureSetting.classic

    @property
    def textures_mode(self) -> TextureSetting:
        return self._textures_mode

    @textures_mode.setter
    def textures_mode(self, value: TextureSetting):
        self._textures_mode = value

    @property
    def texture_modifier(self):
        real_setting = self.textures_mode
        if self.textures_mode is TextureSetting.automatic:
            current_time = datetime.now()
            if 18 > current_time.hour > 5:
                real_setting = TextureSetting.classic
            else:
                real_setting = TextureSetting.alternative
        return real_setting.texture_modifier

    def __str__(self):
        return "ThemeApi(" + \
               f"textures_mode={self.textures_mode}, " + \
               f"texture_modifier={self.texture_modifier}" + \
               ")"
