
# import this
# print(this.d)
# print(this.s)
# ============================Variables=================================================================

code = """Gur Mra bs Clguba, ol Gvz Crgref. \n
Ornhgvshy vf orggre guna htyl. \nRkcyvpvg vf orggre guna vzcyvpvg.\t 
Fvzcyr vf orggre guna pbzcyrk. \nPbzcyrk vf orggre guna pbzcyvpngrq.\t 
Syng vf orggre guna arfgrq. \nFcnefr vf orggre guna qrafr. \nErnqnovyvgl pbhagf.\t 
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf. \nNygubhtu cenpgvpnyvgl orngf chevgl.\t 
Reebef fubhyq arire cnff fvyragyl. Hayrff rkcyvpvgyl fvyraprq. \nVa gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.\t 
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.\t 
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu. \nAbj vf orggre guna arire.\t 
Nygubhtu arire vf bsgra orggre guna evtug abj. \nVs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.\t 
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn-- \nAnzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

key = {',':',','\n':'\n','\t':'\t','\'':'\'','!':'!', '-':'-', '.':'.', ' ': ' ', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
        'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 
        'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', 'a': 'n', 'b': 'o', 
        'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 
        'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 
        'y': 'l', 'z': 'm'}
#=====================Custom split function================================================================

def convert(string):
    list1=[] #.....................creates an empty list
    list1[:0]=string #.............compresses the list and includes the spaces; as opposed to the split() method
    return list1 #.................returns the list

#=====================spliting the code variable=========================================================

code2 = convert(code) #...........splits the code variable using the convert() function 

#===================Decryption=============================================================================
new_list=[] #...............................creates an empty list
for char in code2: #.....................loops through the code2(encrypted) list
    if char in key:
        new_list.append(key[char]) #...........checks the keys and appends the decrypted value to the new_list

result = ''.join(new_list) #................converts the list into a string
print(result) #.......................print the result


