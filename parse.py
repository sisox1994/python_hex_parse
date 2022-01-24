def utf8_str_covert_to_hex_str(str_in):
    str_out = ""
    for c in str_in:        
        str_out += hex(ord(c)) + " "
    
    return str_out
    

if __name__ == '__main__':
    str = 'Hello world'
    str_hex = utf8_str_covert_to_hex_str(str)
    print(str_hex)


