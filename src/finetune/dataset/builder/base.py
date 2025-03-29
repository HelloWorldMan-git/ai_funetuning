import abc


class Base:
    @abc.abstractmethod
    def build(
            self, type: str = None, *args, **kwargs
    ) -> str:
        pass