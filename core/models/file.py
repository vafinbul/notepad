

class File:

    def __init__(self):
        self.file_name = ''

    def open(self, filename):
        # FIXME need to add GUI init
        self.file_name = open(filename)

    def close(self, filename):
        # FIXME need to add GUI termination and stuff
        self.close(filename)

    def save(self, filename):
        f = open(filename, 'w')
        f.write() # FIXME need to add some data written by user
        f.close()

    def write(self, filename):
        f = open(filename, 'w')

    # first_index - array
    # last_index - array
    # line - array
    def write(self, first_index, last_index, line):
        pass

    def read(self, filename):
        f = filename.open(filename, 'r')

    def get_name(self):
        pass

    def set_name(self, filename):
        pass