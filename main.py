from container.container import Container
import sys
import time

def check_int(input: str) -> bool:
    """
     Check cast str to int.
    :param input: string
    :return: bool
    """
    for i in input:
        if 48 > ord(i) or ord(i) > 57:
            return False
    return True

def check_file(open_file: str) -> bool:
    """
     Check file access.
    :param open_file: checking file
    :return: bool
    """
    try:
        file = open(open_file, 'r')
        return True
    except Exception as ex:
        print("Error: could not open file {}".format(open_file))
        return False

def main(argv):
    container = Container()
    if len(argv) == 4:
        if argv[1] == "-r":
            output_file = open(argv[3], 'w')
            if (check_int(argv[2])) :
                container.generate(int(argv[2]), output_file)
            else:
                print("Error: Incorrect args.")
                return 1
        elif argv[1] == "-in":
            if check_file(argv[2]):
                input_file = open(argv[2], "r")
                try:
                    container.input(input_file)
                except Exception as ex:
                    "Error: Incorrect input"
                    return 1
                input_file.close()
                output_file = open(argv[3], "w")
                container.output(output_file)
                container.sort()
                output_file.write("\n\n===================================\n\nSorted container:\n\n")
                container.output(output_file)
            else:
                return 1
        else:
            print("The wrong command was entered.")
            return 1
    elif len(argv) == 5 and argv[1] == "-s":
        output_file = open(argv[2], "w");
        if check_int(argv[3]):
            container.generate(int(argv[3]), output_file)
            output_file = open(argv[4], "w");
            container.output(output_file)
            container.sort()
            output_file.write("\n\n===================================\n\nSorted container:\n\n")
            container.output(output_file)
        else:
            print("Error: Incorrect args.")
            return 1
    else:
        print("The wrong command was entered.")
        return 1
    output_file.write("Execution: {}".format(time.time() - start_time))
    output_file.close()

if __name__ == '__main__':
    start_time = time.time()
    main(sys.argv)

