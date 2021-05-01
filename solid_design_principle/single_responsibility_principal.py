# single responsibility principle is the principle where a class should have only one reason to change

# Here we are breaking the single responsibility rule . here the class journal is not only allowing the jouranl
# to add and manipulate the entries but it taking the functionality of saving and loading the journal . This is the wrong
# approach suppose if you have multiple class and they implement also save and load method, suppose if
# you have to change your save and load method in the future you have to go to every class and change their
# save and load method.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entries(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def del_entires(self, position):
        del self.entries[position]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def low_from_web(self, uri):
    #     pass


## Now we will the move  responsibility of saving and loading to another class


class PersistenceManager:
    # def __init__(self):
    #     pass

    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()

j = Journal()

j.add_entries("I played Pubg")
j.add_entries("I done little work")

filename = "/home/sandip/work/Learn/python_design_patterns/solid_design_principle/test.txt"

PersistenceManager.save_to_file(j, filename=filename)

with open(filename, "r")as file:
    file.read()

print(j)
