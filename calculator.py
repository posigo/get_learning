class Calculator:

    __last_res = None

    def sum(self, *args):
        result = 0
        for arg in args:
            result += arg
        self.__last_res = result
        return result

    def print_last_res(self):
        print(self.__last_res)