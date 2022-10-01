# We have to import 2 internal modules in python to operate this function i,e, 'random' and 'string' modules
import random, string
# We have to pass only one parameter i.e, 'length of our password ' in our custom made function
def random_password_generator(length_of_password):

    # We are randomly taking all upper and lower case letters, all numeric digits and all the punctuations to generate our password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""   

    # Here the mixture of those random things are taking place with the help of a for loop which will run till the (length of password provided to the function)
    for index in range(length_of_password):
        password = password + random.choice(characters)

    # This will return our password
    print("{}".format(password))

