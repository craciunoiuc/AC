Password: hpaMx
Flag: CRYPTO_CTF{0bladiOBlad4TimeG0esOn}
``**Hint!** Might help if you listen to https://www.youtube.com/watch?v=b8HVQtIoBYU while solving this challenge.  ``
``If it doesn't help you the first time, it might help you the 9192631700th time you listen to it.``

The hint helped me a lot. I looked for 9192631700 on the Internet and found out that was the atomic time, so there had to be a timing attack involved.
I found it quite difficult to construct the perfect metric, so I chose to implement a brute force attack.

N.B.: Please read the comments of the ``script.py``. 
