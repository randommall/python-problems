

class Instructor:

    followers = 0

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_followers(self, follower_name):

        self.followers += 1
        return self.followers, (follower_name)
        
instr_1 = Instructor("Johnson", "Abuja")
address_1 = instr_1.get_address()
name_1 = instr_1.get_name()
followers_1 = instr_1.get_followers("Ben")

print("intstr 1 followers = {}".format(followers_1))
print("name_1 = {}".format(name_1))
print("address_1 = {}".format(address_1))
