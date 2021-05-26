class Jutsu():
    jutsu_ranks = ('D', 'C', 'B', 'A', 'S',)

    def __init__(self, jutsu_name, jutsu_type, jutsu_level, jutsu_damage, chakra_spend):
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_level = jutsu_level
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = chakra_spend

    def define_level(self, jutsu_ranks):
        self.jutsu_level = self.jutsu_level.upper()

        for level in jutsu_ranks:
            if level == self.jutsu_level:
                self.jutsu_level.upper()
            else:
                self.jutsu_level = 'Unranked'       

    def define_chakra_spend(self):

        if self.chakra_spend <= 0:
            self.chakra_spend = 100

if __name__ == '__main__':

    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
    print(rasengan.__dict__)