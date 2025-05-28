'''
Write a python program to Create Animal Class
'''
class Animal:
Animal_Name="Dog"
Animal_Breed="Neapolitan Mastiff"
Animal_Size="Large"
Animal_Color="Black"

def display(self):
print("Animal_Name:",self.Animal_Name)
print("Animal_Breed:",self.Animal_Breed)
print("Animal_Size:",self.Animal_Size)
print("Animal_Color:",self.Animal_Color)
e=Animal()
e.display()
