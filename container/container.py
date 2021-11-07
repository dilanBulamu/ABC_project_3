from objects.number import Number

MAX_CONTAINER_SIZE = 10000
class Container:
    def __init__(self):
        """
        Constructor.
        """
        self.__length = 0
        self.__container = list()

    def generate(self, size: int, output_file):
        """
        Create container with random numbers.
        :param size: container capasity.
        :param output_file: file to write generated numbers params.
        :return:
        """
        if (size > MAX_CONTAINER_SIZE):
            return 1
        output_file.write("{}\n".format(size))
        for i in range(size):
            number = Number.static_generate()
            self.__container.append(number)
            output_file.write(str(number))
            self.__length += 1
        return 0

    def input(self, input_file):
        """
        Create container bu params from input file.
        :param input_file:
        :return:
        """
        data = input_file.readline().split('\n')[0]
        try:
            if (int(data) > MAX_CONTAINER_SIZE or int(data) <= 0):
                print("Error: size is out of range")
                return 1
            for i in range(int(data)):
                number = Number.static_input(input_file)
                if number == None:
                    print("Error with {} element".format(i + 1))
                    continue
                self.__container.append(number)
                self.__length += 1
        except Exception as ex:
            print("Error: Incorrect input")
            return 1
        return 0

    def output(self, output_file):
        """
        Write the contents of the container to the output file.
        :param output_file:
        :return:
        """
        output_file.write("Container contains {} elements.\n".format(self.__length))
        for i in range(self.__length):
            number = self.__container[i]
            output_file.write("[{}] - ".format(i + 1))
            number.output(output_file)


    def sort(self):
        """
        Sort container elements (straight merge).
        :return:
        """
        self.__container = Container.straight_merge(self.__container)

    @staticmethod
    def straight_merge(container):
        if len(container) < 2:
            return container[:]
        else:
            middle = int(len(container) / 2)
            left = Container.straight_merge(container[:middle])
            right = Container.straight_merge(container[middle:])
            return Container.merge(left, right)

    @staticmethod
    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i].cast_to_double() < right[j].cast_to_double():
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result