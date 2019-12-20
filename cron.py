import time
import os


class Eraser:
    def __init__(self):
        self.delay = 300
        self.files = {}
        self.dirs = {}

    def run(self):
        while True:
            self.find_new()
            time.sleep(self.delay)
            self.count_values()
            self.remove_dead()

    def find_new(self):
        for directory in ['uploads', 'downloads']:
            for address, dirs, files in os.walk(directory):
                # find new files
                for file in files:
                    path = address+'/'+file
                    if path not in self.files:
                        self.files[path] = 60
                        print('Added new file {}'.format(file))

                # find new directories
                for dir in dirs:
                    path = address+'/'+dir
                    if path not in self.dirs and len(os.listdir(path)) == 0:
                        self.dirs[path] = 60
                        print('Added new dir {}'.format(dir))

    def count_values(self):
        if self.files.values():
            for val in self.files.values():
                val -= 5
        if self.dirs.values():
            for val in self.dirs.values():
                val -= 5

    def remove_dead(self):
        # remove dead files
        for key, value in self.files.items():
            if value <= 0:
                os.remove(key)
                del self.files[key]
                print('File {} was removed'.format(key))

        # remove empty folders
        for key, val in self.dirs.items():
            if val <= 0:
                os.rmdir(dir)
                del self.dirs[dir]
                print('Dir {} was removed'.format(dir))


if __name__ == '__main__':
    Eraser().run()
