import logging

from cryptography.fernet import Fernet

from .i_encryptor import IEncryptor

logger = logging.getLogger(__name__)

# KeyBasedEncryptor is an encryption method which use random key of specific length
# and AES block cipher to encrypt/decrypt the data. The key is more complex
# one and hard to remember than user provided one. This class provides more secure way of
# encryption compared to PasswordBasedEncryptor because of the random and complex key.
# We can merge the two into the one encryption method but then we lose the entropy
# of the key with whatever key derivation function we use.
# Note: password != key


class KeyBasedEncryptor(IEncryptor):

    _BLOCK_SIZE = 32

    def __init__(self, key: bytes):
        self._key = key

    def encrypt(self, plaintext: bytes) -> bytes:
        fernet_object = Fernet(self._key)
        return fernet_object.encrypt(plaintext.encode())

    def decrypt(self, ciphertext: bytes) -> bytes:
        fernet_object = Fernet(self._key)
        return fernet_object.decrypt(ciphertext)
