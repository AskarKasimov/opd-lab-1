import sys
import logging
from textes import Content
from task2 import Rights

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
commands = []
content = Content("textes.txt")
rights = Rights("task2.txt")
files = []
dirs = []

with open("task1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line_index in range(len(lines)):
        this_line = lines[line_index]
        this_name = lines[line_index].split()[-2][3:]
        this_type = lines[line_index].split()[-1]

        prev_line = lines[line_index-1]
        prev_name = lines[line_index-1].split()[-2][3:]

        if this_type == "каталог":
            dirs.append(this_name)
            commands.append(f"mkdir {this_name}")
        elif this_type == "файл":
            files.append(this_name)
            commands.append(f"touch {this_name}")
            try:
                a = content.get_content_by_filename(
                    this_name.split("/")[-1]).replace("\n", "\\n")
                commands.append(
                    f"echo -e '{a}' >{this_name}")
            except KeyError:
                logging.info(f"File content not found: {this_name}")
        else:
            logging.error(f"Unknown type in parsed file: {this_type}")


commands.extend([x.strip() for x in open(
    "hardcode3.sh", "r", encoding="utf-8").readlines()])

commands.extend([x.strip() for x in open(
    "hardcode4.sh", "r", encoding="utf-8").readlines()])

files.sort(key=lambda x: (len(x.split("/")), x), reverse=True)
for file in files:
    a = rights.get_rights_by_filename(file.split("/")[-1])
    commands.append(
        f"chmod {a} {file}")

dirs.sort(key=lambda x: (len(x.split("/")), x), reverse=True)
for dir in dirs:
    a = rights.get_rights_by_filename(dir.split("/")[-1])
    commands.append(
        f"chmod {a} {dir}")

commands.extend([x.strip() for x in open(
    "hardcode5.sh", "r", encoding="utf-8").readlines()])

with open("solve.sh", "w", encoding="utf-8") as file:
    for command in commands:
        file.write(command + "\n")
