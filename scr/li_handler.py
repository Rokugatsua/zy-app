import config, os

class Ul:
    class file:
        def __init__(self, file_extension):
            self.file_extension = file_extension

        def chose_dir(self):
            dirs = {
                ".csv":"csv",
                ".xml":"xml"
            }
            return dirs[self.file_extension]

        def li(self):
            li = []
            dir_to_watch = os.path.join(config.cfgDir.FileDir, str(self.chose_dir()))

            for r, d, f in os.walk(dir_to_watch):
                for files in f:
                    if self.file_extension in files:
                        li.append(files)

            return li

    class db:
        def __init__(self, file_extension):
            self.file_extension = file_extension

        def li(self):
            li = []
            dir_to_watch = config.cfgDir.DbDir

            for r, d, f in os.walk(dir_to_watch):
                for files in f:
                    if self.file_extension in files:
                        li.append(files)
            return li



