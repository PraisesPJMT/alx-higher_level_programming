#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(argv) == 1:
        print('0 arguments.')
    elif len(argv) == 2:
        print('1 argument:')
    else:
        print('{} arguments:'.format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print('{}: {:s}'.format((i + 1), argv[i + 1]))
