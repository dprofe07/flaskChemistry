from exceptions import IncorrectOrbitalNameException


class Element:
    """Класс химического элемента"""

    def __init__(
            self, number: int, position: (int, int, int),
            label: str, is_metal: int, atomic_mass: float,
            possible_oxidstates: tuple,
            ru_name: str, is_paired_simple=False,
            electroneg: float = -1
    ):
        self.number = number
        self.position = position
        self.label = label
        self.possible_oxidstates = possible_oxidstates
        self.is_metal = is_metal
        self.atomic_mass = atomic_mass
        self.is_paired_simple = is_paired_simple
        self.electroneg = electroneg
        self.ru_name = ru_name
        self.Z = 0

    def __repr__(self):
        return (
            f'{self.__class__.__name__}({self.number}, {self.position}, '
            f'{self.label!r}, {self.is_metal}, {self.atomic_mass}, '
            f'{self.possible_oxidstates}, {self.ru_name!r}, {self.is_paired_simple}, '
            f'{self.electroneg})'
        )

    def count_pne(self):
        return self.protones_count(), self.neutrons_count(), self.electrons_count()

    def el_formula(self):
        s = ''

        gr = self._get_electron_list()

        types_of_orbitals = ['s', 'p', 'd', 'f']

        for i in range(len(gr)):
            for j in range(len(gr[i])):
                if gr[i][j] == 0:
                    break
                s += f'{i + 1}{types_of_orbitals[j]}'
                s += f'<sup>{gr[i][j]}</sup>'

        return s

    def el_schema(self):
        s = ''
        if self.Z != 0:
            s += '<big>[</big>'
        s += f'{self.label}{{+{self.protones_count()}}} '

        gr = self._get_electron_list()

        for i in gr:
            a = 0
            for j in i:
                a += j
            if a != 0:
                s += f')<sub>{a}</sub> '

        if self.Z != 0:
            s += f'<big>]</big><sup>{"+" if self.Z > 0 else "-"}{self.Z}</sup>'

        return s

    def protones_count(self):
        return self.number

    def neutrons_count(self):
        return int(self.atomic_mass - self.protones_count())

    def electrons_count(self):
        return self.protones_count()

    def _get_electrons_on_orbital(self, orbital_name: str):
        number_from_which_starts_orbital = {
            "1s": 1,
            "2s": 3,
            "2p": 5,
            "3s": 11,
            "3p": 13,
            "4s": 19,
            "3d": 21,
            "4p": 31,
            "5s": 37,
            "4d": 39,
            "5p": 49,
            "6s": 55,
            "4f": 58,
            "5d": 72,
            "6p": 81,
            "7s": 87,
            "5f": 90,
            "6d": 104,
            "7p": 113
        }[orbital_name]

        max_on_orbital = {
            's': 2,
            'p': 6,
            'd': 10,
            'f': 14
        }.get(orbital_name[1])
        if max_on_orbital is None:
            raise IncorrectOrbitalNameException(orbital_name[1])

        result = self.electrons_count() - (number_from_which_starts_orbital - 1)

        if result > max_on_orbital:
            result = max_on_orbital
        elif result < 0:
            result = 0
        print(f'call for _get_elecgtrons_for_orbital({orbital_name!r}) returns {result}')
        return result

    def _get_electron_list(self):
        res = [[], [], [], [], [], [], []]

        types_of_orbital = 'spdf'

        for num in range(7):
            for symb in types_of_orbital:
                res[num].append(self._get_electrons_on_orbital(f"{num + 1}{symb}"))
                if num == types_of_orbital.index(symb) or num == 5 and symb == 'd' or num == 6 and symb == 'p':
                    break

        if self.number >= (57 - 1):
            res[4][2] += 1
        if self.number >= (89 - 1):
            res[5][2] += 1

        if self.number == 24:
            res[2][2] = 5
            res[3][0] = 1
        elif self.number == 29:
            res[2][2] = 10
            res[4][0] = 1
        elif self.number == 42:
            res[3][2] = 5
            res[4][0] = 1
        elif self.number == 44:
            res[3][2] = 7
            res[4][0] = 1
        elif self.number == 45:
            res[3][2] = 8
            res[4][0] = 1
        elif self.number == 46:
            res[3][2] = 10
            res[4][0] = 0
        elif self.number == 47:
            res[3][2] = 10
            res[4][0] = 1
        elif self.number == 78:
            res[4][2] = 9
            res[5][0] = 1
        elif self.number == 79:
            res[4][2] = 10
            res[5][0] = 1
        elif self.number == 110:
            res[5][2] = 9
            res[6][0] = 1
        elif self.number == 111:
            res[5][2] = 10
            res[6][0] = 1

        return res

    def pretty_pne(self):
        p, n, e = self.count_pne()

        return f'{p}p<sup>+</sup>, {n}n<sup>0</sup>, {e}e<sup>-</sup>'

    def pretty_position(self):
        p, g, sg = self.position

        return f'{p}-й период, {g}-ая группа, {"главная" if sg else "побочная"} подгруппа'
