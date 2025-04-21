# This module defines a comic book database. In the interests of full disclosure, I received
# some help designing some of the methods from Google's Gemini
# AI via https://g.co/gemini/share/3b4bc25f28b9

# This program was part of my CS 202 Intro to Python course at UWM in Spring 2025.

import bisect
import tkinter as tk
from tkinter import filedialog
class ComicBookDB:
    """ This implements a comic book database as a dictionary of lists. """
    def __init__(self, ComicBook):
        """ This constructor creates a comic book database as a with its first comic book. """
        self.titleDB = {ComicBook.title: [ComicBook]}

    def insertComicBook(self, ComicBook):
        """ This method inserts a comic book into the database in order. """
        if ComicBook.title not in self.titleDB:
            self.titleDB[ComicBook.title] = [ComicBook]
        else:
            insertedComic = False
            for i, obj in enumerate(self.titleDB[ComicBook.title]):
                if not insertedComic:
                    if ComicBook == obj:
                        print(f"{ComicBook.getString()} is already in the database.")
                        insertedComic = True
                    elif ComicBook < obj:
                         self.titleDB[ComicBook.title].insert(i, ComicBook)
                         insertedComic = True
            if not insertedComic:
                self.titleDB[ComicBook.title].append(ComicBook)

    def removeComicBook(self, ComicBook):
        """ This method revoves a comic book from the database. """
        if ComicBook.title not in self.titleDB:
            print(f"{ComicBook.getString()} is not in database.")
        else:
            foundComic = False
            for i, obj in enumerate(self.titleDB[ComicBook.title]):
                if ComicBook == obj:
                     self.titleDB[ComicBook.title].pop(i)
                     foundComic = True
            if not foundComic:
                print(f"{ComicBook.getString()} is not in database.")
                

    def printDB(self, keyParam=None):
        """ This method prints the database. """
        if keyParam is None:
            total_elements = 0
            for key in self.titleDB:
                total_elements += len(self.titleDB[key])  # Get the length of each list and add it
            print(f"Database contents: [", end="")
            counter = 0
            for i, key in enumerate(self.titleDB):
                for j, obj in enumerate(self.titleDB[key]):
                    obj.printComic()
                    counter += 1
                    if counter != total_elements:
                        print(f", ", end = "")
            print(f"]")
        else:
            if self.titleDB[keyParam][0].title not in self.titleDB:
                printString = ComicBook.printComic()
                print(f"ComicBook.getString() is not in database.")
            else:
                total_elements = len(self.titleDB[keyParam])
                print(f"Database contents for title \"{self.titleDB[keyParam][0].title}\": [", end="")
                counter = 0
                for i, obj in enumerate(self.titleDB[keyParam]):
                    obj.printComic()
                    counter += 1
                    if counter != total_elements:
                        print(f", ", end = "")
                print(f"]")

    def readDB(self):
        """ This method reads in a database in csv format. """
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.split(",")
                line[1] = int(line[1])
                line[2] = int(line[2])
                MyComic = ComicBook(line[0], line[1], line[2])
                self.insertComicBook(MyComic)
    
    def writeDB(self):
        """ This method wrties in a database in csv format. """
        file_path = filedialog.askdirectory()
        filename = input("Enter the filename (e.g., MyComicDB.csv): ")
        file_path_and_name = f"{file_path}/{filename}"
        with open(file_path_and_name, 'w') as file:
            for key in self.titleDB:
                for obj in self.titleDB[key]:
                    file.write(f"{obj.title}, {obj.vol}, {obj.issue}\n")
           

class ComicBook:
    """ This constructor creates a comic book class. """
    def __init__(self, title, vol, issue):
        """ This constructor creates a ComicBook entry. """
        self.title = title
        self.vol = vol
        self.issue = issue

    def __lt__(self, other):
        """ This method defines how instances of ComicBook should be compared (based on title, volume number, and issue number in this case) """
        # First, compare by title (if not the same title, incomparable)
        if self.title != other.title:
            return False
        else:
            # Next, compare by volume if titles are equal
            if self.vol < other.vol:
                return True
            elif self.vol > other.vol:
                return False
            # If volumes are equal, compare by issue
            else:  # self.volume == other.volume
                return self.issue < other.issue

    def __repr__(self):
        """ This method represents elements of ComicBook """
        return f"\"{self.title}\", Vol. {self.vol}, No. {self.issue}"

    def getTitle(self):
        """ This method gets the title of ComicBook """
        return self.title

    def getVol(self):
        """ This method gets the volume of ComicBook """
        return self.vol

    def getIssue(self):
        """ This method gets the issue number of ComicBook """
        return get.issue

    def printComic(self):
        """ This method prints a ComicBook """
        print(f"(\"{self.title}\", Vol. {self.vol}, No. {self.issue})", end="")

    def getString(self):
        """ This method gets the ComicBook as a string """
        return f"(\"{self.title}\", Vol. {self.vol}, No. {self.issue})".rstrip()
        
if __name__ == "__main__":
    import comicBookDB

    MyComic1 = comicBookDB.ComicBook("Iron Fist", 1, 8)
    MyDB = comicBookDB.ComicBookDB(MyComic1)
    MyDB.printDB()
    MyComic2 = comicBookDB.ComicBook("Iron Fist", 1, 9)
    MyDB.insertComicBook(MyComic2)
    MyDB.printDB()
    MyComic3 = comicBookDB.ComicBook("Iron Fist", 1, 10)
    MyDB.insertComicBook(MyComic3)
    MyDB.printDB()
    MyDB.removeComicBook(MyComic2)
    MyDB.printDB()
    MyDB.insertComicBook(MyComic1)
    MyDB.removeComicBook(MyComic2)
    MyComic4 = comicBookDB.ComicBook("Luke Cage: Power Man", 1, 1)
    MyDB.insertComicBook(MyComic4)
    MyDB.printDB()
    MyDB.printDB("Iron Fist")
    MyDB.printDB()
    MyDB.insertComicBook(MyComic2)
    MyDB.printDB()
    MyDB.writeDB()
    MyDB2 = comicBookDB.ComicBookDB(MyComic1)
    MyDB2.readDB()
    MyDB2.printDB()
