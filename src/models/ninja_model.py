from jutsu_model import Jutsu

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

    def learn_jutsu(self, jutsu):

        self.jutsu_list.append(jutsu)

        return f'O ninja Naruto Uzumaki acabou de aprender um novo jutsu: {jutsu.jutsu_name}'

    @staticmethod
    def check_health(self, ninja_to_check):
        
        if self.health_pool < 0:
            self.health_pool = 0
            self.concious = False
            
            return self.concious
        
        return self.concious

    def cast_jutsu(self, jutsu, adversary):

        if adversary.concious == True:
            if jutsu in self.jutsu_list and self.chakra_pool > 0:

                adversary.health_pool -= jutsu.jutsu_damage
            
                self.chakra_pool -= jutsu.chakra_spend

                return True

        return False



if __name__ == '__main__':

    rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)
    naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')
    naruto.learn_jutsu(rasengan)
    sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')
    res = naruto.cast_jutsu(rasengan, sasuke)
    print(res)
    # res = naruto.learn_jutsu(rasengan)
    # print(res)
    # narutinho = Ninja('Narutinho', 'Uzumaki', 'Konoha', '5kyiu', ['fire', 'wind'], 30, 40, False)
    # print(naruto.__dict__)
    # # print(narutinho.__dict__)