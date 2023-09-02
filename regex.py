alphabet = " \n\tabcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\b~!@#$%^&*()_+[]\{}|;':,.//<>?"
numbers = "0123456789"

def z(string,pattern):
    
    index_sierra = 0
    index_pascal = 0
    index_pascal_1 = index_pascal
    
    return_string = ""
    
    while index_sierra < len(string):
        while index_pascal < len(pattern):
            bravo = 1
            if pattern[index_pascal] == '*':
                index_pascal += 1
                try:
                    k = ""
                    
                    while pattern[index_pascal] in numbers and index_pascal < len(pattern):
                        k += pattern[index_pascal]
                        index_pascal += 1
                    
                    index_sierra_1 = index_sierra + int(k)

                    while index_sierra < index_sierra_1:
                        return_string += string[index_sierra]
                            
                        index_sierra += 1
                        
                    index_pascal -= 1
                    
                except: 
                    return ""
                    
            elif pattern[index_pascal] == '[':
                try:
                    
                    index_pascal_1 = index_pascal + 3
                    
                    k = ""
                    
                    c = pattern[index_pascal:index_pascal_1]
                    pattern[index_pascal_1] in numbers == True
                    
                    while index_pascal_1 < len(pattern):
                        if pattern[index_pascal_1] in numbers:
                            k += pattern[index_pascal_1]
                        
                            index_pascal_1 += 1
                        else:
                            break
                    
                    index_sierra + int(k) <= len(string) == True
                    
                    while index_sierra < int(k):
                        sierra = alphabet.index(string[index_sierra])
                        
                        if sierra >= alphabet.index(pattern[index_pascal + 1]) and sierra <= alphabet.index(pattern[index_pascal + 2]):
                            return_string += string[index_sierra]
                    
                        index_sierra += 1
                    
                except:
                    return ""
                    
            else:
                index_pascal_1 = index_pascal + 1
                
                while index_pascal_1 < len(pattern) and not(pattern[index_pascal_1] == '*' or pattern[index_pascal_1] == '['):
                    index_pascal_1 += 1
                
                try:
                    delta_pascal = index_pascal_1 - index_pascal

                    if pattern[index_pascal:index_pascal_1] == string[index_sierra:index_sierra + delta_pascal]:
                        return_string += string[index_sierra:index_sierra + delta_pascal]
                        
                    index_sierra += delta_pascal
                except:
                    return ""
                
            index_pascal += 1
        index_sierra += 1
        
    return return_string
    
def zF(string,pattern):
    
    if string == z(string,pattern):
        return string
    else:
        return ""