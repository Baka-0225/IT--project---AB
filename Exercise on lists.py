
task = ["Doing my laundry", "Studying for math test", "Finishing biology lab report"]
print(task)
print("Press 1 to a
task = ["Doing my laundry", "Studying for math test", "Finishing biology lab report"]
print(task)
print("Press 1 to add a task")
print("Press 2 to remove a task")
print("Press 3 to clear the to do list.")

def command1(task):
     task.append(input("Add task: "))
     print(task)
def command2(task):
     print("Which task do you want to delete? ")
     task.remove(input())
     print(task)
def command3(task):
     task.clear()
     print("You have nothing to do!")

inp = input("Command: ")

if int(inp) == 1:
     command1(task)
elif int(inp) == 2:
     command2(task)
elif int(inp) == 3:
     command3(task).