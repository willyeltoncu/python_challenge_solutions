print(2**38) ##Basic math for step 1

def basic_decrypt(raw_bare_text_scrambled, shift): ##Used for the basic cypher of step 2 of pythonchallenge.com
    return_str = ""
    
    for char in raw_bare_text_scrambled: 
        char_order = ord(char)
        if char_order >= ord('a') and char_order <= ord('z'): ##ONLY SHIFT LETTER, not puncts or other charcters.. 
            shifted_val = char_order + shift
            if shifted_val > 122: 
                shifted_val = shifted_val - 26
            if shifted_val < 97: 
                shifted_val = shifted_val + 26
        
            return_str += chr(shifted_val)
        else: 
            return_str += char
    return return_str

    # for i in range(10):
    #     print(i, chr(ord('k') +i))

def step_tree(junk): ##Filter function for step three of python challenge.. 
    print(f"The unique characters of this huge set of junk are: %s "% (set(junk)))
    for char in junk: 
        char_order = ord(char)
        if char_order >= ord('a') and char_order > 

def main(): ## Main function used to call step specfic functions and present the info nicely... 
    ##Step 2 presentation
    file = open("step2_crypt.txt")
    str1 = file.read()
    print("The encrpyted message: \n", str1)
    round_2_solution =  basic_decrypt(str1, 2)
    print(f"The decrypted message: \n \n %s" % (round_2_solution))
    print(f"\n\n\n The new URL ending for python challenge is : %s  \n\n" % (basic_decrypt("map",2)))
    file.close()
    ##Step 3 presentation
    file = open("step3_mess.txt")
    mess_to_sort_through = file.read()
    step_tree(mess_to_sort_through)




if __name__ == "__main__":
    main()

