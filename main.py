from creation.array_creation import array, zeros, ones, eye
from statistic.stats import mean, var, std

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

    a = array([[1,2,3],[4,5,6]])

    print("Array:")
    print(a)

    print("\nMean:")
    print(mean(a))

    print("\nVariance:")
    print(var(a))

    print("\nStandard Deviation:")
    print(std(a))



if __name__ == "__main__":
    main()