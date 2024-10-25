class Recycle:
    def __init__(self):
        self.queue = [[], []]
        self.idx = 0

    def update(self, elements):
        self.queue[self.idx].clear()
        for i in self.queue[self.idx ^ 1]:
            i.hide()
        for i in elements:
            i.show()
            self.queue[self.idx].append(i)
        self.idx ^= 1
