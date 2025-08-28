from .JsonLoader import JsonLoader
from .JsonMapper import JsonMapper
from Entity.JSON_interface import IConfigProvider

class JsonConfigProvider(IConfigProvider):
    def __init__(self):
        jl = JsonLoader()
        global_configs = jl.load_all()
        self.jm = JsonMapper(global_configs)

    def get(self, name: str):
        return getattr(self.jm, name)
