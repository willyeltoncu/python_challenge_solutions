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
        for idx in range(len(data2D)-3):
            for iidx in range(len(data2D[idx])-2):
                up_left , up_mid , up_right,  mid_lef, mid_mid , mid_right, bot_left, bot_mid, bot_right = data2D[idx][iidx], data2D[idx][iidx+1], data2D[idx][iidx+2],  data2D[idx+1][iidx] , data[idx+1][iidx+1], data2D[idx+1][iidx+2] , data2D[idx+2][iidx] , data[idx+2][iidx+1], data2D[idx+2][iidx+2] 
                print(up_left , up_mid , up_right,  mid_lef, mid_mid , mid_right, bot_left, bot_mid, bot_right)
                print("\n")
                if mid_mid.islower() and (up_mid.isupper() + mid_lef.isupper()+ mid_right.isupper() + bot_mid.isupper()) == 3: 
                    return mid_mid
                
        
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)

    return "BALLS"
