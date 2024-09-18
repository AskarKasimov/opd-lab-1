import sys
import logging
from task2.main import Content

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
commands = []
content = Content()

with open("task1.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line_index in range(len(lines)):
        this_line = lines[line_index]
        this_name = lines[line_index].split()[-2][3:]
        this_type = lines[line_index].split()[-1]

        prev_line = lines[line_index-1]
        prev_name = lines[line_index-1].split()[-2][3:]

        if line_index > 0 and len(prev_line.split()) > len(this_line.split()):
            commands.append("cd " +
                            "../" * (len(prev_line.split()) - len(this_line.split())))
        elif line_index > 0 and len(prev_line.split()) < len(this_line.split()):
            commands.append(f"cd {prev_name}")

        if this_type == "каталог":
            commands.append(f"mkdir {this_name}")
        elif this_type == "файл":
            commands.append(f"touch {this_name}")
            try:
                commands.append(
                    f"echo -e '{content.get_content_by_filename(this_name).replace("\n", "\\n")}' > {this_name}")
            except KeyError:
                logging.info(f"File not found: {this_name}")
        else:
            logging.error(f"Unknown type in parsed file: {this_type}")
            sys.exit()

with open("solve.sh", "w", encoding="utf-8") as file:
    for command in commands:
        file.write(command + "\n")
