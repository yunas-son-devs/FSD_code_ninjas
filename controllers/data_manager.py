import os
import pickle

class DataManager:
    def __init__(self, file_path="data/students.data"):
        self.file_path = file_path
        self._make_file_ready()

    def _make_file_ready(self):
        folder = os.path.dirname(self.file_path) or "."
        os.makedirs(folder, exist_ok=True)
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            with open(self.file_path, "wb") as f:
                pickle.dump([], f)

    def loadData(self):
        try:
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
            return data if isinstance(data, list) else []
        except Exception:
            with open(self.file_path, "wb") as f:
                pickle.dump([], f)
            return []

    def saveData(self, student_list):
        if not isinstance(student_list, list):
            raise TypeError("saveData expects a list.")
        with open(self.file_path, "wb") as f:
            pickle.dump(student_list, f)

    def clearData(self):
        with open(self.file_path, "wb") as f:
            pickle.dump([], f)

    def clear(self):
        self.clearData()

    def backupData(self, suffix=".bak"):
        backup_path = self.file_path + suffix
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as src, open(backup_path, "wb") as dst:
                dst.write(src.read())
        return backup_path