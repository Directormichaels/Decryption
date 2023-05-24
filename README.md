# Decryption challenge

The variable `code` contains a multiline string in an encrypted format.
The variable `key` is a dictionary containing decryption keys to decode the text stored in the code variable  

There are three general steps:
- convert the `code` string into a list.<br>
- loop through the list and compare its values with the key dictionary
- convert the resulting list back into a string

<br>

The key dictionary contains only `[a-z][A-Z]` characters and does not contain  special characters, spaces, tabs or newlines.<br>
So you would have to modify the key dictionary to contain all you need to make the output as good as possible. 

.
<br>
.
<br>
.
<br>
.

The original format can be obtained by importing the `this` module.
```
import this
print(this.s)
print(this.d)
```
- the first command `import this` gives a poem  _**The Zen of Python, by Tim Peters.**_<br>


>The Zen of Python, by Tim Peters  <br>
>Beautiful is better than ugly.
>Explicit is better than implicit.  
>Simple is better than complex.  
>Complex is better than complicated.  
>Flat is better than nested.  
>Sparse is better than dense.  
>Readability counts.  
>Special cases aren't special enough to break the rules.  
>Although practicality beats purity.  
>Errors should never pass silently.  
>Unless explicitly silenced.  
>In the face of ambiguity, refuse the temptation to guess.  
>There should be one-- and preferably only one --obvious way to do it.  
>Although that way may not be obvious at first unless you're Dutch.  
>Now is better than never.  
>Although never is often better than *right* now.  
>If the implementation is hard to explain, it's a bad idea.  
>If the implementation is easy to explain, it may be a good idea.  
>Namespaces are one honking great idea -- let's do more of those! 


- running the `print(this.s)` command outputs a bunch of encrypted text.<br>
>Gur Mra bs Clguba, ol Gvz Crgref<br>
>
>Ornhgvshy vf orggre guna htyl.<br>
>Rkcyvpvg vf orggre guna vzcyvpvg.<br>
>Fvzcyr vf orggre guna pbzcyrk.<br>
>Pbzcyrk vf orggre guna pbzcyvpngrq.<br>
>Syng vf orggre guna arfgrq.<br>
>Fcnefr vf orggre guna qrafr.<br>
>Ernqnovyvgl pbhagf.<br>
>Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.<br>
>Nygubhtu cenpgvpnyvgl orngf chevgl.<br>
>Reebef fubhyq arire cnff fvyragyl.<br>
>Hayrff rkcyvpvgyl fvyraprq.<br>
>Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.<br>
>Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.<br>
>Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.<br>
>Abj vf orggre guna arire.<br>
>Nygubhtu arire vf bsgra orggre guna *evtug* abj.<br>
>Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.<br>
>Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.<br>
>Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!<br>

- the `print(this.d)` command outputs a dictionary of decryption keys to decode the result of the first print statement.<br>
>{'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',<br>
>'O': 'B', 'P':'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M',<br>
>'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e':'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a',<br>
>'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's':'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}<br>

This was quite a fun and somewhat challenging endavour
<br>
The bulk of this code run lied in the cleaning and modifying to ensure a result that is as clean as possible.

