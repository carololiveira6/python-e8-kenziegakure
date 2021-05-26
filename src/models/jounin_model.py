from ninja_model import Ninja
import operator

class Jounin(Ninja):

    ninja_level = 'Jounin'

    def __init__(self, name, clan, village, proficiency = {'taijutsu': int, 'ninjutsu': int, 'genjutsu': int}, is_in_mission = False):

        super().__init__(name, clan, village, ninja_level = 'Unranked', jutsu_list = [], health_pool = 100, chakra_pool = 100, concious = True)
        
        self.name = name
        self.clan = clan
        self.village = village
        self.proficiency = proficiency
        self.is_in_mission = is_in_mission

    def list_best_proficiency(self):
        
        max_values = max(self.proficiency.items(), key=operator.itemgetter(1))[0]

        return f'{self.name} demonstra maior proficiência em {max_values}'

    def start_mission(self):

        if self.is_in_mission == False:
            self.is_in_mission = True
            
            return f'O ninja {self.name} {self.clan} saiu em missão'

        return f'O ninja {self.name} {self.clan} já está em uma missão'

    def return_from_mission(self):

        if self.is_in_mission == True:
            self.is_in_mission = False

            return f'O ninja {self.name} {self.clan} não está em nenhuma missão no momento'

        return f'O ninja {self.name} {self.clan} retornou em segurança da missão'

if __name__ == '__main__':

    kakashi_proficiency = {'taijutsu': 7, 'ninjutsu': 9, 'genjutsu': 4}
    kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi_proficiency)
    res = kakashi.list_best_proficiency()
    print(res)
    res = kakashi.start_mission()
    print(res)
    res = kakashi.return_from_mission()
    print(res)