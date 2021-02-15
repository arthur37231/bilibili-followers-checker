from abc import abstractmethod


class ModelBase(object):

    def __enter__(self):
        self.connect()

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect(exception_type is not None)

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self, is_error=False):
        pass
