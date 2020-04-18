import redis
import abc


class Storage:

    def __init__(self, uri):
        self.uri = uri
        self.connection = self.connect()
    
    @abc.abstractmethod
    def connect(self):
        return NotImplementedError("SubClasses should implement this method")

    @abc.abstractmethod
    def set_key(self):
        return NotImplementedError("SubClasses should implement this method")

    @abc.abstractmethod
    def get_key(self):
        return NotImplementedError("SubClasses should implemente this method")


class Redis(Storage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StorageFactory:

    persistency = {
        "redis": Redis
    }
    
    @classmethod
    def loadstorage(cls, storage_type, *args, **kwargs):
        return  persistency['storage_type'](*args, **kwargs)