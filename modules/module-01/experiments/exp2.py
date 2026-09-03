'''Challenge 1 — no hints

A cinema has 347 people entering.

Each bus can carry 50 people.

You need to determine:

How many full buses are required?
How many people will be left after filling the full buses?'''


no_of_people = 347
people_bus_carry = 50

no_of_buses = no_of_people // people_bus_carry
people_left = no_of_people % people_bus_carry
print(no_of_buses)
print(people_left)