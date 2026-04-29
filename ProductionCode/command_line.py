##
# 
# 
# 
import unittest
import sys 
import csv
import os

class Search():
    data = []
    Filename = "/root/cs257/ind-flask-LucyCab123/ProductionCode/Species.csv"
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'Species.csv')
        """Loads in data from a CSV file and stores it in `data`"""
        with open(file_path, newline='') as datafile:
            csv_file = csv.reader(datafile)
            for row in csv_file:
                self.data.append(row)
        


    def findNum(self, sortCriteria):
        """finds the index number for the wanted criteria and returns it
        location and threats will most likely have to be done in a different
        function because of its complexity.
        """
        sortCriteria = sortCriteria.lower()
    
        if "name" in sortCriteria:
            return 1
        if "common name" in sortCriteria:
            return 2
        if "type" in sortCriteria:
            return 3   
        
        
        if "estimated pop" in sortCriteria:
            return 5
        

    def listSort(self, sortCriteria):
        """
        Function that intakes the sort criteria and returns all animals matching that criteria in a 
        list of lists.
        """
        finalsort = []
        criteriaNum = self.findNum(sortCriteria[0])
        for animal in self.data:
            if animal[criteriaNum].lower() in sortCriteria[1].lower():
                finalsort.append(animal)
        return finalsort


    def typeToList(self, wantedType):
        """
        
        function that takes in the wanted type for an animal (like bird) and searches through the 
        data for animals that match that type, returning them in a list of lists
        """
        sortCriteria = ["type", wantedType]

        wantedAnimals = self.listSort(sortCriteria)
        return wantedAnimals


    def nameToInfo(self, wantedName):
        """
        function that takes in the Scientific name for an animal and searches through the data for that 
        animal before returning it in a list of lists (which will have a length of 1)
        """
        sortCriteria = ["name", wantedName]

        wantedAnimals = self.listSort(sortCriteria)
        return wantedAnimals
    
    def userProblemType(self, typeOfSearch):
        if "name" in typeOfSearch:
            info = self.nameToInfo((input("please type the scientific name: ")).lower())
            if info == []:
                print("Sorry! No animal found. Make sure you are entering the taxonomical name! Not all animals have a different common name.")
        
        elif "type" in typeOfSearch:
            info = self.typeToList((input("please type the type: ")).lower())
            if info == []:
                print("Sorry! No info. make sure you entered the classificaiton correctly!")
        
        else:
            print("Sorry! that was not a valid search type. please try again.")
            info = []
        return info
            
def main():
    Test = Search()
    info = Test.userProblemType((input("Please Type what type of search you would like to perform (name, type):")).lower())
    print(info)



