from exceptions.errors import NonNumericDataError

class Array:
    def __init__(self, data):
        self._check_numeric(data)   
        self.data = data
        self.shape = self._get_shape(data)
        self.ndim = len(self.shape)

    def _check_numeric(self, item):
        if isinstance(item, list):
            for x in item:
                self._check_numeric(x)
        elif not isinstance(item, (int, float)):
            raise NonNumericDataError()

    def _get_shape(self, data):
        shape = []
        current = data
        while isinstance(current, list):
            shape.append(len(current))
            current = current[0]
        return tuple(shape)

    def flatten(self):
        result = []
        def collect(item):
            if isinstance(item, list):
                for x in item:
                    collect(x)
            else:
                result.append(item)
        collect(self.data)
        return Array(result)

    def __repr__(self):
        return f"Array(shape={self.shape})\n{self.data}"