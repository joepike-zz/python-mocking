

class Animal(db.Model):
    __tablename__ = "animal"
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Sting)
    noise = db.Column(db.Sting)

def get_animal_noises():
    animal_list = Animal.query.all()
    noises = [animal.noise in animal_list]
    return noises

def use_get_noise(self):
    noises = get_animal_noises()
    assert(noises[0] == 'RAAAH')

@mock.patch("animals.Animal")
def test_get_noise(self, mock_animal):

    # create test animal
    test_animal = Animal()
    test_animal.noise = "RAAAAH"
    test_animal.type = "honey badger"

    # set return_value of all to list containing test_animal
    mock_animal.query.all.return_value = [test_animal]

    noises = get_animal_noises()
    assert(noises[0] == "RAAAAH")
