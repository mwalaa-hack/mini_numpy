from creation.array_creation import array, zeros, ones, eye

def main():
    a1 = array([1,2,3])
    # print(a1)

    a2 = array([[1,2],[3,4]])
    # print(a2)

    z = zeros((2,2,2))
    # print(z)

    o = ones((3,2))
    # print(o)

    e = eye(3)
    print(e)

if __name__ == "__main__":
    main()