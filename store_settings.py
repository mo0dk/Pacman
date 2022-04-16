import csv
import enum
import os
from dataclasses import dataclass

import global_variables

filename = "saves/settings.csv"
_settings_cache = None


@enum.unique
class TextureSetting(enum.IntEnum):
    classic = 0
    alternative = 1
    automatic = 2

    def __str__(self):
        if self is TextureSetting.classic:
            return "Классическая"
        if self is TextureSetting.alternative:
            return "Альтернативная"
        if self is TextureSetting.automatic:
            return "Автоматическая"
        return ""

    @property
    def texture_modifier(self):
        if self is TextureSetting.alternative:
            return "r_"
        return ""

    @texture_modifier.setter
    def texture_modifier(self, value: str):
        if value == "":
            self.value = TextureSetting.classic.value
        if value == "r_":
            self.value = TextureSetting.alternative.value


@dataclass
class Settings:
    difficulty: float
    cell_size: int
    texture_setting: TextureSetting


def clear_settings():
    open(filename, "w", encoding="utf-8").close()


def get_settings():
    global _settings_cache
    if _settings_cache is None:
        if not os.path.exists(filename):
            clear_settings()
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for line_num, line in enumerate(reader):
                if len(line) >= 3:
                    result = Settings(float(line[0]), int(line[1]), TextureSetting(int(line[2])))
                    _settings_cache = result
                    return result
                elif global_variables.debug:
                    print(f"[WARNING] Can not parse {filename}:{line_num} {line}")
    else:
        return _settings_cache


def store_settings():
    if not os.path.exists(filename):
        clear_settings()
    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow((
            str(global_variables.difficulty), str(global_variables.cell_size),
            str(global_variables.theme_api.textures_mode.value)
        ))
    global _settings_cache
    _settings_cache = Settings(global_variables.difficulty, global_variables.cell_size, global_variables.theme_api)
