class CustomList(list):
    def remove_if_exist(self, v):
        try:
            self.remove(v)
        except ValueError:
            pass
