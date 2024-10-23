


class AirLine:  # Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.


    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return self
