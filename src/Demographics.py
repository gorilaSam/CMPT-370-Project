from Names import *
from datetime import date

class Demographics(object):

    def __init__(self):
        """
        :return: a demographics object
        """
        self.demographics = {}

    def set_name(self, name:FullName):
        """
        Set patient name in the Demographics
        :params: FullName object
        """
        self.demographics['name'] = name

    def set_address(self, address):
        """
        set patient address
        :param: str containing patient address
        """
        self.demographics['address'] = address

    def set_date_of_birth(self, birthdate):
        """
        set patient's date of birth
        :param: birthdate
        """
        self.demographics['dateOfBirth'] = birthdate
   
    def set_family_history(self, family_history):
        """
        set family history
        :param: str containing patient's history
        """
        self.demographics['familyHistory'] = family_history

    def set_medical_conditions(self, conditions:str):
        """
        Set patient's medical conditions
        :params: str representation of patient medical conditions
        """
        self.demographics['medicalConditions'] = conditions
   
    def get_name(self):
        """
        Get patient name
        :return: FullName object
        """
        return self.demographics['name']

    def get_address(self):
        """
        Get patient address
        :return: str containing patient's adress
        """
        return self.demographics['address']

    def get_date_of_birth(self):
        """
        Get patient date of birth
        :return: str representation of patient's date of birth
        """
        return self.demographics['dateOfBirth']
    
    def get_family_history(self):
        """
        Get patient's family history
        :return: str representation of family history
        """
        return self.demographics['familyHistory']
    
    def get_medical_conditions(self):
        """
        Get patient's medical conditions
        :return: str representation of patient medical conditions
        """
        return self.demographics['medicalConditions']
       
    
