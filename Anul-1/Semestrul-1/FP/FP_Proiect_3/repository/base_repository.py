class InMemoryRepository:
    def __init__(self):
        self._items = {}

    def store(self, item_id: str, item):
        if item_id in self._items:
            raise ValueError(f"Item with ID {item_id} already exists.")
        self._items[item_id] = item

    def find_by_id(self, item_id: str):
        if item_id not in self._items:
            raise ValueError(f"Item with ID {item_id} not found.")
        return self._items[item_id]

    def remove(self, item_id: str):
        if item_id not in self._items:
            raise ValueError(f"Item with ID {item_id} not found.")
        return self._items.pop(item_id)

    def get_all(self) -> list:
        return list(self._items.values())