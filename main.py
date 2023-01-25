from datetime import datetime
import uuid


class Task:
    __all_tasks = []
    __incomplete_tasks = []
    __completed_tasks = []

    def __init__(self) -> None:
        self.updated_time = "N/A"
        self.status = False
        self.completed_time = "N/A"

    def create_task(self, name):
        self.name = name
        self.id = uuid.uuid1()
        now = datetime.now()
        self.created_time = now.strftime("%d/%m/%Y %H:%M:%S")
        self.__all_tasks.append(self)
        self.__incomplete_tasks.append(self)

    @classmethod
    def details(cls, lst):
        for i, ob in enumerate(lst):
            print("Task No        - ", i+1)
            print("ID             - ", ob.id)
            print("Task           - ", ob.name)
            print("Created time   - ", ob.created_time)
            print("Updated time   - ", ob.updated_time)
            print("Completed      - ", ob.status)
            print("Completed time - ", ob.completed_time, end="\n\n")

    def show_all_task(self):
        if Task.__all_tasks:
            self.details(Task.__all_tasks)
        else:
            print("No task to show\n")

    def show_incomplate(self):
        if Task.__incomplete_tasks:
            self.details(Task.__incomplete_tasks)
        else:
            print("No task to show\n")

    def show_complated(self):
        if Task.__completed_tasks:
            self.details(Task.__completed_tasks)
        else:
            print("No Completed Task\n")

    def chk_task(self, oparation):
        if Task.__all_tasks:
            print(f"Select Which Task to {oparation}\n")
            self.show_incomplate()
            return True
        else:
            print(f"No task to {oparation}\n")
            return False

    def update_task(self, t, name,):
        now = datetime.now()
        self.updated_time = now.strftime("%d/%m/%Y %H:%M:%S")

        Task.__all_tasks[t-1].name = name
        Task.__all_tasks[t-1].updated_time = self.updated_time

        Task.__incomplete_tasks[t-1].name = name
        Task.__incomplete_tasks[t-1].updated_time = self.updated_time

        print("\nTask Updated Successfully\n")

    def complete_task(self, t):
        now = datetime.now()
        self.updated_time = now.strftime("%d/%m/%Y %H:%M:%S")

        for ob in Task.__all_tasks:
            if ob == Task.__incomplete_tasks[t-1]:
                ob.status = True
                ob.completed_time = self.updated_time
                Task.__completed_tasks.append(ob)
                Task.__incomplete_tasks.pop(t-1)
                break

        print("\nTask Completed Successfully\n")


while True:
    print("1. Add New Task")
    print("2. Show All Task")
    print("3. Show Incomplete Tasks")
    print("4. Show Completed Tasks")
    print("5. Update Task")
    print("6. Mark A Task Completed")
    print("0. Terminate this Program")

    inp = int(input("Enter Option: "))
    print()
    task = Task()

    if inp == 1:
        tsk_name = input("Enter New Task: ")
        task.create_task(tsk_name)

        print("\nTask Created Successfully\n")

    elif inp == 2:
        task.show_all_task()
    elif inp == 3:
        task.show_incomplate()
    elif inp == 4:
        task.show_complated()
    elif inp == 5:
        chk = task.chk_task('Update')
        if chk:
            t = int(input("Enter Task No: "))
            name = input("Enter New Task: ")
            task.update_task(t, name)

    elif inp == 6:
        chk = task.chk_task('Complete')
        if chk:
            t = int(input("Enter Task No: "))
            task.complete_task(t)
    else:
        break
