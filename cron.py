import time
import os


class Eraser:
    def __init__(self):
        self.DIRS = [os.path.join(os.getcwd(), 'app', 'uploads'), os.path.join(os.getcwd(), 'app', 'downloads')]
        self.delay = 3
        self.files = {}

    def run(self):
        while True:
            self.find_new()
            time.sleep(self.delay)
            print('...5 minutes passed...')
            self.count_values()
            self.remove_dead()

    def find_new(self):
        for directory in self.DIRS:
            for address, dirs, files in os.walk(directory):
                # find new files
                for file in files:
                    path = address+'/'+file
                    if path not in self.files:
                        self.files[path] = 5
                        print('Added new file {}'.format(file))

    def count_values(self):
        for key in self.files.keys():
            self.files[key] -= 5

    def remove_dead(self):
        # remove dead files
        to_del = []
        for key, value in self.files.items():
            print(key, value)
            if value <= 0:
                os.remove(key)
                to_del.append(key)
                print('File {} was removed'.format(key))

        for key in to_del:
            del self.files[key]


if __name__ == '__main__':
    Eraser().run()
