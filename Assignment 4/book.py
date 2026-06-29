#create a class book with title,author and kist of reviews.add methods to add a new review count reviews display all reviews
class Book:

    def __init__(self, title, author, list_of_reviews):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews

    def add_new_review(self, new):
        self.list_of_reviews.append(new)

    def count_review(self):
        return len(self.list_of_reviews)

    def display(self):
        print("\nReviews:")
        for review in self.list_of_reviews:
            print(review)


title = input("Enter title of book: ")
author = input("Enter name of author: ")

list_of_reviews = []

review = input("Add first review: ")
list_of_reviews.append(review)

book = Book(title, author, list_of_reviews)

while True:

    print("\nChoose 1, 2, 3 and 4:")
    print("1. Add new review")
    print("2. Count reviews")
    print("3. Display all reviews")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new = input("Enter review: ")
        book.add_new_review(new)

    elif choice == 2:
        print("Total Reviews:", book.count_review())

    elif choice == 3:
        book.display()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")