"""
Задание 4-5-6.
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""


class Warehouse:
    __storage = []
    __summary = {}

    def push(self, equipment):
        if not isinstance(equipment, OfficeEquipment):
            raise Exception('Склад может принимать только оргтехнику')
        self.__storage.append(equipment)
        if self.__summary.get(equipment.category) is not None:
            self.__summary[equipment.category] += 1
        else:
            self.__summary.setdefault(equipment.category, 1)

    def report_items(self):
        for item in self.__storage:
            print(item)

    def report_total(self):
        for k, v in self.__summary.items():
            print(f'{k}: {v} шт')


class OfficeEquipment:
    def __init__(self, category: str, model: str, cost: float, sn: str):
        self.category = str(category)
        self.model = str(model)
        self.cost = float(cost)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.category} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, sn: str):
        self.is_colorful = is_colorful
        super().__init__('Принтер', model, cost, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model: str, cost: float, dpi: str, sn: str):
        self.dpi = dpi
        super().__init__('Сканер', model, cost, sn)


class Copier(OfficeEquipment):
    def __init__(self, model: str, cost: float, is_colorful: bool, dpi: str, velocity: int, sn: str):
        self.is_colorful = is_colorful
        self.dpi = dpi
        self.velocity = velocity
        super().__init__('МФУ', model, cost, sn)


if __name__ == '__main__':
    printer01 = Printer('Pantum P2200', 10300.12, True, 'N6SS549876548')
    printer02 = Printer('HP LaserJet M111a', 12600, False, 'FG64855SFG5')
    printer03 = Printer('Xerox Phaser 3020', 13600, False, 'FG64855SFG5')
    scanner01 = Scanner('Epson Perf V19', 15010, '4800x4800', '65482321FF5')
    scanner02 = Scanner('Canon LiDE 300', 17000.45, '2400x2400', '31313131FFF')
    copier01 = Copier('Canon i-sensys MF443dw', 26000.50, True, '4800x600', 8, 'FG8#HHHF')
    copier02 = Copier('HP LaserJet PRO MFP M1180n', 28500, False, '1200x1200', 22, '9BB654848554')

    warehouse = Warehouse()
    warehouse.push(printer01)
    warehouse.push(printer02)
    warehouse.push(printer03)
    warehouse.push(scanner01)
    warehouse.push(scanner02)
    warehouse.push(copier01)
    warehouse.push(copier02)

    warehouse.report_items()
    warehouse.report_total()
