class Printer():

    COLOUR_MESSAGE = '\033[0;33m'
    COLOUR_SUCCESS = '\033[0;32m'
    COLOUR_FAILURE = '\033[0;31m'
    COLOUR_RESET = '\033[0m'

    def __init__(self, coloured=False):
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
        print('✔ [{}]'.format(message))

    def print_plain_failure(self, message, error):
        print('✖ [{}]'.format(message))
        print('Failed with the following reason(s):')
        print(error)

    def print_coloured_success(self, message):
        check = '{}✔{} [{}]'.format(self.COLOUR_SUCCESS, self.COLOUR_RESET, message)
        print(check)

    def print_coloured_failure(self, message, error):
        check  = '{}✖{} [{}]'.format(self.COLOUR_FAILURE, self.COLOUR_RESET, message)
        prompt = '{}Failed for the following reason(s):{}'.format(self.COLOUR_MESSAGE, self.COLOUR_FAILURE)

        print(check)
        print(prompt)
        print(error)
        print(self.COLOUR_RESET)
