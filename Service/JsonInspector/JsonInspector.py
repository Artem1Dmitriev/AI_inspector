import json
from .JsonLoader import JsonLoader
from .JsonMapper import JsonMapper


class JsonInspector():
    def __init__(self):
        self.jl = JsonLoader()
        self.global_configs = self.jl.load_all()
        self.jm = JsonMapper(self.global_configs)
        self.init_variable()

    def init_variable(self):
        # можно прямо создать атрибуты для каждого конфига
        for name, conf_obj in self.jm.configs.items():
            setattr(self, name, conf_obj)
