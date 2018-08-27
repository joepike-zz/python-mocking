from contextlib import contextmanager

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
        print("The stars are falling")
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
    hells = [hell for hell in Dragon.spawn_badger().dance()[0].star["the_star"].fall()]
    for hell in hells:
        with hell.initiate_breaking_loose() as broke_loose:
            if broke_loose:
                return "Hell broke loose"
            else:
                return "Hell did not break loose"

# no mocking
# def test_if_hell_broke_loose(self):
#     broke_loose = break_hell_loose()
#     asser(broke_loose == "Hell did not break loose")

@mock.patch("silly.Dragon")
def test_if_hell_broke_loose(self, mock_dragon):
    broke_loose = break_hell_lose()
    dance_return_mock = mock_dragon.spawn_badger.return_value.dance.return_value
    flower_mock = dance_return_mock.__getitem__.return_value
    star_dict_mock = flower_mock.star
    star_mock = star_dict_mock.__getitem__.return_value
    hell_mock = mock.MagicMock()
    star_mock.fall.return_value = [hell_mock]
    hell_mock.initiate_breaking_loose.return_value.__enter__.return_value = False
