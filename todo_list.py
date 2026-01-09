class TodoList:
    def __init__(self):
        self.tasks = []  # In-memory storage

    def add_task(self, description):
        task = {
            'id': len(self.tasks) + 1,
            'description': description.strip(),
            'completed': False
        }
        self.tasks.append(task)
        print(f"Added task #{task['id']}: {task['description']}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        print("\nYour Tasks:")
        for task in self.tasks:
            status = "[COMPLETE]" if task['completed'] else "[PENDING]"
            line = f"{status} [{task['id']}] {task['description']}"
            if task['completed']:
                line = f"~~{line}~~"
            print(line)
        print()

    def complete_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                print(f"Marked task #{task_id} as complete!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                self.tasks.pop(i)
                print(f"Deleted task #{task_id}!")
                return
        print("Task not found!")

def main():
    todo = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks") 
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            desc = input("Enter task description: ")
            if desc:
                todo.add_task(desc)
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            try:
                tid = int(input("Enter task ID to complete: "))
                todo.complete_task(tid)
            except ValueError:
                print("Invalid ID!")
        
        elif choice == '4':
            try:
                tid = int(input("Enter task ID to delete: "))
                todo.delete_task(tid)
            except ValueError:
                print("Invalid ID!")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
