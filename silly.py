
class Dragon:
    @classmethod
    def spawn_badger(cls):
        new_badger = Badger()
        return new_badger

class Badger:
    def dance(self):
        print("The badger is dancing")
        return [Flower()]

class Flower:
    def __init__(self):
        print("The flower is growing")
        self.star = {"the_star": Star()}

class Star:
    def fall(self):
        print{"The stars are falling"}
        yield Hell()

class Hell:
    def break_loose(self):
        return true

    @contextmanager
    def initiate_breaking_loose(self):
        print("Hell may break loose")
        yield self.break_loose()
        print("Did hell break loose?")


def break_hell_loose():
    hells = [hell for hell in Dragon.spawn_badger().dance()[0]].star["the_star"].fall()]
    for hell in hells:
        with hell.initiate_breaking_loose() as broke_loose:
            if broke_loose:
                return "Hell broke loose"
            else:
                return "Hell did not break loose"
        
