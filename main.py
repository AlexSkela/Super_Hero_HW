import requests

from pprint import pprint

class SuperHero:
    super_heros = []

    def __init__(self, name):
        self.name = name
        self.params = {}
        SuperHero.super_heros.append(self.params)

    def _super_found(self):
        super_url = f"https://superheroapi.com/api/2619421814940190/search/{self.name}"
        headers = {'Authorization' : 'secret-token-123'}
        timeout = 2
        res = requests.get(super_url, headers=headers, timeout=timeout)
        resalt = res.json()
        return resalt['results'][0]['id']


    def param_of_hero(self, name):
        id = self._super_found()
        url = f"https://superheroapi.com/api/2619421814940190/{id}/powerstats"
        headers = {'Authorization' : 'secret-token-123'}
        params = {'intelligence' : ' '}
        timeout = 2
        resp = requests.get(url, headers=headers, params=params, timeout=timeout)
        self.params[self.name] = resp.json()
        return resp.json()

    def __gt__(self, other):
        if not isinstance(other, SuperHero):
            print('Такого супергероя нет')
            return
        else:
            res = int(self.params[self.name]['intelligence']) > int(other.params[other.name]['intelligence'])
            if res == True:
                res_1 = f'{self.name} умнее {other.name}'
                return res_1
            elif res == False:
                res_2 = f'{self.name} глупее {other.name}'
                return res_2



if __name__ == '__main__':
    one_hero = SuperHero('Hulk')
    one_hero.param_of_hero("Hulk")
    next_hero = SuperHero('Captain America')
    next_hero.param_of_hero('Captain America')
    bad_hero = SuperHero('Thanos')
    bad_hero.param_of_hero('Thanos')
    pprint(SuperHero.super_heros)
    pprint(one_hero > next_hero)
    pprint(one_hero > bad_hero)