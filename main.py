import sys
commands = []
with open("task.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in range(len(lines)):
        name = lines[line].split()[-2][3:]
        type = lines[line].split()[-1]
        print(lines[line].split())
        if line > 0 and len(lines[line-1].split()) > len(lines[line].split()):
            command = "cd " + "../" * (len(lines[line-1].split()) - len(lines[line].split()))
            commands.append(command)
        elif line > 0 and len(lines[line-1].split()) < len(lines[line].split()):
            command = f"cd {lines[line-1].split()[-2][3:]}"
            commands.append(command)
        if type == "каталог":
            command = f"mkdir {name}"
        elif type == "файл":
            command = f"touch {name}"
        else:
            print(f"unknown type: {type}")
            sys.exit()
        commands.append(command)

with open("solve.sh", "w") as file:
    for command in commands:
        file.write(command + "\n")
