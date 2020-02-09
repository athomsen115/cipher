#!/usr/bin/env python
import pycipher

def main_menu():
    menu = {}
    menu['1'] = "Substitution Ciphers"
    menu['2'] = "Transposition Ciphers"
    menu['3'] = "Nomenclature Ciphers"
    menu['4'] = "Polyalphabetic Ciphers"
    menu['5'] = "Other Ciphers"
    menu['99'] = "Quit"
    options=menu.keys()
    options.sort()
    for entry in optins:
        print entry, menu[entry]

        selection = input("Please select a cipher type [1-5]: ")
        if selection == '1':
            print("You have selected Substitution Ciphers.")
            substitution_menu()


        elif selection == '2':
            print("You have selected Transposition Ciphers.")
            transposition_menu()


        elif selection == '3':
            print("You have selected Code and Nomenclature Ciphers.")
            nomenclature_menu()


        elif selection == '4':
            print("You have selected Polyalphabetic Ciphers.")
            polyalphabetic_menu()


        elif selection == '5':
            print("You have selected ciphers that just don't quite fit.")
            other()

        elif selection == '99':
            print("Goodbye!")
            break

        def substitution_menu():
            sub_menu = {}
            sub_menu['1'] = "Simple Substitution Cipher"    #pycipher
            sub_menu['2'] = "Atbash Cipher" #pycipher
            sub_menu['3'] = "Affine Cipher" #pycipher
            sub_menu['4'] = "Playfair Cipher" #pycipher
            sub_menu['5'] = "Polybius Square Cipher"    #pycipher
            sub_menu['6'] = "Baconian Cipher"
            sub_menu['7'] = "Straddle Checkerboard Cipher"
            sub_menu['99'] = "Return to main menu"
            options=sub_menu.keys()
            options.sort()
            for entry in optins:
                print entry, sub_menu[entry]
                selection = input("Please select a cipher to use [1-7]: ")
                if selection == '1':
                    print("You have selected Simple Substitution Cipher.")


                elif selection == '2':
                    print("You have selected Atbash Cipher.")


                elif selection == '3':
                    print("You have selected Affine Cipher.")


                elif selection == '4':
                    print("You have selected Playfair Cipher.")


                elif selection == '5':
                    print("You have selected Polybius Square Cipher.")


                elif selection == '6':
                    print("You have selected Baconian Cipher.")

                elif selection == '7':
                    print("You have selected Straddle Checkerboard Cipher.")


                elif selection == '99':
                    main_menu()


                    def transposition_menu():
                        trans_menu = {}
                        trans_menu['1'] = "Rail-Fence Cipher"   #pycipher
                        trans_menu['2'] = "Columnar Transposition Cipher"   #pycipher
                        trans_menu['3'] = "ADFGVX Cipher"   #pycipher
                        trans_menu['4'] = "ADFGX Cipher"    #pycipher
                        trans_menu['5'] = "Bifid Cipher"    #pycipher
                        trans_menu['6'] = "Trifid Cipher"
                        trans_menu['99'] = "Return to main menu"
                        options=sub_menu.keys()
                        options.sort()
                        for entry in optins:
                            print entry, sub_menu[entry]
                            selection = input("Please select a cipher to use [1-6]: ")
                            if selection == '1':
                                print("You have selected Rail-Fence Cipher.")


                            elif selection == '2':
                                print("You have selected Columnar Transposition Cipher.")


                            elif selection == '3':
                                print("You have selected ADFGVX Cipher.")


                            elif selection == '4':
                                print("You have selected ADFGX Cipher.")


                            elif selection == '5':
                                print("You have selected Bifid Cipher.")


                            elif selection == '6':
                                print("You have selected Trifid Cipher.")


                            elif selection == '99':
                                main_menu()

                                def nomenclature_menu():
                                    nom_menu = {}
                                    nom_menu['1'] = "Nomenclature Cipher"
                                    nom_menu['2'] = "Code Cipher"
                                    nom_menu['99'] = "Return to main menu"
                                    options=sub_menu.keys()
                                    options.sort()
                                    for entry in optins:
                                        print entry, sub_menu[entry]
                                        selection = input("Please select a cipher to use [1-2]: ")
                                        if selection == '1':
                                            print("You have selected Nomenclature Cipher.")
                                            substitution_menu()


                                        elif selection == '2':
                                            print("You have selected Code Ciphers.")

                                        elif selection == '99':
                                            main_menu()


                                            def polyalphabetic_menu():
                                                poly_menu = {}
                                                poly_menu['1'] = "Autokey Cipher"   #pycipher
                                                poly_menu['2'] = "Vignere Cipher"   #pycipher
                                                poly_menu['3'] = "Gronsfield Cipher" #pycipher
                                                poly_menu['4'] = "Beaufort Cipher"  #pycipher
                                                poly_menu['5'] = "Porta Cipher"     #pycipher
                                                poly_menu['6'] = "Running Key Cipher"
                                                poly_menu['99'] = "Return to main menu"
                                                options=sub_menu.keys()
                                                options.sort()
                                                for entry in optins:
                                                    print entry, sub_menu[entry]
                                                    selection = input("Please select a cipher to use [1-6]: ")
                                                    if selection == '1':
                                                        print("You have selected Autokey Cipher.")


                                                    elif selection == '2':
                                                        print("You have selected Vignere Cipher.")


                                                    elif selection == '3':
                                                        print("You have selected Gronsfield Cipher.")


                                                    elif selection == '4':
                                                        print("You have selected Beaufort Cipher.")


                                                    elif selection == '5':
                                                        print("You have selected Porta Cipher.")


                                                    elif selection == '6':
                                                        print("You have selected Running Key Cipher.")


                                                    elif selection == '99':
                                                        main_menu()

                                                        def other():
                                                            other_menu = {}
                                                            other_menu['1'] = "ROT13 Cipher"    #pycipher
                                                            other_menu['2'] = "Caesar Cipher"   #pycipher
                                                            other_menu['3'] = "Four-Square Cipher"  #pycipher
                                                            other_menu['4'] = "Enigma M3 Cipher"    #pycipher
                                                            other_menu['5'] = "M-209 Cipher"    #pycipher
                                                            other_menu['6'] = "Base64 Cipher"
                                                            other_menu['7'] = "Hill Cipher"
                                                            other_menu['99'] = "Return to main menu"
                                                            options=sub_menu.keys()
                                                            options.sort()
                                                            for entry in options:
                                                                print entry, sub_menu[entry]
                                                                selection = input("Please select a cipher to use [1-7]: ")
                                                                if selection == '1':
                                                                    print("You have selected ROT13 Cipher.")
                                                                    substitution_menu()


                                                                elif selection == '2':
                                                                    print("You have selected Caesar Cipher.")


                                                                elif selection == '3':
                                                                    print("You have selected Four-Square Cipher.")


                                                                elif selection == '4':
                                                                    print("You have selected Enigma M3 Cipher.")


                                                                elif selection == '5':
                                                                    print("You have selected M-209 Cipher.")


                                                                elif selection == '6':
                                                                    print("You have selected Base64 Cipher.")

                                                                elif selection == '7':
                                                                    print("You have selected Hill Cipher.")

                                                                elif selection == '99':
                                                                    main_menu()

                                                                    if __name__() == __main__():
                                                                        while True:
                                                                            main_menu()

