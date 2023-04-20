import random as rnd


def check_types(is_method, *types):  # проыерка типов переданных в метод
    def level1(func):
        def level2(*args, **kwargs):
            for i in args[int(is_method):]:
                if type(i) not in types:
                    raise TypeError(f"Args must be some of types {types}")
            result = func(*args, **kwargs)
            return result

        return level2

    return level1


class PrintableMixin:  # печать информации об обектах
    __trans_table = {'cpu': 'процессор', 'memory': 'память', 'sim_cards_list': 'список сим-кард'}

    def __make_trans(self, string):
        for i in self.__trans_table.keys():
            string = string.replace(i, self.__trans_table[i])
        return string

    def __str__(self):
        res = self.__class__.__name__
        bases = ['_' + res + '__']

        for i in self.__class__.__bases__:
            bases.append("_" + i.__name__ + "__")

        for i in self.__dict__:
            atr_name = i
            for x in bases:
                atr_name = atr_name.replace(x, '')
            res += ', ' + atr_name + ': ' + str(self.__dict__[i])

        return self.__make_trans(res)


class Computer(PrintableMixin):
    @check_types(True, float, int)
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    @check_types(True, float, int)
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    @check_types(True, float, int)
    def memory(self, memory):
        self.__memory = memory

    def make_computations(self):
        return (self.__cpu * rnd.random() + self.__memory * rnd.random()) / rnd.random()

    def __lt__(self, other):  # <
        if self.__memory < other.__memory:
            return True
        else:
            return False

    def __le__(self, other):  # <=
        if self.__memory <= other.__memory:
            return True
        else:
            return False

    def __eq__(self, other):  # ==
        if self.__memory == other.__memory:
            return True
        else:
            return False

    def __ne__(self, other):  # !=
        if self.__memory != other.__memory:
            return True
        else:
            return False

    def __gt__(self, other):  # >
        if self.__memory > other.__memory:
            return True
        else:
            return False

    def __ge__(self, other):  # >=
        if self.__memory >= other.__memory:
            return True
        else:
            return False


class Phone(PrintableMixin):
    __digits_in_numbers = [10, 11, 12]  # допустимое количество цифр в номере

    def __init__(self, *sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @staticmethod
    @check_types(False, str)
    def __calc_digits_in_numer(num):  # посчет цифр в числе
        return len(num)

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, sim_cards_list):
        if type(sim_cards_list) is not tuple:
            self.__sim_cards_list = (sim_cards_list,)
        else:
            self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number: int, call_number: str):
        if type(sim_card_number) != int or type(call_number) != str:
            raise TypeError("Send incorrect types of sim or number")

        if Phone.__calc_digits_in_numer(call_number) not in Phone.__digits_in_numbers:
            print("Такого номера не существует...")
        elif sim_card_number > len(self.__sim_cards_list) or sim_card_number == 0:
            print("Сим-карта не обнаружена...")
        else:
            print(f"Вызов с сим-карты {self.__sim_cards_list[sim_card_number - 1]} на номер {call_number}...")


class SmartPhone(Computer, Phone, PrintableMixin):

    def __init__(self, cpu, memory, *sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, *sim_card_list)

    @staticmethod
    @check_types(False, str)
    def use_gps(location):
        print(f"Прокладываем маршрут до {location}...")


ibm = Computer(832, 600)
nokia = Phone("beeline", "tele2")
samsung = SmartPhone(682, 4000, "O!", "Yota")
xiaomi = SmartPhone(732, 2500, "MTC", "MegaCom")
technic = [ibm, nokia, samsung, xiaomi]
print("Распечеать информацию об объектах:")
for i in technic:
    print(i)
print("__________________________________\n"
      "Опробовать методы каждого объекта:")
ibm.cpu = 700
ibm.memory = 300
print(ibm.make_computations())
nokia.call(2, "89648011149")
samsung.call(1, "0558474049")
print(samsung.make_computations())
samsung.use_gps("Sulaiman-Too")
xiaomi.call(1, "6641239878")
print(xiaomi.make_computations())
xiaomi.use_gps("Angarsk")
print("__________________________________\n"
      "Сравнение обектов:")
print(ibm > xiaomi)
print(xiaomi <= samsung)
print(samsung == ibm)
