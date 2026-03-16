from creation.array_creation import array, zeros, ones, eye
from statistic.stats import mean, var, std
from exceptions.errors import DimensionMismatchError, NonNumericDataError, InvalidShapeError, InvalidOperationError
from core.ndarray import Array

def main():
    # a1 = array([1,2,3])
    # # print(a1)

    # a2 = array([[1,2],[3,4]])
    # # print(a2)

    # z = zeros((2,2,2))
    # # print(z)

    # o = ones((3,2))
    # print(o)

    # e = eye(3)
    # # print(e)

    # a = array([[1,2,3],[4,5,6]])

    # print("Array:")
    # print(a)

    # print("\nMean:")
    # print(mean(a))

    # print("\nVariance:")
    # print(var(a))

    # print("\nStandard Deviation:")
    # print(std(a))

    try:
        raise DimensionMismatchError()
    except DimensionMismatchError as e:
        print("Caught DimensionMismatchError:", e)

    try:
        raise NonNumericDataError("abc")
    except NonNumericDataError as e:
        print("Caught NonNumericDataError:", e)

    try:
        raise InvalidShapeError()
    except InvalidShapeError as e:
        print("Caught InvalidShapeError:", e)

    try:
        raise InvalidOperationError("aaa")
    except InvalidOperationError as e:
        print("Caught InvalidOperationError:", e)

if __name__ == "__main__":
    main()