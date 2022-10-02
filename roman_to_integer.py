# Conversion of 'Roman Number' to 'Integer Number'
def roman_to_int(roman_num):

    # all the basic roman values are mapped with their specific integer values
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    '''
    let roman_num = 'IV', so it's length is '2'
    Now current index(i=0) is at 'I', and since (i>0) and not greater than (i-1), so int_val+=1
    Now current index(i=1) is at 'V', and since (i>0) and also greater than (i-1), so int_val+=(5-2*(1)) i.e, int_val+=3
    SO the final value of int_val is = 0+1+3 = 4.

    '''
    for i in range(len(roman_num)):
        if i > 0 and rom_val[roman_num[i]] > rom_val[roman_num[i - 1]]:
            int_val += rom_val[roman_num[i]] - 2 * rom_val[roman_num[i - 1]]
        else:
            int_val += rom_val[roman_num[i]]

    # here we return our answer
    return (int_val)




