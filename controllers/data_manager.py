# controllers/data_manager.py  — simple pickle version
import os
import pickle

class DataManager:
    def __init__(self, file_path="data/students.data"):
        self.file_path = file_path
        self._make_file_ready()

    def _make_file_ready(self):
        """Make sure the folder exists and the file is a valid pickle list."""
        folder = os.path.dirname(self.file_path) or "."
        os.makedirs(folder, exist_ok=True)
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            # start the file with an empty list so pickle can read it later
            with open(self.file_path, "wb") as f:
                pickle.dump([], f)

    def loadData(self):
        """Return the list of students (or [] if something goes wrong)."""
        try:
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
            return data if isinstance(data, list) else []
        except Exception:
            # if file is corrupted, reset to []
            with open(self.file_path, "wb") as f:
                pickle.dump([], f)
            return []

    def saveData(self, student_list):
        """Save (overwrite) the full list. Return True if successful, False otherwise."""
        try:
            if not isinstance(student_list, list):
                raise TypeError("saveData expects a list (e.g., list of dicts).")
            with open(self.file_path, "wb") as f:
                pickle.dump(student_list, f)
            return True  # 
        except Exception as e:
            print(f"Error saving data: {e}")
            return False  # 

    def clearData(self):
        """Clear all students (set the file to [])."""
        with open(self.file_path, "wb") as f:
            pickle.dump([], f)

    def backupData(self, suffix=".bak"):
        """Create a simple backup next to the main file."""
        backup_path = self.file_path + suffix
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as src, open(backup_path, "wb") as dst:
                dst.write(src.read())
        return backup_path