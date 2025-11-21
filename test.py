name="Oliver"
print(f"Hello {name}!")

my_favourite_number = 3
times_five = my_favourite_number * 5

print("I multiplied your favourite number by 5 and got...")
print(times_five)

#homework

two_numbers = input ("Hey, can you give me two numbers?")
var1, var2 = two_numbers.split()

#turns them into integers for calculations
var1 = int(var1)
var2 = int(var2)

#print(f"first number: {var1}")
#print(f"second number: {var2}")  

print("Adding the two numbers gives...")
adding = var1 + var2
print(adding)

print("Subtracting the two numbers gives...")
subtracting = var1 - var2
print(subtracting)

print("Multiplying the two numbers gives...")
multiplying = var1 * var2
print(multiplying)

print("Dividing the two numbers gives...")
dividing = var1 / var2
print(dividing)

print("First number raised to the power of the second number gives...")
powering = var1 ** var2
print(powering)

print("Thanks for playing!")
