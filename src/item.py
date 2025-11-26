class Item:

    def __init__(self, descricao: str, volume: int):
        self._volume = volume
        self._descricao = descricao

    def get_volume(self):
        return self._volume

    def get_descricao(self):
        return self._descricao