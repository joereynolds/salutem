class Printer():

    def __init__(self, coloured = False):
        self.coloured = coloured

    def print_success(self, message):
        if self.coloured:
            return self.print_coloured_success(message)

        return self.print_plain_success(message)

    def print_failure(self, message, error):
        if self.coloured:
            return self.print_coloured_failure(message, error)

        return self.print_plain_failure(message, error)

    def print_plain_success(self, message):
        print('✔ ' + '[' + message + ']')

    def print_plain_failure(self, message, error):
        print('✖ ' + '[' + message + ']')
        print('Failed with the following reason(s):')
        print(error)

    def print_coloured_success(self, message):
        print('✔ WITH COLOUR ' + '[' + message + ']')

    def print_coloured_failure(self, message, error):
        print('✖ WITH COLOUR ' + '[' + message + ']')
        print('Failed with the following reason(s):')
        print(error)
