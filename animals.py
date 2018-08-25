
something = aClass().a_class_method()["a key"].a_method().an_attribute

class Animal(db.Model):
    __tablename__ = "animal"
    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.Sting)
    noise = db.Column(db.Sting)

def get_animal_noises():
    animal_list = Animal.query.all()
    noises = [animal.noise in animal_list]
    return noises
