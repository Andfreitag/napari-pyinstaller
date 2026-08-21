import sys


class NullWriter:
    def write(self, text):
        pass

    def flush(self):
        pass


if sys.stdout is None:
    sys.stdout = NullWriter()

if sys.stderr is None:
    sys.stderr = NullWriter()


from napari import __main__


if __name__ == "__main__":
    __main__.main()

