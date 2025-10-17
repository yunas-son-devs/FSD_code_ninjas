# controllers/data_manager.py  (pickle variant)
import os
import pickle
from typing import List, Any

class DataManager:
    def __init__(self, file_path: str = "data/students.data"):
        self.file_path = file_path
        self.handleEmptyData()

    def handleEmptyData(self) -> None:
        """Create folder/file and ensure the file contains a pickled empty list."""
        folder = os.path.dirname(self.file_path) or "."
        os.makedirs(folder, exist_ok=True)
        # Create file or fix zero-length/corrupted file by seeding with []
        if (not os.path.exists(self.file_path)) or os.path.getsize(self.file_path) == 0:
            with open(self.file_path, "wb") as f:
                pickle.dump([], f)

    def loadData(self) -> List[Any]:
        """Load list of students (list) from pickle. Safe on corruption."""
        try:
            with open(self.file_path, "rb") as f:
                data = pickle.load(f)
            return data if isinstance(data, list) else []
        except Exception:
            # On error, repair file and return empty list
            with open(self.file_path, "wb") as f:
                pickle.dump([], f)
            return []

    def saveData(self, studentList: List[Any]) -> None:
        """Overwrite the file with the full student list."""
        with open(self.file_path, "wb") as f:
            pickle.dump(studentList, f)

    def clearData(self) -> None:
        """Reset file to an empty list."""
        with open(self.file_path, "wb") as f:
            pickle.dump([], f)

    def backupData(self, suffix: str = ".bak") -> str:
        """Copy the pickle file next to it and return the backup path."""
        backup_path = f"{self.file_path}{suffix}"
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as src, open(backup_path, "wb") as dst:
                dst.write(src.read())
        return backup_path
