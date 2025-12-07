import numpy as np

# Lista de casos de prueba generados
casos_prueba = []

# n = 1 (10 casos aleatorios)
casos_1 = [
    {
        'n': 1,
        'conjunto': 1,
        'punto_inicial': np.array([12.489, 3.772]),
        'punto_final': np.array([6.114, 14.981]),
        'obstaculos': [np.array([17.442, 9.881])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 2,
        'punto_inicial': np.array([19.772, 0.514]),
        'punto_final': np.array([2.905, 7.450]),
        'obstaculos': [np.array([12.332, 11.773])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 3,
        'punto_inicial': np.array([3.221, 17.904]),
        'punto_final': np.array([14.771, 18.662]),
        'obstaculos': [np.array([7.944, 6.008])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 4,
        'punto_inicial': np.array([10.554, 12.332]),
        'punto_final': np.array([1.104, 9.882]),
        'obstaculos': [np.array([4.551, 16.772])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 5,
        'punto_inicial': np.array([0.992, 4.222]),
        'punto_final': np.array([18.004, 13.501]),
        'obstaculos': [np.array([9.442, 3.712])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 6,
        'punto_inicial': np.array([16.109, 15.771]),
        'punto_final': np.array([7.331, 4.197]),
        'obstaculos': [np.array([10.228, 19.003])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 7,
        'punto_inicial': np.array([4.771, 11.550]),
        'punto_final': np.array([13.884, 16.662]),
        'obstaculos': [np.array([0.884, 3.228])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 8,
        'punto_inicial': np.array([2.551, 18.661]),
        'punto_final': np.array([8.770, 1.332]),
        'obstaculos': [np.array([15.772, 7.115])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 9,
        'punto_inicial': np.array([11.552, 6.884]),
        'punto_final': np.array([3.004, 19.772]),
        'obstaculos': [np.array([5.442, 14.331])],
        'radio_seguro': 1.0
    },
    {
        'n': 1,
        'conjunto': 10,
        'punto_inicial': np.array([14.661, 8.115]),
        'punto_final': np.array([19.228, 2.772]),
        'obstaculos': [np.array([9.554, 17.884])],
        'radio_seguro': 1.0
    }
]

casos_prueba.extend(casos_1)


# n = 3 (10 casos aleatorios)
casos_3 = [
    {
        'n': 3,
        'conjunto': 1,
        'punto_inicial': np.array([12.884, 6.551]),
        'punto_final': np.array([3.114, 18.772]),
        'obstaculos': [
            np.array([8.442, 14.115]),
            np.array([17.332, 9.884]),
            np.array([4.771, 3.228])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 2,
        'punto_inicial': np.array([7.551, 1.442]),
        'punto_final': np.array([19.771, 12.554]),
        'obstaculos': [
            np.array([3.554, 17.662]),
            np.array([12.115, 8.442]),
            np.array([16.990, 4.331])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 3,
        'punto_inicial': np.array([4.884, 14.228]),
        'punto_final': np.array([18.441, 2.990]),
        'obstaculos': [
            np.array([9.772, 11.114]),
            np.array([13.220, 19.552]),
            np.array([6.115, 4.774])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 4,
        'punto_inicial': np.array([2.004, 10.551]),
        'punto_final': np.array([16.882, 17.114]),
        'obstaculos': [
            np.array([10.551, 6.332]),
            np.array([14.441, 12.551]),
            np.array([5.772, 18.115])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 5,
        'punto_inicial': np.array([5.332, 3.772]),
        'punto_final': np.array([12.995, 19.220]),
        'obstaculos': [
            np.array([2.551, 15.771]),
            np.array([8.442, 9.332]),
            np.array([17.771, 11.552])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 6,
        'punto_inicial': np.array([1.221, 11.990]),
        'punto_final': np.array([19.330, 3.551]),
        'obstaculos': [
            np.array([6.884, 13.114]),
            np.array([11.772, 7.442]),
            np.array([15.551, 2.882])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 7,
        'punto_inicial': np.array([8.551, 2.772]),
        'punto_final': np.array([3.554, 16.115]),
        'obstaculos': [
            np.array([12.332, 14.551]),
            np.array([5.772, 9.115]),
            np.array([17.115, 4.995])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 8,
        'punto_inicial': np.array([14.222, 9.114]),
        'punto_final': np.array([0.995, 4.772]),
        'obstaculos': [
            np.array([7.551, 12.332]),
            np.array([18.220, 10.001]),
            np.array([1.771, 17.882])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 9,
        'punto_inicial': np.array([17.551, 11.442]),
        'punto_final': np.array([2.772, 2.551]),
        'obstaculos': [
            np.array([9.551, 16.771]),
            np.array([4.774, 13.332]),
            np.array([14.115, 7.551])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 3,
        'conjunto': 10,
        'punto_inicial': np.array([3.554, 18.442]),
        'punto_final': np.array([15.772, 0.885]),
        'obstaculos': [
            np.array([11.442, 9.228]),
            np.array([6.995, 15.441]),
            np.array([19.114, 12.995])
        ],
        'radio_seguro': 1.0
    }
]

casos_prueba.extend(casos_3)


# n = 5 (10 casos aleatorios)
casos_5 = [
    {
        'n': 5,
        'conjunto': 1,
        'punto_inicial': np.array([12.552, 7.441]),
        'punto_final': np.array([2.884, 17.220]),
        'obstaculos': [
            np.array([4.114, 15.442]),
            np.array([10.551, 3.772]),
            np.array([6.995, 9.115]),
            np.array([15.220, 14.331]),
            np.array([18.771, 6.114])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 2,
        'punto_inicial': np.array([5.772, 13.332]),
        'punto_final': np.array([17.554, 1.551]),
        'obstaculos': [
            np.array([8.115, 12.551]),
            np.array([2.774, 7.441]),
            np.array([14.995, 10.332]),
            np.array([10.551, 17.662]),
            np.array([4.220, 3.552])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 3,
        'punto_inicial': np.array([1.442, 5.995]),
        'punto_final': np.array([19.772, 12.114]),
        'obstaculos': [
            np.array([6.551, 8.220]),
            np.array([11.332, 3.995]),
            np.array([16.220, 13.551]),
            np.array([7.995, 16.882]),
            np.array([3.551, 11.772])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 4,
        'punto_inicial': np.array([3.228, 14.551]),
        'punto_final': np.array([18.441, 8.551]),
        'obstaculos': [
            np.array([5.772, 10.115]),
            np.array([12.884, 6.662]),
            np.array([17.551, 3.331]),
            np.array([9.330, 18.220]),
            np.array([14.115, 12.995])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 5,
        'punto_inicial': np.array([7.551, 1.442]),
        'punto_final': np.array([14.772, 19.551]),
        'obstaculos': [
            np.array([10.551, 5.551]),
            np.array([2.551, 16.774]),
            np.array([12.995, 10.115]),
            np.array([17.772, 9.442]),
            np.array([4.441, 12.551])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 6,
        'punto_inicial': np.array([5.884, 9.990]),
        'punto_final': np.array([19.551, 4.772]),
        'obstaculos': [
            np.array([3.771, 7.551]),
            np.array([8.551, 14.772]),
            np.array([11.115, 5.228]),
            np.array([15.551, 16.551]),
            np.array([6.884, 12.331])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 7,
        'punto_inicial': np.array([3.220, 17.551]),
        'punto_final': np.array([12.551, 2.551]),
        'obstaculos': [
            np.array([9.115, 11.772]),
            np.array([14.551, 7.551]),
            np.array([6.331, 15.551]),
            np.array([17.772, 10.772]),
            np.array([4.551, 3.995])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 8,
        'punto_inicial': np.array([0.995, 9.551]),
        'punto_final': np.array([18.225, 15.772]),
        'obstaculos': [
            np.array([7.551, 6.772]),
            np.array([2.995, 12.115]),
            np.array([16.220, 3.995]),
            np.array([9.551, 18.114]),
            np.array([13.330, 9.772])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 9,
        'punto_inicial': np.array([10.551, 11.442]),
        'punto_final': np.array([2.551, 7.995]),
        'obstaculos': [
            np.array([4.551, 16.551]),
            np.array([12.772, 14.995]),
            np.array([7.551, 9.551]),
            np.array([17.330, 6.551]),
            np.array([14.115, 3.772])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 5,
        'conjunto': 10,
        'punto_inicial': np.array([2.551, 13.772]),
        'punto_final': np.array([19.551, 1.772]),
        'obstaculos': [
            np.array([5.551, 9.995]),
            np.array([11.551, 6.115]),
            np.array([15.772, 12.331]),
            np.array([3.772, 5.551]),
            np.array([17.551, 18.115])
        ],
        'radio_seguro': 1.0
    }
]

casos_prueba.extend(casos_5)


# n = 10 (10 casos aleatorios)
casos_10 = [
    {
        'n': 10,
        'conjunto': 1,
        'punto_inicial': np.array([12.332, 4.551]),
        'punto_final': np.array([1.225, 18.772]),
        'obstaculos': [
            np.array([3.772, 15.331]),
            np.array([7.551, 9.115]),
            np.array([12.115, 6.884]),
            np.array([16.772, 13.772]),
            np.array([9.551, 4.551]),
            np.array([14.442, 7.220]),
            np.array([5.331, 12.772]),
            np.array([18.220, 16.772]),
            np.array([2.551, 8.551]),
            np.array([11.772, 17.551])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 2,
        'punto_inicial': np.array([6.772, 13.551]),
        'punto_final': np.array([18.115, 3.551]),
        'obstaculos': [
            np.array([4.551, 8.115]),
            np.array([9.772, 14.551]),
            np.array([13.551, 6.882]),
            np.array([17.772, 11.551]),
            np.array([2.772, 3.995]),
            np.array([11.115, 9.995]),
            np.array([15.551, 16.220]),
            np.array([7.551, 5.551]),
            np.array([3.551, 17.551]),
            np.array([8.115, 12.115])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 3,
        'punto_inicial': np.array([3.995, 1.772]),
        'punto_final': np.array([17.551, 19.220]),
        'obstaculos': [
            np.array([8.772, 11.551]),
            np.array([14.551, 6.551]),
            np.array([10.551, 16.772]),
            np.array([6.551, 7.551]),
            np.array([12.995, 3.551]),
            np.array([17.220, 12.995]),
            np.array([5.551, 14.551]),
            np.array([9.115, 18.220]),
            np.array([3.551, 10.772]),
            np.array([15.772, 8.551])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 4,
        'punto_inicial': np.array([11.551, 17.772]),
        'punto_final': np.array([1.551, 3.772]),
        'obstaculos': [
            np.array([6.331, 14.551]),
            np.array([12.115, 9.772]),
            np.array([15.551, 5.995]),
            np.array([3.331, 16.331]),
            np.array([9.220, 11.995]),
            np.array([4.115, 8.772]),
            np.array([17.551, 13.115]),
            np.array([7.551, 3.115]),
            np.array([2.551, 19.551]),
            np.array([13.551, 17.772])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 5,
        'punto_inicial': np.array([0.995, 11.551]),
        'punto_final': np.array([19.551, 7.551]),
        'obstaculos': [
            np.array([3.995, 8.551]),
            np.array([14.551, 12.551]),
            np.array([5.772, 17.772]),
            np.array([10.772, 6.551]),
            np.array([8.551, 13.551]),
            np.array([17.551, 10.115]),
            np.array([1.995, 4.772]),
            np.array([12.551, 15.551]),
            np.array([6.551, 2.551]),
            np.array([16.772, 18.331])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 6,
        'punto_inicial': np.array([5.551, 5.551]),
        'punto_final': np.array([17.772, 17.772]),
        'obstaculos': [
            np.array([3.772, 11.115]),
            np.array([8.551, 9.551]),
            np.array([14.551, 10.995]),
            np.array([12.331, 14.551]),
            np.array([6.551, 17.551]),
            np.array([10.995, 4.331]),
            np.array([15.551, 6.551]),
            np.array([9.551, 2.995]),
            np.array([1.551, 8.551]),
            np.array([18.551, 11.551])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 7,
        'punto_inicial': np.array([12.551, 2.772]),
        'punto_final': np.array([3.772, 18.551]),
        'obstaculos': [
            np.array([10.772, 5.551]),
            np.array([5.551, 16.551]),
            np.array([15.772, 8.551]),
            np.array([7.551, 3.995]),
            np.array([13.115, 11.772]),
            np.array([2.331, 7.551]),
            np.array([18.331, 15.772]),
            np.array([9.772, 13.551]),
            np.array([6.551, 10.115]),
            np.array([11.551, 17.551])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 8,
        'punto_inicial': np.array([1.772, 18.551]),
        'punto_final': np.array([12.772, 1.772]),
        'obstaculos': [
            np.array([4.995, 9.551]),
            np.array([10.551, 14.551]),
            np.array([17.551, 6.331]),
            np.array([6.551, 12.551]),
            np.array([14.551, 17.551]),
            np.array([8.331, 3.551]),
            np.array([2.551, 14.995]),
            np.array([9.551, 18.115]),
            np.array([11.331, 4.551]),
            np.array([5.551, 8.115])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 9,
        'punto_inicial': np.array([10.551, 10.551]),
        'punto_final': np.array([1.772, 3.551]),
        'obstaculos': [
            np.array([14.115, 12.772]),
            np.array([9.551, 6.551]),
            np.array([7.551, 17.772]),
            np.array([17.551, 14.551]),
            np.array([3.551, 10.331]),
            np.array([11.551, 5.551]),
            np.array([15.772, 9.115]),
            np.array([2.551, 18.331]),
            np.array([6.551, 8.551]),
            np.array([12.551, 16.331])
        ],
        'radio_seguro': 1.0
    },
    {
        'n': 10,
        'conjunto': 10,
        'punto_inicial': np.array([0.551, 6.551]),
        'punto_final': np.array([19.115, 12.331]),
        'obstaculos': [
            np.array([5.995, 11.772]),
            np.array([14.551, 8.551]),
            np.array([18.551, 17.551]),
            np.array([3.772, 4.772]),
            np.array([11.551, 15.551]),
            np.array([7.551, 9.331]),
            np.array([9.772, 18.551]),
            np.array([13.551, 3.551]),
            np.array([2.551, 7.551]),
            np.array([4.551, 13.551])
        ],
        'radio_seguro': 1.0
    }
]

casos_prueba.extend(casos_10)

