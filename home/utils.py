def generateSalt(mail):
    salt = "@"
    salt += mail[::2]+"#"
    salt += mail[-3:]+"&"
    return salt
