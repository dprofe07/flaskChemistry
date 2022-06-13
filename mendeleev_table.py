from element import Element
from exceptions import ElementNotFoundException, IncorrectElementNumberException


class MendeleevTable:
    lst = [
        Element(1, (1, 1, 1), 'H', False, 1.00795, (-1, 0, 1), 'водород', True, 2.1),
        Element(2, (1, 8, 1), 'He', False, 4.002602, (0,), 'гелий', False, 0.0),
        Element(3, (2, 1, 1), 'Li', True, 6.9412, (0, 1), 'литий', False, 0.99),
        Element(4, (2, 2, 1), 'Be', True, 9.01218, (0, 1, 2), 'бериллий', False, 1.57),
        Element(5, (2, 3, 1), 'B', False, 10.812, (-3, -1, 0, 1, 2, 3), 'бор', False, 2.04),
        Element(6, (2, 4, 1), 'C', False, 12.0108, (-4, -3, -2, -1, 0, 1, 2, 3, 4), 'углерод', True, 2.55),
        Element(7, (2, 5, 1), 'N', False, 14.0067, (-3, -2, -1, 0, 1, 2, 3, 4, 5), 'азот', True, 3.04),
        Element(8, (2, 6, 1), 'O', False, 15.9994, (-2, -1, -0.5, -0.3333333333333333, 0, 0.5, 1, 2), 'кислород', True,
                3.44),
        Element(9, (2, 7, 1), 'F', False, 18.9984, (-1, 0), 'фтор', True, 3.98),
        Element(10, (2, 8, 1), 'Ne', False, 20.179, (0,), 'неон', False, 0),
        Element(11, (3, 1, 1), 'Na', True, 22.98977, (0, 1), 'натрий', False, 0.98),
        Element(12, (3, 2, 1), 'Mg', True, 24.305, (0, 1, 2), 'магний', False, 1.31),
        Element(13, (3, 3, 1), 'Al', True, 26.98154, (0, 3), 'алюминий', False, 1.61),
        Element(14, (3, 4, 1), 'Si', False, 28.086, (-4, -3, -2, -1, 0, 1, 2, 3, 4), 'кремний', False, 1.9),
        Element(15, (3, 5, 1), 'P', False, 30.97376, (-3, -2, -1, 0, 1, 2, 3, 4, 5), 'фосфор', False, 2.19),
        Element(16, (3, 6, 1), 'S', False, 32.06, (-2, -1, 0, 1, 2, 3, 4, 5, 6), 'сера', False, 2.58),
        Element(17, (3, 7, 1), 'Cl', False, 35.453, (-1, 0, 1, 2, 3, 4, 5, 6, 7), 'хлор', True, 3.16),
        Element(18, (3, 8, 1), 'Ar', False, 39.948, (0,), 'аргон', False, 0.0),
        Element(19, (4, 1, 1), 'K', True, 39.0983, (0, 1), 'калий', True, 0.82),
        Element(20, (4, 2, 1), 'Ca', True, 40.08, (0, 2), 'кальций', False, 1.0),
        Element(21, (4, 3, 0), 'Sc', True, 44.9559, (0, 1, 2, 3), 'скандий', False, 1.36),
        Element(22, (4, 4, 0), 'Ti', True, 47.9, (0, 2, 3, 4), 'титан', False, 1.54),
        Element(23, (4, 5, 0), 'V', True, 50.9415, (0, 1, 2, 3, 4, 5), 'ванадий', False, 1.63),
        Element(24, (4, 6, 0), 'Cr', True, 51.996, (0, 1, 2, 3, 4, 6), 'хром', False, 1.66),
        Element(25, (4, 7, 0), 'Mn', True, 54.938, (-1, 0, 1, 2, 3, 4, 5, 6, 7), 'марганец', False, 1.55),
        Element(26, (4, 8, 0), 'Fe', True, 55.847, (0, 1, 2, 3, 4, 5, 6), 'железо', False, 1.83),
        Element(27, (4, 8, 0), 'Co', True, 58.9332, (0, 1, 2, 3, 4, 5), 'кобальт', False, 1.88),
        Element(28, (4, 8, 0), 'Ni', True, 58.7, (0, 1, 2, 3, 4), 'никель', False, 1.91),
        Element(29, (4, 1, 0), 'Cu', True, 63.546, (0, 1, 2, 3, 4), 'медь', False, 1.9),
        Element(30, (4, 2, 0), 'Zn', True, 65.38, (0, 2), 'цинк', False, 1.65),
        Element(31, (4, 3, 1), 'Ga', True, 69.72, (0, 1, 2, 3), 'галлий', False, 1.81),
        Element(32, (4, 4, 1), 'Ge', True, 72.59, (-4, 0, 1, 2, 3, 4), 'германий', False, 2.01),
        Element(33, (4, 5, 1), 'As', False, 74.9216, (-3, 0, 2, 3, 5), 'мышьяк', False, 2.18),
        Element(34, (4, 6, 1), 'Se', False, 78.96, (-2, 0, 2, 4, 6), 'селен', False, 2.55),
        Element(35, (4, 7, 1), 'Br', False, 79.904, (-1, 0, 1, 3, 4, 5, 7), 'бром', True, 2.96),
        Element(36, (4, 8, 1), 'Kr', False, 83.8, (0, 2), 'криптон', False, 3),
        Element(37, (5, 1, 1), 'Rb', True, 85.4678, (0, 1), 'рубидий', False, 0.82),
        Element(38, (5, 2, 1), 'Sr', True, 87.62, (0, 2), 'стронций', False, 1),
        Element(39, (5, 3, 0), 'Y', True, 88.9059, (0, 1, 2, 3), 'иттрий', False, 1.36),
        Element(40, (5, 4, 0), 'Zr', True, 91.22, (0, 1, 2, 3, 4), 'цирконий', False, 1.54),
        Element(41, (5, 5, 0), 'Nb', True, 92.9064, (-1, 0, 2, 3, 4, 5), 'ниобий', False, 1.63),
        Element(42, (5, 6, 0), 'Mo', True, 95.94, (-2, -1, 0, 1, 2, 3, 4, 5, 6), 'молибден', False, 1.66),
        Element(43, (5, 7, 0), 'Tc', True, 98.9062, (-3, -1, 0, 1, 2, 3, 4, 5, 6, 7), 'технеций', False, 1.55),
        Element(44, (5, 8, 0), 'Ru', True, 101.07, (-2, 0, 1, 2, 3, 4, 5, 6, 7, 8), 'рутений', False, 2.2),
        Element(45, (5, 8, 0), 'Rh', True, 102.9055, (-1, 0, 1, 2, 3, 4, 5, 6), 'родий', False, 2.28),
        Element(46, (5, 8, 0), 'Pd', True, 106.4, (0, 2, 4), 'палладий', False, 2.2),
        Element(47, (5, 1, 0), 'Ag', True, 107.868, (0, 1, 2, 3), 'серебро', False, 1.93),
        Element(48, (5, 2, 0), 'Cd', True, 112.41, (0, 2), 'кадмий', False, 1.69),
        Element(49, (5, 3, 1), 'In', True, 114.82, (0, 1, 2, 3), 'индий', False, 1.78),
        Element(50, (5, 4, 1), 'Sn', True, 118.69, (-4, 0, 2, 4), 'олово', False, 1.96),
        Element(51, (5, 7, 1), 'Sb', True, 121.75, (-3, 0, 3, 5), 'сурьма', False, 2.05),
        Element(52, (5, 6, 1), 'Te', False, 127.6, (-2, 0, 4, 5, 6), 'телур', False, 2.1),
        Element(53, (5, 7, 1), 'I', False, 126.9045, (-1, 0, 1, 3, 5, 7), 'иод', True, 2.66),
        Element(54, (5, 8, 1), 'Xe', False, 131.3, (0, 2, 4, 6, 8), 'ксенон', False, 2.6),
        Element(55, (6, 1, 1), 'Cs', True, 132.9054, (0, 1), 'цезий', False, 0.79),
        Element(56, (6, 7, 1), 'Ba', True, 137.33, (0, 2), 'барий', False, 0.89),
        Element(57, (6, 3, 0), 'La', True, 138.9, (0, 2, 3), 'лантан', False, 1.1),
        Element(58, (6, 3, 0), 'Ce', True, 140.1, (0, 2, 3, 4), 'церий', False, 1.12),
        Element(59, (6, 2, 0), 'Pr', True, 140.9, (0, 2, 3, 4), 'празеодим', False, 1.13),
        Element(60, (6, 3, 0), 'Nd', True, 144.2, (0, 2, 3), 'неодим', False, 1.14),
        Element(61, (6, 3, 0), 'Pm', True, 145.0, (0, 3), 'прометий', False, 1.13),
        Element(62, (6, 3, 0), 'Sm', True, 150.4, (0, 2, 3), 'самарий', False, 1.17),
        Element(63, (6, 3, 0), 'Eu', True, 151.9, (0, 2, 3), 'европий', False, 1.2),
        Element(64, (6, 3, 0), 'Gd', True, 157.3, (0, 1, 2, 3), 'гадолиний', False, 1.2),
        Element(65, (6, 3, 0), 'Tb', True, 158.9, (0, 1, 3, 4), 'тербий', False, 1.1),
        Element(66, (6, 3, 0), 'Dy', True, 162.5, (0, 2, 3), 'диспрозий', False, 1.22),
        Element(67, (6, 3, 0), 'Ho', True, 164.9, (0, 3), 'гольмий', False, 1.23),
        Element(68, (6, 3, 0), 'Er', True, 167.3, (0, 3), 'эрбий', False, 1.24),
        Element(69, (6, 3, 0), 'Tm', True, 168.9, (0, 2, 3), 'тулий', False, 1.25),
        Element(70, (6, 3, 0), 'Yb', True, 173.0, (0, 2, 3), 'иттербий', False, 1.1),
        Element(71, (6, 3, 0), 'Lu', True, 174.9, (0, 3), 'лютеций', False, 1.27),
        Element(72, (6, 4, 0), 'Hf', True, 178.49, (0, 2, 3, 4), 'гафний', False, 1.3),
        Element(73, (6, 5, 0), 'Ta', True, 180.9479, (-1, 0, 2, 3, 4, 5), 'тантал', False, 1.5),
        Element(74, (6, 6, 0), 'W', True, 183.85, (-2, -1, 0, 1, 2, 3, 4, 5, 6), 'вольфрам', False, 2.36),
        Element(75, (6, 7, 0), 'Re', True, 186.207, (-3, -1, 0, 1, 2, 3, 4, 5, 6, 7), 'рений', False, 1.9),
        Element(76, (6, 8, 0), 'Os', True, 190.2, (-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8), 'осмий', False, 2.2),
        Element(77, (6, 8, 0), 'Ir', True, 192.22, (-3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 'иридий', False, 2.2),
        Element(78, (6, 8, 0), 'Pt', True, 195.09, (0, 2, 4, 5, 6), 'платина', False, 2.28),
        Element(79, (6, 1, 0), 'Au', True, 107.868, (-1, 0, 1, 2, 3, 5), 'золото', False, 2.54),
        Element(80, (6, 2, 0), 'Hg', True, 200.59, (0, 1, 2, 4), 'ртуть', False, 2.0),
        Element(81, (6, 3, 1), 'Tl', True, 204.37, (0, 1, 3), 'таллий', False, 1.62),
        Element(82, (6, 4, 1), 'Pb', True, 207.2, (-4, 0, 2, 4), 'свинец', False, 2.33),
        Element(83, (6, 5, 1), 'Bi', True, 208.9, (-3, 0, 3, 5), 'висмут', False, 2.02),
        Element(84, (6, 6, 1), 'Po', True, 209.0, (-2, 0, 2, 4, 6), 'полоний', False, 2.0),
        Element(85, (6, 7, 1), 'At', False, 210.0, (-1, 0, 1, 3, 5), 'астат', False, 2.2),
        Element(86, (6, 8, 1), 'Rn', False, 222.0, (0, 2, 4, 6), 'радон', False, 2.2),
        Element(87, (7, 1, 1), 'Fr', True, 223.0, (0, 1), 'франций', False, 0.7),
        Element(88, (7, 2, 1), 'Ra', True, 226.0, (0, 2), 'радий', False, 0.9),
        Element(89, (7, 3, 0), 'Ac', True, 227.0, (0, 3), 'актиний', False, 1.1),
        Element(90, (7, 3, 0), 'Th', True, 232.0, (0, 2, 3, 4), 'торий', False, 1.3),
        Element(91, (7, 3, 0), 'Pa', True, 231.0, (0, 3, 4, 5), 'протактиний', False, 1.5),
        Element(92, (7, 3, 0), 'U', True, 238.0, (0, 3, 4, 5, 6), 'уран', False, 1.38),
        Element(93, (7, 3, 0), 'Np', True, 237.0, (0, 3, 4, 5, 6, 7), 'нептуний', False, 1.36),
        Element(94, (7, 3, 0), 'Pu', True, 244.0, (0, 3, 4, 5, 6, 7), 'плутоний', False, 1.28),
        Element(95, (7, 3, 0), 'Am', True, 243.0, (0, 2, 3, 4, 5, 6), 'америций', False, 1.13),
        Element(96, (7, 3, 0), 'Cm', True, 247.0, (0, 3, 4), 'кюрий', False, 1.28),
        Element(97, (7, 3, 0), 'Bk', True, 247.0, (0, 3, 4), 'берклий', False, 1.3),
        Element(98, (7, 3, 0), 'Cf', True, 251.0, (0, 2, 3, 4), 'калифорний', False, 1.3),
        Element(99, (7, 3, 0), 'Es', True, 252.0, (0, 2, 3), 'эйнштейний', False, 1.3),
        Element(100, (7, 3, 0), 'Fm', True, 257.0, (0, 2, 3), 'фермий', False, 1.3),
        Element(101, (7, 3, 0), 'Md', True, 258.0, (0, 2, 3), 'менделевий', False, 1.3),
        Element(102, (7, 3, 0), 'No', True, 259.0, (0, 2, 3), 'нобелий', False, 1.3),
        Element(103, (7, 3, 0), 'Lr', True, 262.0, (0, 3), 'лоуренсий', False, 1.291),
        Element(104, (7, 4, 0), 'Rf', True, 261.0, (0, 4), 'резерфордий', False, 0.0),
        Element(105, (7, 5, 0), 'Db', True, 262.0, (0, 3, 4, 5), 'дубний', False, 0.0),
        Element(106, (7, 6, 0), 'Sg', True, 266.0, (0, 6), 'сиборгий', False, 0.0),
        Element(107, (7, 7, 0), 'Bh', True, 269.0, (0, 7), 'борий', False, 0),
        Element(108, (7, 8, 0), 'Hs', True, 269.0, (0, 8), 'хассий', False, 0.0),
        Element(109, (7, 8, 0), 'Mt', False, 268.0, (0, 4), 'мейтнерий', False, 0.0),
        Element(110, (7, 8, 0), 'Ds', False, 271.0, (0, 8), 'дармштадтий', False, 0.0),
        Element(111, (7, 1, 0), 'Rg', False, 282.0, (0, 1), 'рентгений', False, 0.0),
        Element(112, (7, 2, 0), 'Cn', True, 285.0, (0, 2), 'коперниций', False, 0.0),
        Element(113, (7, 3, 1), 'Nh', False, 286.0, (0, 3), 'нихоний', False, 0.0),
        Element(114, (7, 4, 1), 'Fl', False, 289.0, (0, 4), 'флеровий', False, 0.0),
        Element(115, (7, 5, 1), 'Mc', False, 288.0, (0, 5), 'московий', False, 0.0),
        Element(116, (7, 6, 1), 'Lv', False, 293.0, (0, 6), 'ливерморий', False, 0.0),
        Element(117, (7, 7, 1), 'Ts', False, 294.0, (0, 7), 'теннессин', False, 0.0),
        Element(118, (7, 8, 1), 'Og', False, 294.0, (-1, 0, 1, 2, 4, 6), 'оганесон', False, 0.0),
    ]

    @staticmethod
    def from_name(name: str) -> Element:
        for i in MendeleevTable.lst:
            if i.ru_name == name:
                return i
        raise ElementNotFoundException(f'name={name}')

    @staticmethod
    def from_number(number: int) -> Element:
        if number > 118 or number < 1:
            raise IncorrectElementNumberException(f'number={number}')

        return MendeleevTable.lst[number - 1]

    @staticmethod
    def from_label(label: str) -> Element:
        for i in MendeleevTable.lst:
            if i.label == label:
                return i
        raise ElementNotFoundException(f'label={label!r}')

    @staticmethod
    def from_position(position: (int, int, int)):
        for i in MendeleevTable.lst:
            if i.position == position:
                return i
        raise ElementNotFoundException(f'position={position}')
