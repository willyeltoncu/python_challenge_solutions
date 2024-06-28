import requests
print(2**38) ##Basic math for step 1

def url_print(answ):
    print(f"Latest url for python challenge: http://www.pythonchallenge.com/pc/def/%s.html \n" % (answ)) ## clickable/pastable link function

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
    print(f"The unique characters of this huge set (%d items)  of junk are: %s  \nFiltering...."% (len(junk), set(junk)))
    result = ""
    for char in junk: 
        char_order = ord(char)
        if char_order >= ord('a') and char_order <= ord('z'):
            result += char
    return result

## Algo is : --> grab page source --> push data into 2D array, filter for lowercase surronded by EXACTLY 3 UPPERcase daddies 
def fourth_step(url): ## this function searches a 3X3 area of the 2D char array, checking for a  
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the HTML source code
        # print(response.text, len(response.text), type(response.text), (response.text).shape)
        req = response.text
        start_val = req.find("<!--\n") + len("<!--\n")
        end_val = req.find("-->") 
        data = req[start_val:end_val].split('\n')
        data2D = [[*row] for row in data] ## Unpack each element(string) into its components(chars) row by row for 2D array type behavior
        print(data2D[0])
        for idx in range(len(data2D)-2):
            for iidx in range(len(data2D[idx])-2):
                up_left , up_mid , up_right,  mid_lef, mid_mid , mid_right, bot_left, bot_mid, bot_right = data2D[idx][iidx], data2D[idx][iidx+1], data2D[idx][iidx+2],  data2D[idx+1][iidx] , data[idx+1][iidx+1], data2D[idx+1][iidx+2] , data2D[idx+2][iidx] , data[idx+2][iidx+1], data2D[idx+2][iidx+2] 
                print(up_left , up_mid , up_right,  mid_lef, mid_mid , mid_right, bot_left, bot_mid, bot_right)
                print("\n")
            
        
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

    return "BALLS"











def main(): ## Main function used to call step specfic functions and present the info nicely... 
    ##Step 2 presentation
    file = open("step2_crypt.txt") ##Info found in the page source of step 2 pythongchallenge.com
    str1 = file.read()
    print("The encrpyted message: \n", str1)
    round_2_solution =  basic_decrypt(str1, 2)
    print(f"The decrypted message: \n \n %s" % (round_2_solution))
    # print(f"\n\n The latest URL ending for python challenge is : %s  \n\n" % (basic_decrypt("map",2)))
    url_print(basic_decrypt("map",2))
    file.close()
    ##Step 3 presentation
    file = open("step3_mess.txt") ##Info found in the page source of step 3 pythongchallenge.com
    mess_to_sort_through = file.read()
    url_print(step_tree(mess_to_sort_through))
    file.close()

    # print(mess_to_sort_through)
    ##Step 4 presentation. 
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'
    url_print(fourth_step(url))
    



if __name__ == "__main__":
    main()

