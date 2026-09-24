from cryptography.utils import Buffer
from cryptography.fernet import Fernet
import base64

class Crypt:
    def GenerateKey():
        key = Fernet.generate_key()
        return key

    @staticmethod
    def Encrypt(line:str, key: bytes) -> bytes:
        fernet = Fernet(key)
        enc_line = fernet.encrypt(line.encode())
        return enc_line

    @staticmethod
    def Decrypt(line:str, key: bytes) -> str:
        fernet = Fernet(key)
        dec_line = fernet.decrypt(line).decode()
        return dec_line

    @staticmethod
    def Encrypt64(line:str) -> str:
        Buffer
        base64_bytes = base64.b64encode(line.encode("utf-8"))
        base64_line = base64_bytes.decode("utf-8")
        return base64_line

    @staticmethod
    def Decrypt64(line: str) -> bytes:
        base64_bytes = bytes(line, "utf-8")
        line_bytes = base64.b64decode(base64_bytes)
        return line_bytes
