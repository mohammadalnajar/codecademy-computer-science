# You can start with the
# Cat class or erase this
# and use your own!
class Cat:
    def __init__(self, input_name, input_breed, input_age=0, is_friendly=True):
        self.name = input_name
        self.breed = input_breed
        self.age = input_age
        self.is_friendly = is_friendly
        self.friends = []

    # Create method where two
    # pets interact.
    # Ex: def name(self, pet):
    def become_friends(self, other_pet):
        if self.is_friendly and other_pet.is_friendly:
            self.friends.append(other_pet)
            other_pet.friends.append(self)
            print(f"{self.name} and {other_pet.name} are now friends!")
        else:
            print(f"{self.name} and {other_pet.name} are not friends!")

    def __repr__(self):
        is_friendly_str = (
            f"{self.name} is friendly"
            if self.is_friendly
            else "{self.name} is not friendly"
        )
        single_plural = "friend" if len(self.friends) == 1 else "friends"
        description = f"{self.name} is a {self.age} year old {self.breed}, {is_friendly_str} and has {len(self.friends)} {single_plural}."

        return description


# Create two pets.
cat_one = Cat("Leo", "Tabby", 3)
cat_two = Cat("Milo", "Tabby", 1)


# Call your method below.

cat_one.become_friends(cat_two)


for cat in cat_one.friends:
    print(cat.name)

cat_one_desc = cat_one.__repr__()

print(cat_one_desc)
