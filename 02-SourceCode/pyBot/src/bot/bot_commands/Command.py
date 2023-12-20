import json

class Command:
    def __init__(self):
        s = open("src/resources/configs/settings.json")
        self.settings = json.load(s)