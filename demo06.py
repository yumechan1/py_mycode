todos = open("todos.txt", "a", encoding="utf8")

print("一个事情！", file=todos)
print("第二个事情！", file=todos)
todos.close()
