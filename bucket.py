class Bucket:
    def __init__(self):
        super().__init__()
        self._item = None
        self._changes = []

    def getItem(self):
        return self._item

    def setItem(self, item):
        self._item = item

    def getChanges(self):
        return self._changes

    def setChanges(self, changes):
        self._changes = changes
