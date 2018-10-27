Paperkey Words
==============

[https://www.jabberwocky.com/software/paperkey/](Paperkey) can be used to create a plain text paper backup of your PGP/GPG private key.  
However, if you don’t trust the available printer, it’s a pain to actually create the physical copy of your key, because you have to write down a lot of hex numbers.

`paperkeywords` can be used to transform those hex numbers into words (using [https://en.wikipedia.org/wiki/PGP_word_list](PGP word list)) and back again for recovery.

Backup and recover
------------------

To create a backup, run paperkey as usual and pipe the output through paperkeywords like this:

    > gpg --export-secret-keys my-key | paperkey | python paperkeywords.py > paperkeywords.txt

Now you can start the tedious but secure job of writing down the content of `paperkeywords.txt`.

To restore your private key, you need your public key (without ascii armor). Then you can run this:

    > cat paperkeywords | python paperkeywords.py -d | paperkey --pubring pubkey.gpg | gpg --import

That’s it. You recovered your private key.
