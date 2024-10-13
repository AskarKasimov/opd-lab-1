import logging


class Rights():
    """ class for parsing files' permissions """

    def __init__(self, path: str):
        """ path to source file needed """
        self.__rights = dict()

        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                file = line.split(":")[0]
                permissions = " ".join(line.split(":")[1:]).strip()
                if len(permissions) == 3:
                    self.__rights[file] = permissions
                else:
                    logging.error("Incorrect source file with permissions. Just chmod values needed: 000-777")

    def get_rights_by_filename(self, key: str):
        return self.__rights[key]
