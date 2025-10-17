from controllers.data_manager import DataManager

def test_data_manager():
    dm = DataManager("students.data")
    dm.handleEmptyData()
    print("Initial load:", dm.loadData())   # expect []

    sample = [{
        "studentID": "S0001",
        "name": "Test User",
        "email": "test@example.com",
        "password": "Abcde123",
        "subjects": [{"subjectID": "IS101", "mark": 85, "grade": "HD"}]
    }]
    dm.saveData(sample)
    print("After save:", dm.loadData())
    print("OK ✓")

if __name__ == "__main__":
    test_data_manager()
