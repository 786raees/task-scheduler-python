import win32com.client

class TaskScheduler:
    def __init__(self):
        self.scheduler = win32com.client.Dispatch('Schedule.Service')
        self.scheduler.Connect()

    def create_task(self, task_name, executable_path, arguments, trigger):
        root_folder = self.scheduler.GetFolder('\\')
        task_definition = self.scheduler.NewTask(0)
        task_definition.RegistrationInfo.Description = task_name

        task_trigger = task_definition.Triggers.Create(1)
        task_trigger.StartBoundary = trigger

        action = task_definition.Actions.Create(0)
        action.Path = executable_path
        action.Arguments = arguments

        root_folder.RegisterTaskDefinition(
            task_name,
            task_definition,
            6,  # TASK_CREATE_OR_UPDATE
            '', '',  # User and password
            0  # TASK_LOGON_INTERACTIVE_TOKEN
        )

    def get_all_tasks(self):
        task_folder = self.scheduler.GetFolder('\\')
        task_collection = task_folder.GetTasks(0)

        all_tasks = []
        for task in task_collection:
            task_info = task.Definition.RegistrationInfo
            task_trigger = task.Definition.Triggers[0]
            task_dict = {
                'Name': task.Name,
                'Executable': task.Definition.Actions[0].Path,
                'Arguments': task.Definition.Actions[0].Arguments,
                'Trigger': task_trigger.StartBoundary
            }
            all_tasks.append(task_dict)

        return all_tasks

    def toggle_task(self, task_name, enable=True):
        task_folder = self.scheduler.GetFolder('\\')
        try:
            task = task_folder.GetTask(task_name)
            task.Enabled = enable
        except Exception as e:
            print("Error toggling task:", e)

    def run_task(self, task_name):
        task_folder = self.scheduler.GetFolder('\\')
        try:
            task = task_folder.GetTask(task_name)
            if task.Enabled:
                task_run = task.Run('')
            else:
                print("Task is disabled and cannot be run.")
        except Exception as e:
            print("Error running task:", e)

    def delete_task(self, task_name):
        task_folder = self.scheduler.GetFolder('\\')
        try:
            task_folder.DeleteTask(task_name, 0)
        except Exception as e:
            print("Error deleting task:", e)
