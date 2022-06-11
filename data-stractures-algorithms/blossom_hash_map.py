from linked_list import Node, LinkedList


flower_definitions = [
    ["begonia", "cautiousness"],
    ["chrysanthemum", "cheerfulness"],
    ["carnation", "memories"],
    ["daisy", "innocence"],
    ["hyacinth", "playfulness"],
    ["lavender", "devotion"],
    ["magnolia", "dignity"],
    ["morning glory", "unrequited love"],
    ["periwinkle", "new friendship"],
    ["poppy", "rest"],
    ["rose", "love"],
    ["snapdragon", "grace"],
    ["sunflower", "longevity"],
    ["wisteria", "good luck"],
]


class HashMap:
    def __init__(self, array_size=0):
        self.array_size = array_size
        self.array = [LinkedList() for x in range(self.array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_idx = self.compressor(self.hash(key))

        payload = Node([key, value])

        list_at_array = self.array[array_idx]

        found = False
        for item in list_at_array:

            if item[0] == key:
                found = True
                item[1] = value

        if found is not True:
            list_at_array.insert(payload)

        return

    def retrieve(self, key):
        array_idx = self.compressor(self.hash(key))
        list_at_index = self.array[array_idx]

        for item in list_at_index:
            if item[0] == key:

                return item[1]


blossom = HashMap(len(flower_definitions))

for item in flower_definitions:
    blossom.assign(item[0], item[1])


print(blossom.retrieve("daisy"))
