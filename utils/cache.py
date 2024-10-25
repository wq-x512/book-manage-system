class Cache:
    def __init__(self):
        self.dict = {}

    def add(self, sql, respond):
        self.dict[f'{sql}'] = respond

    def query(self, sql):
        if f'{sql}' in self.dict.keys():
            return self.dict[f'{sql}']
        else:
            return []
