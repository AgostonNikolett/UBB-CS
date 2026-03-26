from repository.base_repository import InMemoryRepository
from domain.event import Event
import os

class EventFileRepository(InMemoryRepository):
    def __init__(self, file_path: str):
        super().__init__()
        self._file_path = file_path
        self._load_data()

    def _load_data(self):
        if not os.path.exists(self._file_path): return
        with open(self._file_path, 'r') as f:
            for line in f:
                if line.strip():
                    event = Event.from_file_string(line)
                    super().store(event.get_id(), event)

    def _save_data(self):
        with open(self._file_path, 'w') as f:
            for event in self.get_all():
                f.write(event.to_file_string() + '\n')

    def add(self, event: Event):
        super().store(event.get_id(), event)
        self._save_data()

    def update(self, event_id: str, date: str, time: str, description: str):
        event = self.find_by_id(event_id)
        event.set_date(date)
        event.set_time(time)
        event.set_description(description)
        self._save_data()

    def delete(self, event_id: str):
        super().remove(event_id)
        self._save_data()