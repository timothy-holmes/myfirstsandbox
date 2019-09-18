import os, hashlib

def get_js_version_hash():
    hash_md5 = hashlib.md5()
    js_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)),'static','js')
    for file in os.listdir(js_folder):
        if file.endswith(".js"):
            with open(os.path.join(js_folder,file), "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
    return hash_md5.hexdigest()[:8]
