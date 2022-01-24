# python_hex_parse

[TOC]

# Python ord()函數

ord() 函數可以將單一字元(utf-8)字串轉換成10進制int值

輸入參數雖然是 string型別,但是只限一個"utf-8字元",不然執行的時候會報錯

---

輸入: string (1 character only)

輸出: int 

```python
c = 'A'
out_value = ord(c)
print(out_value)  

#output: 65
```



# Python hex()函數

hex()函數可以將int數值轉換成16進制string

---

輸入: int

輸出: string 

```python
dec = 10
hex_str = hex(dec)
print(hex_str.upper())   #轉成大寫字母

#output: 0xA  
```



# 將utf-8字串轉換成HEX字串

```python

def utf8_str_covert_to_hex_str(str_in):
    str_out = ""
    for c in str_in:        
        str_out += hex(ord(c)) + " "
    
    return str_out
    
if __name__ == '__main__':
    str = 'Hello world'
    str_hex = utf8_str_covert_to_hex_str(str)
    print(str_hex)

#output: 0x48 0x65 0x6c 0x6c 0x6f 0x20 0x77 0x6f 0x72 0x6c 0x64 
```



# 將HEX字元轉換成int整數 

```python
hex_str = "0xA"
int_hex = int(hex_str, 16)
print(int_hex)

#output 10   
```



