import timeit

from conatiners import Container
import sys

if __name__ == '__main__':
    cont = Container()
    start_time = timeit.default_timer()

    try:
        if len(sys.argv) != 5:
            raise IndexError('Incorrect number of CL params')
        if sys.argv[1] == '-f':
            cont.input_file(sys.argv[2])
            cont.write_file(sys.argv[3])
            cont.heap_sort()
            cont.write_file(sys.argv[4])
        elif sys.argv[1] == '-n':
            cont.random_in(int(sys.argv[2]))
            cont.write_file(sys.argv[3])
            cont.heap_sort()
            cont.write_file(sys.argv[4])
        else:
            print('Incorrect command')
    except IndexError as ex:
        print(ex.__str__())
    except ValueError as ex:
        print(ex.__str__())
    except IOError:
        print('Incorrect files')
    except Exception:
        print('Something went wrong')

    print(timeit.default_timer() - start_time)
