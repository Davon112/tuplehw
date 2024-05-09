# Question 1 

flight = [("Da'Von", "KCMO", "Brazil"), ("Andrea", "MCI", "Oaxaca" )]

itinerary1_name = flight[0][0]
itinerary1_from = flight[0][1]
itinerary1_to = flight[0][2]
itinerary2_name = flight[1][0]
itinerary2_from = flight[1][1]
itinerary2_to = flight[1][2]
print(f"Itinerary 1: {itinerary1_name} - From {itinerary1_from} to {itinerary1_to} Itinerary 2: {itinerary2_name} - From {itinerary2_from} to {itinerary2_to}")

#Question 2
def shelf():
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    x = list(library)

    add_book = input("Which book would you like to add? ")
    book_author = input("Author: ")
    both = (add_book, book_author)

    x.append(both,) 
    
    new_library = list(set(x))

    updated_library = tuple(new_library)
    
    print(updated_library)
shelf()

#Question 3

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Will", "Phone", 3),
    ("Bill", "PC", 1)
]

print(f"|Customer: {orders[0][0]}| |Item: {orders[0][1]}| |Quantity: {orders[0][2]}|")
print()
print(f"|Customer: {orders[1][0]}| |Item: {orders[1][1]}| |Quantity: {orders[1][2]}|")
print()
print(f"|Customer: {orders[2][0]}| |Item: {orders[2][1]}| |Quantity: {orders[2][2]}|")
print()
print(f"|Customer: {orders[3][0]}| |Item: {orders[3][1]}| |Quantity: {orders[3][2]}|")