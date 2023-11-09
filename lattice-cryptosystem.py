"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""

import sys
import math
from os import system



# Créer un dictionnaire  vide
dict_params = dict()
 
# Remplissez-le avec quelques valeurs

dict_params['n'] = 509
dict_params['l'] = 1
dict_params['q'] = 512
dict_params['d'] = 2
dict_params['v'] = 9
dict_params['etatD'] = 2
dict_params['tauR'] = 140
dict_params['tauG'] = 140



def display_menu(menu):
    """
    Display a menu where the key identifies the name of a function.
    :param menu: dictionary, key identifies a value which is a function name
    :return:
    """
    for k, function in menu.items():
        print(k, function.__name__)


def lwe():
    # remplir la valeur de p dans le dictionnaire
    dict_params['p'] = 2
    #LWE cryptosystem
    print("LWE Cryptosystem")
    print("######## Generate Parameters ########") # Simulate function output.
   
    
    # Calculate Public Key(Pk) , taillePk= (n*v*l^2)/8  en octets
    Pk = dict_params['n']*dict_params['v']*dict_params['l']**2/8

    # Calculate Delta(δ) ,   δ = l*((tauR*etatD)+p*2^(d-1)*tauG)
    δ = dict_params['l']*((dict_params['tauR'])*(dict_params['etatD'])+dict_params['p']*2**(dict_params['d']-1)*dict_params['tauG'])


    # Calculate  Cipher (C) , C =
    C =32+ dict_params['n']*dict_params['l']*((dict_params['v'])-(dict_params['d']))/8


    # Calculate  Probability(Prob) , Prob = -266.3018282954434
    Prob = math.log((1-(((dict_params['q']-1)/(2*δ))))**(dict_params['n']*dict_params['l']),2)




    for cle, valeur in dict_params.items():
        print(" ", cle, "=", valeur)
    

    print("######## Generate Public Key  ########")
    print(" ", "Pk", "=", Pk)

   
    print("######## Generate Delta(δ)  ########")
    print(" ", "δ", "=", δ)


    print("######## Generate Cipher(C)  ########")
    print(" ", "C", "=", C)


    print("######## Generate Probability(Prob)  ########")
    print(" ", "Prob", "=", Prob)

 
    print("\n")
    print("Finish LWE Cryptosystem")
    print("\n")
    input("Press Enter to Continue \n")
    system('cls')  # clears stdout
 

def ntru():
    # remplir la valeur de p dans le dictionnaire
    dict_params['p'] = 3
    #LWE cryptosystem
    print("NTRU Cryptosystem")
    print("######## Generate Parameters ########") # Simulate function output.
   
    
    # Calculate Public Key(Pk) , Pk = 572.625
    Pk = ((dict_params['n'])*((dict_params['v'])*((dict_params['l'])**2)))/8

    # Calculate Delta(δ) ,   δ = 1120
    δ = (dict_params['l'])*(((dict_params['tauR'])*(dict_params['etatD']))+((dict_params['p'])*(2**(dict_params['d']-1))*(dict_params['tauG'])))


    # Calculate  Cipher (C) , C = 445.375
    C = (((dict_params['n'])*(dict_params['l']))*((dict_params['v'])-(dict_params['d'])))/8


    # Calculate  Probability(Prob) , Prob = -190.14247942106653
    Prob = math.log((1-(((dict_params['q']-1)/(2*δ))))**(dict_params['n']*dict_params['l']),2)




    for cle, valeur in dict_params.items():
        print(" ", cle, "=", valeur)
    
    print("######## Generate Public Key  ########")
    print(" ", "Pk", "=", Pk)

   
    print("######## Generate Delta(δ)  ########")
    print(" ", "δ", "=", δ)


    print("######## Generate Cipher(C)  ########")
    print(" ", "C", "=", C)


    print("######## Generate Probability(Prob)  ########")
    print(" ", "Prob", "=", Prob)

 
    print("\n")
    print("Finish NTRU Cryptosystem")
    print("\n")
    input("Press Enter to Continue \n")
    system('cls')  # clears stdout


def ntru_prime():
    # remplir la valeur de p dans le dictionnaire
    dict_params['p'] = 2
    #LWE cryptosystem
    print("NTRU Prime Cryptosystem")
    print("######## Generate Parameters ########") # Simulate function output.
   
    
    # Calculate Public Key(Pk) , Pk = 572.625
    Pk = ((dict_params['n'])*((dict_params['v'])*((dict_params['l'])**2)))/8

    # Calculate Delta(δ) ,   δ = 1120 
    δ = ((2*dict_params['l'])*((dict_params['tauR'])*(dict_params['etatD'])))+((dict_params['p'])*((2**(dict_params['d']-1))*(dict_params['tauG'])))


    # Calculate  Cipher (C) , C = 445.375
    C = (((dict_params['n'])*(dict_params['l']))*((dict_params['v'])-(dict_params['d'])))/8


    # Calculate  Probability(Prob) , Prob = -190.14247942106653
    Prob = math.log((1-(((dict_params['q']-1)/(2*δ))))**(dict_params['n']*dict_params['l']),2)




    for cle, valeur in dict_params.items():
        print(" ", cle, "=", valeur)
    
    print("######## Generate Public Key  ########")
    print(" ", "Pk", "=", Pk)

   
    print("######## Generate Delta(δ)  ########")
    print(" ", "δ", "=", δ)


    print("######## Generate Cipher(C)  ########")
    print(" ", "C", "=", C)


    print("######## Generate Probability(Prob)  ########")
    print(" ", "Prob", "=", Prob)

 
    print("\n")
    print("Finish LWE Cryptosystem")
    print("\n")
    input("Press Enter to Continue \n")
    system('cls')  # clears stdout


def quitter():
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    # Create a menu dictionary where the key is an integer number and the
    # value is a function name.
    functions_names = [lwe, ntru, ntru_prime, quitter]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        print("Lattice-based cryptography:  \n")
        display_menu(menu_items)
        selection = int(
            input("Please choice your cryptosystem: \n"))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function


if __name__ == "__main__":
    main()