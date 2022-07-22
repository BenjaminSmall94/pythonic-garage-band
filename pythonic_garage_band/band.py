class Band:

    instances = []

    def __init__(self, band_name, band_members):
        self.name = band_name
        self.members = band_members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        print(cls.instances)
        return cls.instances

    def __str__(self):
        return f"{self.name}! Featuring members {self.members}"

    def __repr__(self):
        return f"Band({self.name}, {self.members})"


class Musician:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"


class Guitarist(Musician):

    @classmethod
    def get_instrument(cls):
        return "guitar"

    @classmethod
    def play_solo(cls):
        return "face melting guitar solo"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):

    @classmethod
    def get_instrument(cls):
        return "bass"

    @classmethod
    def play_solo(cls):
        return "bom bom buh bom"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    @classmethod
    def get_instrument(cls):
        return "drums"

    @classmethod
    def play_solo(cls):
        return "rattle boom crash"


if __name__ == '__main__':
    mcartney = Bassist("Paul McCartney")
    lennon = Guitarist("John Lennon")
    harrison = Guitarist("George Harrison")
    starr = Drummer("Ringo Starr")

    beatles_list = [mcartney, lennon, harrison, starr]
    beatles = Band("The Beatles", beatles_list)

    print(beatles)
    print(mcartney)
    print(lennon)
    print(harrison)
    print(starr)

    print(Band.to_list())