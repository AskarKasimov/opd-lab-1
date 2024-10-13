class Content():
    """ class for parsing files' content """

    def __init__(self, path: str):
        """ path to source file needed """
        self.__content = dict()

        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            line_index = 0
            while line_index < len(lines):
                if ":" in lines[line_index]:
                    remember_index = line_index
                    number = 0
                    if lines[remember_index].strip()[:-1] in self.__content.keys():
                        number += 1
                        self.__content[lines[remember_index].strip()[
                            :-1]][0].append("")
                    else:
                        self.__content[lines[remember_index].strip()[
                            :-1]] = [[""], 0]
                    line_index += 1
                    while True:
                        if line_index == len(lines) or ":" in lines[line_index]:
                            break
                        self.__content[lines[remember_index].strip()[:-1]][0][number] \
                            += lines[line_index]
                        line_index += 1
                    self.__content[lines[remember_index].strip()[:-1]][0][number] \
                        = self.__content[lines[remember_index].strip()[:-1]][0][number].strip()
                else:
                    line_index += 1

    def get_content_by_filename(self, key: str) -> str:
        if len(self.__content[key][0]) == 1:
            return self.__content[key][0][0]
        value = self.__content[key][0][self.__content[key][1]]
        if self.__content[key][1] == len(self.__content[key][0]) - 1:
            self.__content[key][1] = 0
        else:
            self.__content[key][1] += 1
        return value
