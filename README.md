Paperkey Words
==============

[Paperkey](https://www.jabberwocky.com/software/paperkey/) can be used to create a plain text paper backup of your PGP/GPG private key.  
However, if you don’t trust the available printer, it’s a pain to actually create the physical copy of your key, because you have to write down a lot of hex numbers.

[paperkeywords](https://codeberg.org/vonshednob/paperkeywords) can be used to transform those hex numbers into words (using [PGP word list](https://en.wikipedia.org/wiki/PGP_word_list)) and back again for recovery.

Backup and recover
------------------

To create a backup, run paperkey as usual and pipe the output through paperkeywords like this:

    > gpg --export-secret-keys my-key | paperkey | python paperkeywords.py > paperkeywords.txt

Now you can start the tedious but secure job of writing down the content of `paperkeywords.txt`.

To restore your private key, you need your public key (without ascii armor). Then you can run this:

    > cat paperkeywords | python paperkeywords.py -d | paperkey --pubring pubkey.gpg | gpg --import

That’s it. You recovered your private key.


Shorter Words
-------------

If you don’t like the amount of words you have to write, you can use the `-r` or `--rfc1751` command line option. With this option paperkeyword will use the [RFC1751](https://www.rfc-editor.org/info/rfc1751) word list (or rather the first 512 words thereof) instead of the PGP word list.

When restoring your public key, you must apply the `-r` option again, obviously.


Nice, but where's the code?
---------------------------

It was moved to [codeberg](https://codeberg.org/vonshednob/paperkeywords).

