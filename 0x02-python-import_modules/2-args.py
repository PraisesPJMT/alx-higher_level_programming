#!/usr/bin/python3
if __name__ == "__main__":
    import sys


    def print_arguments(argv):
        if len(argv) == 1:
            print('0 arguments.')
        else:
            print('{} arguments:'.format(len(argv) - 1))
            for i in range(len(argv) - 1):
                print('{}: {}'.format((i + 1), argv[i + 1]))

    print_arguments(sys.argv)
