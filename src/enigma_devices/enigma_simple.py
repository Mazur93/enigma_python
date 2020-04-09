# basic version of the Enigma without the plugboard
import random


class enigma_simple:
    def __init__(self, rotor_1, rotor_2, rotor_3, reflector):
        pass

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

    def __str__(self):
        print("Alphabet: \t" + self.alphabet)
        print("Mapping: \t" + self.mapping)


def list2String(letter_list):
    """
    Converst a list of letters into one string
    :param letter_list: The list with letters
    :return: A single string with concatenated every element of the list
    """
    return (''.join(letter_list))
