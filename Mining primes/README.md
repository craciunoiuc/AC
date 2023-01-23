Flag:  CRYPTO-CTF{319f8d6053e0c8344e775fd9b97f5ca7}

In order to solve this challenge, I used the hints provided. So I looked for similar patterns found in both keys. 
After some additional research, I tried to find out if one of the prime numbers *p* or *q* was used in order to recreate other moduluses. 
`gcd(n1,n2) > 1`
After that, I rebuilt the 2 ids and decrpyt the 2 messages in order to build the flag.

N.B. : Please read the comments from the ``script.py`` 
![[Pasted image 20230115222550.png]]
