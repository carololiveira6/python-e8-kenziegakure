class Jutsu():
    jutsu_ranks = ('D', 'C', 'B', 'A', 'S',)

    def __init__(self, jutsu_name, jutsu_type, jutsu_level, jutsu_damage, chakra_spend):
        self.jutsu_name = jutsu_name
        self.jutsu_type = jutsu_type
        self.jutsu_level = jutsu_level.upper() if jutsu_level.upper() in self.jutsu_ranks else 'Unranked'
        self.jutsu_damage = jutsu_damage
        self.chakra_spend = 100 if chakra_spend <= 0 else chakra_spend