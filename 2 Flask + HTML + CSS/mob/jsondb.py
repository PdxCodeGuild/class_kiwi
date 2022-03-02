'''
A simple JSON-based database that can be used with Flask.
Usage:

import from jsondb import JsonDB
db = JsonDB('database.json')
db.load()
x = db.get('x', 0)
x += 1
db.set('x', x)
db.save()
'''


import json


class JsonDB:
    def __init__(self, path='db.json'):
        self.path = path
        self.data = None
    
    def load(self):
        with open(self.path, 'r') as file:
            self.data = json.loads(file.read())
    
    def save(self):
        with open(self.path, 'w') as file:
            file.write(json.dumps(self.data, indent=4, sort_keys=True))
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
    
    def clear(self, key=None):
        if key is not None:
            del self.data[key]
        else:
            self.data = {}
    