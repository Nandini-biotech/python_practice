>>> print("atgcatgcatgcatgc")
atgcatgcatgcatgc
>>> long_sequence
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    long_sequence
NameError: name 'long_sequence' is not defined
>>> long_sequence= ("atgcatgcatgcatgc")
>>> if len(long_sequence) > 10
  File "<python-input-3>", line 1
    if len(long_sequence) > 10
                              ^
SyntaxError: expected ':'
>>> print("long_sequence")
long_sequence
>>> print(long_sequence)
atgcatgcatgcatgc
>>> if len(long_sequence) > 10    else print(short_sequence)
  File "<python-input-6>", line 1
    if len(long_sequence) > 10    else print(short_sequence)
                                  ^^^^
SyntaxError: invalid syntax
>>> if len(long_sequence) > 10: priint(long_sequence)     else print(short_sequence)
  File "<python-input-7>", line 1
    if len(long_sequence) > 10: priint(long_sequence)     else print(short_sequence)
                                                          ^^^^
SyntaxError: invalid syntax
>>>  if len(long_sequence) > 10: print(long_sequence)     else print(short_sequence)
  File "<python-input-8>", line 1
    if len(long_sequence) > 10: print(long_sequence)     else print(short_sequence)
IndentationError: unexpected indent
>>>  if len(long_sequence) > 10: print("long_sequence")     else print("short_sequence")
  File "<python-input-9>", line 1
    if len(long_sequence) > 10: print("long_sequence")     else print("short_sequence")
IndentationError: unexpected indent
>>>  if len(long_sequence) > 10:
  File "<python-input-10>", line 1
    if len(long_sequence) > 10:
IndentationError: unexpected indent
>>> if len(long_sequence) > 10:                                                                                        \
         print("long_sequence")                                                                                        \
     else print("short_sequence")
  File "<python-input-11>", line 1
    if len(long_sequence) > 10:                                                                                                 print("long_sequence")                                                                                             else print("short_sequence")
                                                                                                                                                                                                                                                   ^^^^
SyntaxError: invalid syntax
>>>  if len(long_sequence) > 10:                                                                                       \
          print("long_sequence")                                                                                       \
      else: print("short_sequence")
  File "<python-input-12>", line 1
    if len(long_sequence) > 10:                                                                                                 print("long_sequence")                                                                                             else: print("short_sequence")
IndentationError: unexpected indent
>>> if len(long_sequence) > 10:                                                                                        \
    print("long_sequence")                                                                                             \
    else print("short_sequence")
  File "<python-input-13>", line 1
    if len(long_sequence) > 10:                                                                                            print("long_sequence")                                                                                                 else print("short_sequence")
                                                                                                                                                                                                                                                  ^^^^
SyntaxError: invalid syntax
>>>  if len(long_sequence) > 10:                                                                                       \
     print("long_sequence")                                                                                            \
     else: print("short_sequence")
  File "<python-input-14>", line 1
    if len(long_sequence) > 10:                                                                                            print("long_sequence")                                                                                                 else: print("short_sequence")
IndentationError: unexpected indent
>>> print("Long Sequence") if len(long_sequence) > 10 else print("Short Sequence")
Long Sequence
>>> print("start codon found"!) if "atg" in 'long sequence' else print("no start codon found")
  File "<python-input-16>", line 1
    print("start codon found"!) if "atg" in 'long sequence' else print("no start codon found")
                             ^
SyntaxError: invalid syntax
>>> print("start codon found") if "atg" in 'long sequence' else print("no start codon found")
no start codon found
>>>  print("start codon found") if "atg" in long sequence else print("no start codon found")
  File "<python-input-18>", line 1
    print("start codon found") if "atg" in long sequence else print("no start codon found")
IndentationError: unexpected indent
>>>  print("start codon found") if "atg" in long_sequence else print("no start codon found")
  File "<python-input-19>", line 1
    print("start codon found") if "atg" in long_sequence else print("no start codon found")
IndentationError: unexpected indent
>>> print("start codon found") if "atg" in long_sequence else print("no start codon found")
start codon found
>>>  print("start codon found") if "atg" in long_sequence else print("no start codon found")
  File "<python-input-21>", line 1
    print("start codon found") if "atg" in long_sequence else print("no start codon found")
IndentationError: unexpected indent
>>> print("start codon found") if "atg" in long_sequence else print("no start codon found")
start codon found
>>> print(long_sequence.replace("t","u"))
augcaugcaugcaugc
>>> for base in long_sequence print("base:", base)
  File "<python-input-24>", line 1
    for base in long_sequence print("base:", base)
                              ^^^^^
SyntaxError: invalid syntax
>>> for base in long_sequence: print("base:", base)
...
base: a
base: t
base: g
base: c
base: a
base: t
base: g
base: c
base: a
base: t
base: g
base: c
base: a
base: t
base: g
base: c
>>> amino_acid = { "atg": "methionine", "ttt": "phenylalanine" , "gaa" : "glutamicacid"}
>>> print("atg")
atg
>>> print(amino_acid["arg"])
Traceback (most recent call last):
  File "<python-input-28>", line 1, in <module>
    print(amino_acid["arg"])
          ~~~~~~~~~~^^^^^^^
KeyError: 'arg'
>>>  print(amino_acids["atg"])
  File "<python-input-29>", line 1
    print(amino_acids["atg"])
IndentationError: unexpected indent
>>> amino_acids = {"atg": "Methionine", "ttt": "Phenylalanine", "gaa": "Glutamic Acid"}; print(amino_acids["atg"])
Methionine
>>>
KeyboardInterrupt
>>> amino_acids = {"atg": "Methionine", "ttt": "Phenylalanine", "gaa": "Glutamic Acid"}
>>> print(amino_acids["atg"])
Methionine
>>> print(amino_acids["atg"])
Methionine
>>> 0<1
True
>>> len("atgcatgcatgcatgc")>10
True
>>> motif= ("atgc")
>>> motif in long_sequence
True
>>> for letter in "atgXatg":
...     if letter == "X":
...         break
...     print(letter)
...
a
t
g
>>> for letter in "atgXatg":
...     if letter == "X":
...         continue
...     print(letter)
...
a
t
g
a
t
g
>>> dna = "atgcatag"
... pos = 0
...
... # Jab tak position 6 se choti hai, tab tak aage badho
... while pos < 6:
...     print("Base at position", pos, "is", dna[pos])
...     pos = pos + 1
...
Base at position 0 is a
Base at position 1 is t
Base at position 2 is g
Base at position 3 is c
Base at position 4 is a
Base at position 5 is t
>>> pos = 0; dna = "atgcatag"
... while pos < 5: print("Position:", pos, "Base:", dna[pos]); pos = pos + 1
...
Position: 0 Base: a
Position: 1 Base: t
Position: 2 Base: g
Position: 3 Base: c
Position: 4 Base: a
>>> for i in range(4)
  File "<python-input-42>", line 1
    for i in range(4)
                     ^
SyntaxError: expected ':'
>>> for i in range(4):
...     print(i)
...
0
1
2
3
>>> for i in range(1,10,2): print(i)
...
1
3
5
7
9
>>> protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
>>> for i in range(len(protein)):
... if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
... print("protein contains invalid amino acid %s is at position %d" % (protein[i], i))
...
  File "<python-input-46>", line 2
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
    ^^
IndentationError: expected an indented block after 'for' statement on line 1
>>> protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'; for i in range(len(protein)): print("invalid:", protein[i], "at", i) if pr\
otein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ' else None
  File "<python-input-47>", line 1
    protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'; for i in range(len(protein)): print("invalid:", protein[i], "at", i) if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ' else None
                                                        ^^^
SyntaxError: invalid syntax
>>> protein = 'SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
... for i in range(len(protein)):
...     if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
...         print("invalid:", protein[i], "at position", i)
...
invalid: U at position 8
invalid: U at position 9
invalid: J at position 20
