import numpy as np

class Student:

    def __init__(self, name, surname, albumNo, gradeList, presence):
        self.name = name
        self.surname = surname
        self.albumNo = albumNo
        self.gradeList = gradeList
        self.presence = presence

    def gradeAvg(self):
        return(np.mean(self.gradeList))

    def introObject(self):
        avgGrade = np.mean(self.gradeList)
        avgPresence = np.mean(self.presence)
        if (np.mean(avgPresence) > 0.8):
            print ("Student: " + self.name + " " + self.surname + " index: " + str(self.albumNo) + "ma średnią ocen " + str(avgGrade) + ", jest studentem z dobrą frekfencją")
        else:
            print ("Student: " + self.name + " " + self.surname + " index: " + str(self.albumNo) + "ma średnią ocen " + str(avgGrade) + ", jest studentem ze słabą frekfencją")

uczen = Student("Zbigniew", "Karolczuk", 42431, [4, 3, 2, 6, 4, 5, 5, 1], [0, 1, 1, 1, 1, 1, 1, 1])
print (uczen.name)
print (uczen.gradeAvg())
uczen.introObject()
