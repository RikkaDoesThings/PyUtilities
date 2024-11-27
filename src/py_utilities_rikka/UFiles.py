import hashlib
import os

def kb_to_mb(num):
    return (num/1024)

def mb_to_gb(num):
    return (num/1000)

def mb_to_kb(num):
    return (num*1024)

def gb_to_kb(num):
    return (num*1048576)

def bytes_to_kb(num):
    return (num/1024)

def gb_to_bytes(num):
    return (num*1073741824)

def mb_to_bytes(num):
    return (num/1048576)

def kb_to_bytes(num):
    return (num*1024)

def bytes_to_gb(num):
    return (num/1073741824)

def kb_to_gb(num):
    return (num/1048576)

def gb_to_mb(num):
    return (num*1000)

def bytes_to_mb(num):
    return (num/1048576)

def file_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        return (sha256_hash.hexdigest())

def file_size(file_path):
    try:
        return (os.path.getsize(file_path))
    except Exception as err:
        print("Error: "+err)