from .ConfigObject_type import ConfigObject


class JsonMapper:
    def __init__(self, configs):
        self.configs = {}
        for name, conf in configs.items():
            self.configs[name] = ConfigObject(conf)

    def __getattr__(self, item):
        if item in self.configs:
            return self.configs[item]
        raise AttributeError(f"No config named {item}")
