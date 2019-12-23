import time
import os


class Eraser:
    def __init__(self):
        self.delay = 300
        self.files = {}

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

    def count_values(self):
        if self.files.values():
            for val in self.files.values():
                val -= 5

    def remove_dead(self):
        # remove dead files
        for key, value in self.files.items():
            if value <= 0:
                os.remove(key)
                del self.files[key]
                print('File {} was removed'.format(key))


if __name__ == '__main__':
    Eraser().run()
