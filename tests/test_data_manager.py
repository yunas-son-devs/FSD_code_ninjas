from controllers.data_manager import DataManager

def main():
    dm = DataManager()  # uses data/students.data

    # 1) start clean
    dm.clearData()
    print("After clear:", dm.loadData())  # expect []

    # 2) save a small list
    sample = [
        {"studentID": "S0001", "name": "Test User",
         "subjects": [{"subjectID": "IS101", "mark": 85}]}
    ]
    dm.saveData(sample)

    # 3) read back
    print("After save:", dm.loadData())   # expect the same list

if __name__ == "__main__":
    main()
