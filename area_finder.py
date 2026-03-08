import numpy as np
import matplotlib.pyplot as plt

#Naming and all

bot: str = "Hamm"
print (f'{bot}: Hey there, Wanna find area of shapes??')

while True:
    user: str = input("Greatness: ").lower()
    
#Starting and Breaking
    
    if user == 'quit':
        break
    elif user == 'yeah':
        print(f"Nice, what shape you got??\n                A) Circle\n                B) Square\n                C) Triangle")
        
        try:
            option = input("option: ").lower()
            
#Area for Circle
            
            if option == 'a':
                radius = float(input("Enter the radius of the circle: "))
                area = np.pi * radius**2
                print(f"The area of the circle is {area}\nwana see the circle??")
                
#Plotting the Circle
                
                if input("see??: ").lower() == 'yeah':

                    plt.plot(radius * np.cos(np.linspace(0, 2 * np.pi, 100)), radius * np.sin(np.linspace(0, 2 * np.pi, 100)))
                    plt.xlabel("X-axis")
                    plt.ylabel("Y-axis")
                    plt.title("Circle")
                    plt.show()
                else:
                        print("Okay, maybe next time!")
                    
#Area for Square
            
            elif option == 'b':
                side = float(input("Enter the side length of the square: "))
                area = side**2
                print(f"The area of the square is {area}\nwana see the square??")
                
#Plotting the Square
                
                if input("see??: ").lower() == 'yeah':

                    plt.plot([0, side, side, 0, 0], [0, 0, side, side, 0])
                    plt.xlabel("X-axis")
                    plt.ylabel("Y-axis")
                    plt.title("Square")
                    plt.show()
                else:
                    print("Okay, maybe next time!")
                    
#Area for Triangle
            
            elif option == 'c':
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = 0.5 * base * height
                print(f"The area of the triangle is {area}\nwana see the triangle??")
                
#Plotting the Triangle
                
                if input("see??: ").lower() == 'yeah':

                    plt.plot([0, base, 0], [0, 0, height])
                    plt.xlabel("X-axis")
                    plt.ylabel("Y-axis")
                    plt.title("Triangle")
                    plt.show()
                else:
                    print("Okay, maybe next time!")

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print(f"{bot}: I don't understand that. Please type 'yeah' to find area or 'quit' to exit.")
    
