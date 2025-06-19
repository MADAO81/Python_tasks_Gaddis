# File encryption and decryption. 
# Write a program that uses a dictionary to assign "codes" to each letter of the alphabet.
# The program should open a given text file, read its contents, 
# and use a dictionary to write an encrypted version of the file contents to a second file.

CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}

def main():
    # get string value of text 
    result = convert()
    
    # Write text to the screen
    print(result)
    
# The convert function asks the user for the file name, 
# opens the file, and converts its contents using the CODE dictionary. 
# It then returns a string of converted text.
def convert():
    input_name = input("Enter the name of input file: ")
    
    input_file = open("data\\" + input_name, "r")
    
    result = ""
    text = input_file.read()
    
    # If the character is a space, it is not converted; otherwise, convert.
    for ch in text:
        
        if ch.isspase():
            result = result + ch 
        else: 
            result = result + CODE[ch]
            
        return result
        
# call main function
main()

    
  