class FabricAnimals():
    def cats_draw(size):
        return f'you have cat with weight {size}' 
    def dogs_draw(size):
        return f'you have dog with weight {size}'


def some_fabric(creator, our_name, size):
    if our_name == 'cat':
        return creator.cats_draw(size)
    elif our_name == 'dog':
        return creator.dogs_draw(size)


print(some_fabric(FabricAnimals, 'cat', 4))

print(hasattr(FabricAnimals, 'cats_draw'))
print(getattr(FabricAnimals, 'dogs_draw'))

def creator_animals(creator, our_name, size):
    if hasattr(creator, our_name):
        return getattr(creator, our_name)(size)
    else:
        return f'no {our_name} in {creator}'


print(creator_animals(FabricAnimals, 'cats_draw', 5))
print(creator_animals(FabricAnimals, 'cats_draw_1', 5))
