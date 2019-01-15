import numpy as np


class BasicSlime(object):
    """
    This is the basic slime class.
    It includes the most basic features of slime
    """

    def __init__(self, can_cyber=True):
        self.can_cyber = can_cyber
        self.is_cyber_unlocked = False

    def do(self, activity):
        """Used for doing activities with the slime

        Args:
            activity (string): The activity (method name)
        """

        if activity == "play":
            self.play()
        elif activity == "calculate":
            try:
                operation = input(
                    "Please enter the operation you'd like to use (+, -, *, /): ")
                num1 = int(input("Please enter the first number: "))
                num2 = int(input("Please enter the second number: "))

                self.calculate(operation, num1, num2)
            except:
                print("Something is invalid.")
        elif activity == "trigo" or activity == "trigonometry":
            try:
                operation = input(
                    "Please enter the operation you'd like to use (cos, sin, tan): ")
                angle = int(
                    input("Please enter the angle you'd like to calculate: "))
                is_deg = input("Are you using degrees? ")

                if is_deg.lower() == "yes" or is_deg.lower() == "y":
                    is_deg = True
                else:
                    is_deg = False

                self.trigo(operation, angle, is_deg)
            except:
                print("Something is invalid.")
        elif activity == "unlock secret power":
            self.unlock_secret_power()
        elif activity == "cyber":
            self.cyber()
        else:
            print("Your slime doesn't recognize this kind of activity!")

    def play(self):
        """Playing with the slime
        """

        print("You are playing with the slime!")
        print("You are \"enjoying\"!")

    def calculate(self, operation, num1, num2):
        """Calculates using the inputted operation something with inputted nums

        Args:
            operation (string): The operation used (+, -, *, /)
            num1 (int): The first number
            num2 (int): The second number
        """

        if operation == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Unknown operation")

    def trigo(self, operation, angle, is_deg=True):
        """Prints the result for the inputted trigonometry function on the inputted angle

        Args:
            operation (string): The function used (cos, sin, tan)
            angle (int): The angle
            is_deg (bool, optional): Defaults to True. Whether you use degrees or radians
        """

        degree_sign = '°' if is_deg else "rad"
        if operation == "cos":
            result = np.cos(angle)
            if is_deg:
                result = np.cos(np.deg2rad(angle))
            print(f"{operation}({angle}{degree_sign}) = {result}")
        elif operation == "sin":
            result = np.sin([angle])
            if is_deg:
                result = np.sin(np.deg2rad(angle))
            print(f"{operation}({angle}{degree_sign}) = {result}")
        elif operation == "tan":
            result = np.tan(angle)
            if is_deg:
                result = np.tan(np.deg2rad(angle))
            print(f"{operation}({angle}{degree_sign}) = {result}")
        else:
            print("Unknown operation")

    def unlock_secret_power(self):
        """Unlocks the secret power
        """

        if self.can_cyber:
            print("You've just unlocked the secret power of AvinoamCo's slime!")
            self.is_cyber_unlocked = True
        else:
            print("Your slime isn't capable of unlocking the secret power!")

    def cyber(self):
        """Cybers
        """

        if self.is_cyber_unlocked:
            print("You've just used the \"Cyber\" activity!")
            print("Your slime is now cybering the Pentagon!")
        else:
            print("Your slime isn't capable of \"Cyber\" yet!")
