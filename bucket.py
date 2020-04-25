class Bucket:
    def __init__(self):
        super().__init__()
        self._item = None
        self._changes = []

    def get_item(self):
        return self._item

    def set_item(self, item):
        self._item = item

    def get_changes(self):
        return self._changes

    def set_changes(self, changes):
        self._changes = changes
