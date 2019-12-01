#cripto itens

class Crypto(object):
    from Crypto.Cipher import AES
    import base64  
    from Crypto.Hash import SHA256

    def __init__(self, counter):
      self.counter = counter

    def key_select(self, text):
        hash = SHA256.new()
        hash.update(text)
        new_hash = hash.digest()
        encode_bytes = base64.b64encode(new_hash.encode("utf-8"))
        key = str(encode_bytes, "utf-8")
        return key

    def encrypt(self, key, iten):
        obj_key = AES.new(key, AES.MODE_CBC, counter=lambda: self.counter)
        cipher_iten = obj_key.encrypt(iten)
        return cipher_iten

    def decrypt(self, key, iten):
        obj_key = AES.new(key, AES.MODE_CBC, counter=lambda: self.counter)
        decipher_iten = obj_key.decrypt(iten)
        return decipher_iten