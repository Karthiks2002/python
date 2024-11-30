pi=3.1416
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

if num1>=num2 and num1>=num3:
   n=num1
elif num2>=num1 and num2>=num3:
   n=num2
else:
   n=num3
print(f"The biggest number is:{n}")
nn=n**2
nnn=n**3
print(f"n+nn+nnn={n}+{nn}+{nnn}")

radius=n
area=pi*radius**2
perimeter=2*pi*radius
print(f"Area of circle:{area}")
print(f"Perimeter of circle:{perimeter}")
volume=4/3*pi*radius**3
print(f"Volume of sphere:{volume}")