#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed = None):
        self._name = None
        self._breed = None

        if breed is not None:
            self.set_breed(breed)
        
        if name is not None:
            self.set_name(name)

    
    def get_name(self):
        return self._name 
    
    def get_breed(self):
        return self._breed
    
    
    def set_name(self, value):
        if value is None:
            self._name = None
        elif isinstance(value, str) and (1 <= len(value) <= 25):
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
    
    def set_breed(self,value):
        if value is None:
            self._breed = None
        elif value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)