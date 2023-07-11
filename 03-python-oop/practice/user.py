class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            print("Points spent:", amount)
        else:
            print("Insufficient points to spend.")


# Create a user instance and call the display_info method
user1 = User("John", "Doe", "john@example.com", 30)
user1.display_info()

# Call the enroll method on user1
user1.enroll()

# Create 2 more instances of the User class
user2 = User("Jane", "Smith", "jane@example.com", 25)
user3 = User("Michael", "Johnson", "michael@example.com", 35)

# Call the spend_points method on the first user
user1.spend_points(50)

# Call the enroll method on the second user
user2.enroll()

# Call the spend_points method on the second user
user2.spend_points(80)

# Call the display_info method on all the users
user1.display_info()
user2.display_info()
user3.display_info()

# BONUS: Try to re-enroll the first user
user1.enroll()

# BONUS: Prevent over-spending on the third user
user3.spend_points(40)




user1.enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
user3.enroll().spend_points(40).display_info()




users = [
    User("John", "Doe", "john@example.com", 30),
    User("Jane", "Smith", "jane@example.com", 25),
    User("Michael", "Johnson", "michael@example.com", 35)
]

for user in users:
    user.enroll().spend_points(50).display_info()