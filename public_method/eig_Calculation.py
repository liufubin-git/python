import numpy
import math


class EigCalculation(object):
    """特征向量计算方法"""
    def __init__(self):
        pass

    @staticmethod
    def eig_calculation(eig_list):
        # numpy.linalg.eig计算方阵的特征值和右特征向量。
        w, v = numpy.linalg.eig(eig_list)
        w.tolist()
        condition_number = math.sqrt(max(w)/min(w))
        print(condition_number)


list1 = [[1.0000, 0.7042, 0.5061, 0.3143, -0.0807],
         [0.7042, 1.0000, 0.4090, 0.1267, -0.0851],
         [0.5061, 0.4090, 1.0000, 0.1958, -0.0636],
         [0.3143, 0.1267, 0.1958, 1.0000, 0.0856],
         [-0.0807, -0.0851, -0.0636, 0.0856, 1.0000]]
calmethod = EigCalculation()
calmethod.eig_calculation(list1)
