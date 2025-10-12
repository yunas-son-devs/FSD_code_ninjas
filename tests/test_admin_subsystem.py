from controllers.admin_subsystem import AdminSubsystem
from controllers.data_manager import DataManager

def main():
    dm = DataManager()
    admin = AdminSubsystem()

    # seed two students
    dm.saveData([
        {"studentID":"S0001","name":"A","subjects":[{"subjectID":"IS101","mark":85}]},
        {"studentID":"S0002","name":"B","subjects":[{"subjectID":"IS102","mark":45}]},
    ])

    print("All:", admin.view_all_students())
    print("Grouped:", admin.organise_by_grade())
    print("Pass/Fail:", admin.categorise_pass_fail())
    print("Remove S0002:", admin.remove_student("S0002"))
    print("Remove S404:", admin.remove_student("S404"))

if __name__ == "__main__":
    main()
