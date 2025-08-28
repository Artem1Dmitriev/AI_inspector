import os, sys, json

class JsonLoader():
    def __init__(self):
        self.folder = os.getenv("CONFIGS_PATH", os.path.join(os.getcwd(), "Configs"))

        if not os.path.exists(self.folder):
            raise FileNotFoundError(f"Папка конфигов не найдена: {self.folder}")


    def load_all(self):
        configs = {}
        for filename in os.listdir(self.folder):
            if filename.endswith(".json"):
                path = os.path.join(self.folder, filename)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        configs[filename[:-5]] = json.load(f)
                except Exception as e:
                    print(f"Ошибка загрузки {filename}: {e}")
        return configs
