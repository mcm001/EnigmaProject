#Enigma Machine Simulator
#By Matthew
x=0
#Input settings
print("We're going to set the rotor settings now.")
print("Choose a rotor between 1 and 5 (Left to Right) for now - this supports the Enigma 1 and M3.")
#TODO: Enigma M4 support

rotor1= "1"#input("What rotor do you want for Rotor 1?")
rotor2= '2'#input("What rotor do you want for Rotor 2?")
rotor3= '3'#input("What rotor do you want for Rotor 3?")

#Rings are irrelivent.
#I'll do it later
#ring1= input("What is Rotor 1's Ring?")
#ring2= input("What is Rotor 3's Ring?")
#ring3= input("What is Rotor 3's Ring?")
#TODO: Rings

#We aren't going to worry about the plugboard for now
print("Plugboards are for noobs.")
#Coz it's hard and stupid

#rotor definitions
rotorI = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotorII = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotorIII = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotorIV = list("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotorV = list("VZBRGITYUPSDNHLXAWMJQOFECK")


#Input stuff
input_charicter = input("What is your message?").upper()
#print(input_charicter)
#print(list(input_charicter)) #Sanity check
#This line just takes your input_charicter and spits out an array. I.e. hello ==> ['h', 'e', 'l', 'o']

length = ((len(input_charicter)))
while  x < (length):
  charicter=ord(input_charicter[x])-65
  print(charicter)
  x=x+1
