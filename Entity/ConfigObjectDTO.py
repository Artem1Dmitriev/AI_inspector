class ConfigObject():
    def __init__(self, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                value = ConfigObject(value)
            setattr(self, key, value)
