class Ninja():

    def __init__(self, name, clan, village, ninja_level = 'Unranked', jutsu_list = [], health_pool = 100, chakra_pool = 100, concious = True):

        self.name = name
        self.clan = clan
        self.village = village
        self.ninja_level = ninja_level
        self.jutsu_list = jutsu_list
        self.health_pool = health_pool
        self.chakra_pool = chakra_pool
        self.concious = concious

if __name__ == '__main__':

    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    narutinho = Ninja('Narutinho', 'Uzumaki', 'Konoha', '5kyiu', ['fire', 'wind'], 30, 40, False)
    print(naruto.__dict__)
    print(narutinho.__dict__)