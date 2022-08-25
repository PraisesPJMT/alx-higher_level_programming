#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv


    def print_arguments(arg_array):
        if len(arg_array) == 1:
            print('0 arguments.')
        else:
            print('{} arguments:'.format(len(arg_array) - 1))
            for i in range(len(arg_array) - 1):
                print('{}: {}'.format((i + 1), arg_array[i + 1]))

    print_arguments(argv)
