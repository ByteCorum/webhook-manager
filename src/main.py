import gui
from encryption import Crypt
from file import File
import os

if __name__ == "__main__":
    try:
        os.makedirs("data/")
    except:
        pass
    if not os.path.exists("data/key.db"):
        key = Crypt.GenerateKey()
        enc_key = Crypt.Encrypt64(key.decode("utf-8"))
        File.Write(enc_key,"data/key.db")
    gui.GUI()
