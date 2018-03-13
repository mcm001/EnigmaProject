#Enigma Machine Simulator
#By Matthew
#Function definitions
def lettertonumber(letter):
  charicter=ord(letter)-65
  return charicter
def numbertoletter(number):
  return chr(number+65)

#Plugboard. First element is the "A" setting, second is "B", etc
plugboard = ['A','Q','D','C','X','K','G','U','M','N','F','L','I','J','O','S','B','R','P','T','H','V','W','E','Z','Y']

#rotor definitions
rotorI = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]#list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotorII = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]#list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotorIII = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]#list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotorIV = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]#list("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotorV = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]#list("VZBRGITYUPSDNHLXAWMJQOFECK")


#Choose a rotor between 1 and 5 (Left to Right) here - this supports the Enigma 1 and M3.")
#Rotor definitions are above - just type in the name of the variable
#I.e. for rotor one, replace rotorII with rotorI. Make sure it's in Ruman Numerals!
rotor1= rotorI#input("What rotor do you want for Rotor 1?")
rotor2= rotorII#input("What rotor do you want for Rotor 2?")
rotor3= rotorIII#input("What rotor do you want for Rotor 3?")


#Rings are irrelivent.
#I'll do it later
#ring1= input("What is Rotor 1's Ring?")
#ring2= input("What is Rotor 3's Ring?")
#ring3= input("What is Rotor 3's Ring?")
#TODO: Rings


#Turn the plugboard into a 
plugboardnumbers = []
for x in range(len(plugboard)):
  plugboardnumbers.append(lettertonumber(plugboard[x]))
print("plug board settings: ")
print(plugboardnumbers)
print(" ")

#Input stuff. This line removes all the non-letters from the input.
input_charicter = list(''.join(filter(str.isalpha, ('abcdabcdzyx'.upper()) ) ))    #input("What is your message?").upper()  <== Use this instead later
print("Your message is: " + str(input_charicter))
input_ord = [] #This is our ordinal number list. We make it blank to start.
length = ((len(input_charicter))) #Input length
print("Your message length: " + str(length)) #Prints input length


for x in range(length): #This loop will turn the input charicters into numbers
  input_ord.append(lettertonumber(input_charicter[x]))
print("Your message in numbers:")
print(input_ord) #Prints our array which is a list of non-letters.

#Plug board stuff. So what we are going to need to do here is make a new list, take a number input, and replace it with the corrosponding index of the 'plugboard' list. 
plugboard_output=[]
for x in range(length):
  plugboard_output.append(  plugboardnumbers[input_ord[x]] )
print("Plug-boarded output")
print(plugboard_output)
















output=[]
for x in range(length):
  output.append(numbertoletter(plugboard_output[x]))
print("")
print("Output:")
print(output)
