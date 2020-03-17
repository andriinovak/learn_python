class Manager:
    """Manager class"""

    def __init__(self):
        pass

    def a(self, *args):
        pass
        # do the first thing

    def b(self, *args):
        pass
        # do a second thing

    def c(self, *args):
        print(args)
        # do a third thing


def main_routine():
    """Calls Manager methods. Does not return anything."""
    manager = Manager()
    manager.a()
    manager.b()
    manager.c("c_args")


if __name__ == "__main__":
    main_routine()
