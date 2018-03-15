#Enigma Machine Simulator
#By Matthew
#Function definitions
listlen26 = list('00000000000000000000000000')
def lettertonumber(letter):
  charicter=ord(letter)-65
  return charicter
def numbertoletter(number):
  if number < 26:
    return chr(number+65)
  if number >= 26:
    return chr(number+65-26)
def shift_list(array, s):
    s %= len(array)
    return (array[s:] + array[:s])
def reciprocaltable(array):
  array2=listlen26
  for x in range(len(array)):
    array2[rotorI[x]]=x
  return array2

#Plugboard. First element is the "A" setting, second is "B", etc
plugboard = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


#rotor definitions
rotorI = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]#list("EKMFLGDQVZNTOWYHXUSPAIBRCJ") Notch:  = 16
rotorII = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]#list("AJDKSIRUXBLHWTMCQGZNPYFVOE") Notch: E = 4
rotorIII = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]#list("BDFHJLCPRTXVZNYEIWGAKMUSQO") Notch: V = 21
rotorIV = [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]#list("ESOVPZJAYQUIRHXLNFTGKDCMWB") Notch: J = 9
rotorV = [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]#list("VZBRGITYUPSDNHLXAWMJQOFECK") Notch: Z = 25
#Reflector definition
UKWA = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]
UKWB = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
UKWC = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

#Choose a rotor between 1 and 5 (Left to Right) here - this supports the Enigma 1 and M3.")
#Rotor definitions are above - just type in the name of the variable
#I.e. for rotor one, replace rotorII with rotorI. Make sure it's in Ruman Numerals! This just defines the starting state.
rotor1state = rotorI#input("What rotor do you want for Rotor 1?")
rotor2state = rotorII#input("What rotor do you want for Rotor 2?")
rotor3state = rotorIII#input("What rotor do you want for Rotor 3?")
rotor1notch = 16
rotor2notch = 4
rotor3notch = 21
#MAKE SURE if you update the rotors, update the notches accordingly
reflector = UKWB

print("Rotor starting position. Make sure they are capital letters!")
rotor1start = lettertonumber('A')
rotor2start = lettertonumber('A')
rotor3start = lettertonumber('Z')
print("Rotor starting positions: " + str(numbertoletter(rotor1start)) + ", " + str(numbertoletter(rotor2start)) + ", " + str(numbertoletter(rotor3start)) + ".")
print("-----------------")

#Make reciprocal rotor tables. We do this for rotor 1, 2 and 3 (NOT I, II and III), so it's as modular as possible.
reciprocalrotor1state = reciprocaltable(rotor1state)
reciprocalrotor2state = reciprocaltable(rotor2state)
reciprocalrotor3state = reciprocaltable(rotor3state)

#Rotate the rotors to the starting positions
#What we do is rotate by the ordinal of the lettertonumber
rotor1state = shift_list(rotor1state,(rotor1start))
rotor2state = shift_list(rotor2state,(rotor2start))
rotor3state = shift_list(rotor3state,(rotor3start))


#Turn the plugboard into a 
plugboardnumbers = []
for x in range(len(plugboard)):
  plugboardnumbers.append(lettertonumber(plugboard[x]))
print("plug board settings: ")
print(plugboardnumbers)
print("-----------------")

#Input stuff. This line removes all the non-letters from the input.
input_charicter = list(''.join(filter(str.isalpha, ('A'.upper()) ) ))    #input("What is your message?").upper()  <== Use this instead later
print("Your message is: " + str(input_charicter))
input_ord = [] #This is our ordinal number list. We make it blank to start.
length = ((len(input_charicter))) #Input length
print("Your message length: " + str(length)) #Prints input length


for x in range(length): #This loop will turn the input charicters into numbers
  input_ord.append(lettertonumber(input_charicter[x]))
print("Your message in numbers: " + str(input_ord))


#Plug board stuff. So what we are going to need to do here is make a new list, take a number input, and replace it with the corrosponding index of the 'plugboard' list. 
plugboard_output=[]

output=[]
#Main loop here! It will repeat (length of message) times. First, it will step the rotors forward and that jazz. Next, plugboard. Then it will put the message through the 1st rotor, then the 2nd rotor, then 3rd, then the reflector, then the 3rd rotor, 2nd, 1st, plugboard, and then appends that to the output array. Next, we do the same thing with the second charicter - shift the rotors, go through plugboard, all that jazz. Rince and repeat ;)
rotor1pos = rotor1start
rotor2pos = rotor2start
rotor3pos = rotor3start
print("-----------------")
print("The current state of the rotors:")
print(str(numbertoletter(rotor1pos)))
print(str(numbertoletter(rotor2pos)))
print(str(numbertoletter(rotor3pos)))
print("-----------------")
print("LOOP INIT!")
for x in range(length):
  stepR1 = False
  stepR2 = False
  stepR3 = False
  
  #Rotor stepping logic
  #REMEMBER! The rotors go Reflector - Rotor1 - Rotor2 - Rotor3!
  
  #Rules per the paper enigma page:   
  #To handle turnover correctly, we need to add to our instructions above for turning the rotors, based on the letters showing in line with the grey bars:
    
    #If the letter on the middle rotor is shaded grey, turn all three rotors one step towards you,
    
    #otherwise, if the letter on the right-hand rotor is shaded grey, turn the middle and right-hand rotors one step towards you,
    
    #otherwise, turn just the right-hand rotor one step towards you.
    
  #The shading of the letter on the left-hand rotor doesn't matter; it would only come in to play if that rotor was in a different place in the order.

  if rotor2pos == rotor2notch:
    stepR1 = True
    stepR2 = True
    stepR3 = True
  elif rotor3pos == rotor3notch:
    stepR2 = True
    stepR3 = True
  else:
    stepR3 = True
  print("Loop iteration: " + str(x))
  print("R1 step is " + str(stepR1))
  print("R2 step is " + str(stepR2))
  print("R3 step is " + str(stepR3))
  
  
  #Array rotation stuff
  if stepR1 == True:
    #Rotate rotor 1's array
    rotor1state = shift_list(rotor1state, 1)
    rotor1pos = rotor1pos + 1
    print("Rotor 1 has stepped!")
  if stepR2 == True:
    #Rotate rotor 2's array
    rotor2state = shift_list(rotor2state, 1)
    print("Rotor 2 has stepped!")
    rotor2pos = rotor2pos + 1
  if stepR3 == True:
    #Rotate rotor 3's array
    rotor3state = shift_list(rotor3state, 1)
    rotor3pos = rotor3pos + 1
    print("Rotor 3 has stepped! Position: " + str(numbertoletter(rotor3pos)))
  #OK, all the rotations are done. Now we gotta put the letter through the Enimga's stepped path. First, figure out what letter we're rotating
  thingWeAreManipulating = input_ord[x]
  print("We start with " + str(numbertoletter(thingWeAreManipulating)) + ".")
  #First, the plugboard!
  thingWeAreManipulating = plugboardnumbers[thingWeAreManipulating]
  print("After the plugboard, we get " + str(numbertoletter(thingWeAreManipulating)))
  #Next, rotor 1, 2 and 3!
  thingWeAreManipulating = rotor3state[thingWeAreManipulating]
  print("After the right rotor, we get " + str(numbertoletter(thingWeAreManipulating)))
  thingWeAreManipulating = rotor2state[thingWeAreManipulating]
  print("After the middle rotor, we get " + str(numbertoletter(thingWeAreManipulating)))
  thingWeAreManipulating = rotor1state[thingWeAreManipulating]
  print("After the left rotor, we get " + str(numbertoletter(thingWeAreManipulating)))
  #Reflector!
  thingWeAreManipulating = reflector[thingWeAreManipulating]
  print("After the reflector, we get " + str(numbertoletter(thingWeAreManipulating)))
  #Back through 3, 2 and 1!
  thingWeAreManipulating = rotor1state[thingWeAreManipulating]
  print("After the left rotor again, we get " + str(numbertoletter(thingWeAreManipulating)))
  thingWeAreManipulating = rotor2state[thingWeAreManipulating]
  print("After the middle rotor again, we get " + str(numbertoletter(thingWeAreManipulating)))
  thingWeAreManipulating = rotor3state[thingWeAreManipulating]
  print("After the right rotor again, we get " + str(numbertoletter(thingWeAreManipulating)))
  #Plugboard(agan)
  thingWeAreManipulating = plugboardnumbers[thingWeAreManipulating]
  print("After the plugboard (again), we get " + str(numbertoletter(thingWeAreManipulating)))
  #Huzzah! Ok. Now append to the output list and do it all agian
  output.append(thingWeAreManipulating)
  
  print("-----------------")
  
print("")
print("Output:")
outputString=[]
for x in range(length):
  outputString.append(numbertoletter(output[x]))
outputMeme= " ".join(outputString)
print(''.join(filter(str.isalpha, ((str(outputMeme)).upper()) ) ))   


