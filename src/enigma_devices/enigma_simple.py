# basic version of the Enigma without the plugboard
import random


class enigma_simple:
    def __init__(self, rotor_1, rotor_1_position, rotor_2, rotor_2_position, rotor_3, rotor_3_position, reflector):
        """
        Constructor for a simple Enigma

        :param rotor_1: the right rotor which rotates after each letter
        :param rotor_1_position: the position of the right rotor (1-26)
        :param rotor_2: the middle rotor which rotates after each full rotation of the right rotor
        :param rotor_2_position: the position of the middle rotor (1-26)
        :param rotor_3: the left rotor which rotates after each full rotation of the middle rotor
        :param rotor_3_position: the position of the left rotor (1-26)
        :param reflector: the reflector which guides the current from one letter to another but never to itself
        """
        # set rotors
        self.rotor_1 = rotor_1
        self.rotor_2 = rotor_2
        self.rotor_3 = rotor_3

        # set rotor positions
        self.rotor_1_position = rotor_1_position
        self.rotor_2_position = rotor_2_position
        self.rotor_3_position = rotor_3_position

        # set reflector
        self.reflector = reflector

    def encrypt_letter(self):
        pass

    def encrypt_text(self):
        pass


# Rotor of the Enigma, where which it rotation the mapping changes
class rotor:
    def __init__(self, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", mapping=None, random_mapping=True, seed=42):
        self.alphabet = alphabet
        # if mapping is not given and random is true
        if mapping is None and random_mapping:
            random.seed(seed)
            mapping_list = random.sample(alphabet, len(alphabet))
            self.mapping = list2String(mapping_list)
            self.initual_mapping = list2String(mapping_list)

    # simulate a rotation, as consequence, the mapping changes
    def rotate(self):
        self.mapping = self.mapping[1:] + self.mapping[0]


# Reflector of the device, difference to rotor: a letter cannot map on itself
# basically letters are building pairs
class reflector:
    def __init__(self, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", mapping=None, random_mapping=True, seed=42):
        self.alphabet = alphabet
        # if mapping is not given and random is true
        if mapping is None and random_mapping:
            random.seed(seed)
            # this will be updated (letters will be taken away as soon as they have a pair)
            alphabet_to_create_mapping_from = list(alphabet)
            self.mapping_dict = {}
            while len(alphabet_to_create_mapping_from) > 0:
                pair_list = random.sample(alphabet_to_create_mapping_from, 2)
                print(pair_list)
                self.mapping_dict[pair_list[0]] = pair_list[1]
                self.mapping_dict[pair_list[1]] = pair_list[0]
                # update letters which still should be mapped
                alphabet_to_create_mapping_from = [ele for ele in alphabet_to_create_mapping_from if
                                                   ele not in pair_list]
                mapping_string = ''
                for key in sorted(self.mapping_dict.keys()):
                    mapping_string += (self.mapping_dict[key])
                self.mapping = mapping_string

        # check if mapping maps to itself
        if mapping:
            print("Mapping was given")
            self.mapping = mapping
            for idx, letter in enumerate(alphabet):
                if letter == self.mapping[idx]:
                    raise Exception("Reflector cannot map to itself!")

    def __str__(self):
        return ("Alphabet: \t" + self.alphabet + "\n" + "Mapping: \t" + self.mapping)


def list2String(letter_list):
    """
    Converst a list of letters into one string
    :param letter_list: The list with letters
    :return: A single string with concatenated every element of the list
    """
    return (''.join(letter_list))
