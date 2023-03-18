############
# Part 1   #
###########

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    def __repr__(self):
        return f'<name={self.name } code={self.code} first_harvest={self.first_harvest} color={self.color} is_seedless={self.is_seedless} is_bestseller={self.is_bestseller}>' 

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    # code, first_harvest, color, is_seedless, is_bestseller, name

    muskmelon = MelonType(
        code="musk",
        name="Muskmelon",
        first_harvest=1998,
        color="green",
        is_seedless=True,
        is_bestseller= True)
    muskmelon.add_pairing("mint")

    all_melon_types.append(muskmelon)


    casaba = MelonType(
        code="cas",
        name="Casaba",
        first_harvest=2003,
        color="orange",
        is_seedless=False,
        is_bestseller= False)
        
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")

    all_melon_types.append(casaba)

   
    crenshaw = MelonType(
        code="cren",
        name="Crenshaw",
        first_harvest=1996,
        color="green",
        is_seedless=False,
        is_bestseller= False)
    crenshaw.add_pairing("prosciutto")
    
    all_melon_types.append(crenshaw)

   
    yellow_watermelon = MelonType(
        code="yw",
        name="Yellow Watermelon",
        first_harvest=2013,
        color="yellow",
        is_seedless=False,
        is_bestseller= True)
    yellow_watermelon.add_pairing("ice cream")
    
    all_melon_types.append(yellow_watermelon)

    

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_obj in melon_types:
        print(f'{melon_obj.name} pairs with')
        for food in melon_obj.pairings:
            print(f'- {food}')
        print()



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    dictionary_of_melons = {}

    for melon in melon_types:
        code = melon.code
        dictionary_of_melons[code] = melon

    return dictionary_of_melons


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by

    def __repr__(self):
        return f'<melon_type={self.melon_type} shape_rating={self.shape_rating} color_rating={self.color_rating} harvested_from={self.harvested_from} harvested_by={self.harvested_by}>'

    def is_sellable(self):
        if (self.shape_rating > 5) and (self.color_rating > 5) and not (self.harvested_from == 3):
            return True
    
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_lookup = make_melon_type_lookup(melon_types)

    melon_objects = []

    melon1 = Melon(
        melon_type=melon_lookup['yw'],
        shape_rating=8,
        color_rating=7,
        harvested_from=2,
        harvested_by="Sheila")
    melon_objects.append(melon1)
   
    melon2 = Melon(
        melon_type=melon_lookup['yw'],
        shape_rating=3,
        color_rating=4,
        harvested_from=2,
        harvested_by="Sheila") 
    melon_objects.append(melon2)

    melon3 = Melon(
        melon_type=melon_lookup['yw'],
        shape_rating=9,
        color_rating=8,
        harvested_from=3,
        harvested_by="Sheila")
    melon_objects.append(melon3)
    

    melon4 = Melon(
        melon_type=melon_lookup['cas'],
        shape_rating=10,
        color_rating=6,
        harvested_from=35,
        harvested_by="Sheila")
    melon_objects.append(melon4)
    

    melon5 = Melon(
        melon_type=melon_lookup['cren'],
        shape_rating=8,
        color_rating=9,
        harvested_from=35,
        harvested_by="Michael")
    melon_objects.append(melon5)
    

    melon6 = Melon(
        melon_type=melon_lookup['cren'],
        shape_rating=8,
        color_rating=2,
        harvested_from=35,
        harvested_by="Michael")
    melon_objects.append(melon6)
    

    melon7 = Melon(
        melon_type=melon_lookup['cren'],
        shape_rating=2,
        color_rating=3,
        harvested_from=4,
        harvested_by="Michael")
    melon_objects.append(melon7)
    

    melon8 = Melon(
        melon_type=melon_lookup['musk'],
        shape_rating=6,
        color_rating=7,
        harvested_from=4,
        harvested_by="Michael")
    melon_objects.append(melon8)
    

    melon9 = Melon(
        melon_type=melon_lookup['yw'],
        shape_rating=7,
        color_rating=10,
        harvested_from=3,
        harvested_by="Sheila")
    melon_objects.append(melon9)

    return melon_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
