from uuid import uuid4
from hashlib import sha256

def GenerateHash(text:str):
    salt = uuid4().hex
    ToEncode = salt.encode() + text.encode()
    return sha256(ToEncode).hexdigest() + ":" + salt

def VerifyHash(ActualText:str, TestText:str):
    _HashedActualText, _salt = ActualText.split(":")
    ToEncode = _salt.encode() + TestText.encode()
    _HashedTestText = sha256(ToEncode).hexdigest()
    return _HashedActualText == _HashedTestText
