class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'


class Human(Animal):
    def __init__(self, sex, race):
        self.__sex = sex
        self.__race = race

    @property
    def sex(self):
        """ Getter for sex"""
        return self.__sex

    @property
    def race(self):
        """ Getter for race"""
        return self.__race

    def __repr__(self):
        return f'{self.__class__.__name__}(sex={self.sex!r}, race={self.race!r})'


class Person(Human):
    def __init__(self, sex, race, name, age):
        super().__init__(sex, race)
        self.change_name(name)
        self.__age = age

    def change_name(self, new_name):
            self.name = new_name

    def greeting(self):
        return f'Hi, my name is {self.__name:}'

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
         if isinstance(new_name, str):
            self.__name = new_name
         else:
            err = f'{value!r} must be a string'
            raise ValueError(err)

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.__name!r}, age={self.__age!r})'


class Vaccine:
    def __init__(self, vac_list):
        self.add_vaccine(vac_list)

    def add_vaccine(self, new_vac):
        self.__vac_list = new_vac,

    @property
    def vac_list(self):
        return self.__vac_list

    @vac_list.setter
    def vac_list(self, new_vac):
        if isinstance(new_vac, str):
            self.__vac_list += new_vac,
        else:
            err = f'{new_vac!r} must be a string'
            raise ValueError(err)

    def __repr__(self):
        return f'{self.__class__.__name__:}(vac_list={self.__vac_list!r})'


class Chip:
    implanted = False
    def __init__(self, id_num):
        self.__id_num = id_num

    @property
    def id_num(self):
        return self.__id_num

    def __repr__(self):
        return f'{self.__class__.__name__:}(id_num={self.__id_num!r})'


# TODO: fill classes above with the required logic
#       to represent human and person (probably with tax number, ...)
# TODO: try to make an Enterprise able to own Pets
# TODO: - add class to represent vaccine
#       - add class to represent generic chip,
#           and separate subclasses for concrete animal ID chips
#       - anything other you want to extend here


class Pet(Animal):
    """Abstracts an animal with an owner and name.

    Each pet is an animal having an owner and a name --
    that is how we model it.
    """

    def __init__(self, owner, vac, chp):
        """Set owner at instantiation."""
        self.change_owner(owner)
        self.change_vaccine(vac)
        self.change_chip(chp)

    def change_owner(self, new_owner):
        """Called to transfer ownership or set a new owner."""
        self.owner = new_owner

    def change_vaccine(self, new_vac):
        self.vaccine = new_vac

    def change_chip(self, new_chip):
        self.chip = new_chip

    @property
    def owner(self):
        """Dummy getter for hidden method."""
        return self.__owner

    @property
    def vaccine(self):
        """Dummy getter for hidden method."""
        return self.__vaccine

    @property
    def chip(self):
        """Dummy getter for hidden method."""
        return self.__chip

    @owner.setter
    def owner(self, value):
        """This is called when setting owner.

        The difference is that here we can check
        what the user sets owner to. E.g. check
        that owner is not number.

        Called at dog.owner = value
        """
        # do some checks here
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of Person.'
            raise ValueError(err)

    @vaccine.setter
    def vaccine(self, value):
        if isinstance(value, Vaccine):
            self.__vaccine = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of Vaccine.'
            raise ValueError(err)

    @chip.setter
    def chip(self, value):
        if isinstance(value, Chip):
            self.__chip = value
        else:
            err = f'{value!r} must be an instance'
            err += ' or subclass of Chip.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(owner={self.owner!r}, vaccine={self.__vaccine!r}, chip={self.__chip!r})'


if __name__ == '__main__':
    pass
