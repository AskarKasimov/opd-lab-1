class Content():
    def __init__(self):
        self.content = dict()

        with open("textes.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            line_index = 0
            while line_index < len(lines):
                if ":" in lines[line_index]:
                    remember_index = line_index
                    number = 0
                    if lines[remember_index].strip()[:-1] in self.content.keys():
                        number += 1
                        self.content[lines[remember_index].strip()[
                            :-1]][0].append("")
                    else:
                        self.content[lines[remember_index].strip()[
                            :-1]] = [[""], 0]
                    line_index += 1
                    while True:
                        if line_index == len(lines) or ":" in lines[line_index]:
                            break
                        self.content[lines[remember_index].strip()[:-1]][0][number] \
                            += lines[line_index]
                        line_index += 1
                    self.content[lines[remember_index].strip()[:-1]][0][number] \
                        = self.content[lines[remember_index].strip()[:-1]][0][number].strip()
                else:
                    line_index += 1

    def get_content_by_filename(self, key: str) -> str:
        if len(self.content[key][0]) == 1:
            return self.content[key][0][0]
        value = self.content[key][0][self.content[key][1]]
        # if self.content[key][1] == len(self.content[key][0]) - 1:
        #     self.content[key][1] = 0
        # else:
        self.content[key][1] += 1
        return value


if __name__ == "__main__":
    content = Content()
    print(content.content)
