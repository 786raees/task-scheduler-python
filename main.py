from app.scheduler import TaskScheduler
import datetime, logging

def main():
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        scheduler = TaskScheduler()

        # Retrieve data from the database

        # # Schedule tasks
        now = datetime.datetime.now()
        trigger_time = now + datetime.timedelta(minutes=15)
        scheduler.create_task("Cancel Worker Server", "C:/Users/Lenovo/Desktop/Server_Automation/script.bat", "", trigger_time)

        # Get all tasks
        # all_tasks = scheduler.get_all_tasks()
        # logging.info("All Scheduled Tasks:")
        # for task in all_tasks:
        #     task_info = f"Name: {task['Name']}\nExecutable: {task['Executable']}\nArguments: {task['Arguments']}\nTrigger: {task['Trigger']}\n"
        #     logging.info(task_info)

        # Disable a task
        scheduler.delete_task('Build Worker Server')
    except Exception as e:
        logging.error("An error occurred: %s", e)

if __name__ == "__main__":
    main()
