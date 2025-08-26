import hashlib

def md5(data_string):
    salt = "XXXXXX"
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()