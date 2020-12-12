# passexport

Exports encrypted passwords from `pass` or `gopass` (or just gpg) to a single plaintext file. I made this because my public key expired, and I forgot my LUKS password to decrypt my master key. Therefore, I just made a new key pair and encrypt what we exported with it.

Usage: put encrypted files into system arguments, so we can do this:

`find ~/.password-store -iname \*.gpg | xargs python main.py`

Probably could have been done with shell scripting, but whatever.
