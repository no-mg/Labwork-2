#родитель1
class Album:
    def __init__(self, version):
        self.version = version

    def show(self):
        print(f"Альбом {self.version}")

#дети
class StandarVerAlbum(Album):
    def __init__(self):
        super().__init__("Стандартная версия")


class LimitedVerAlbum(Album):
    def __init__(self):
        super().__init__("Лимитированная версия")


class MerchVerAlbum(Album):
    def __init__(self):
        super().__init__("Мерч версия")


#родитель2
class Photocard:
    def __init__(self, member, set_name):
        self.member = member
        self.set_name = set_name

    def show(self):
        print(f"Участник {self.member} (сет {self.set_name})")

#другие дети
class SetAPhotocard(Photocard):
    def __init__(self, member):
        super().__init__(member, "A")


class SetBPhotocard(Photocard):
    def __init__(self, member):
        super().__init__(member, "B")


#фабрика может делать альбом и карту но не знает какие
class AlbumFactory:
    def create_album(self):
        pass

    def create_photocard(self):
        pass


class StandardFactory(AlbumFactory):
    def create_album(self):
        return StandarVerAlbum()

    def create_photocard(self):
        return SetAPhotocard("Уён")


class LimitedFactory(AlbumFactory):
    def create_album(self):
        return LimitedVerAlbum()

    def create_photocard(self):
        return SetBPhotocard("Сан")


class MerchFactory(AlbumFactory):
    def create_album(self):
        return MerchVerAlbum()

    def create_photocard(self):
        return SetAPhotocard("Сонхва")

factory = StandardFactory()
album = factory.create_album()
card = factory.create_photocard()
album.show()
card.show()