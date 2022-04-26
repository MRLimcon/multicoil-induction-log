import numpy as np
import pandas as pd
import sqlite3 as sql
import pyhank


def test_hankel_transform():
    init_test = np.arange(0, 20, 0.1)
    func = np.cos(init_test)
    results = pyhank.one_shot.qdht(init_test, func, 0)

    plt.plot(init_test, func)
    plt.show()
    inverse = pyhank.one_shot.iqdht(results[0], results[1])
    plt.plot(results[0], results[1])
    plt.show()
