from pathlib import Path
import os
import re

owner = os.environ["GH_OWNER"]
repo = os.environ["GH_REPO"]

if repo.lower() == f"{owner}.github.io".lower():
    url = f"https://{owner}.github.io"
    root = "/"
else:
    url = f"https://{owner}.github.io/{repo}"
    root = f"/{repo}/"

path = Path("_config.yml")
text = path.read_text(encoding="utf-8")
text = re.sub(r"^url:.*$", f"url: {url}", text, count=1, flags=re.M)
if re.search(r"^root:", text, flags=re.M):
    text = re.sub(r"^root:.*$", f"root: {root}", text, count=1, flags=re.M)
else:
    text = re.sub(r"^(url: .*)$", rf"\1\nroot: {root}", text, count=1, flags=re.M)
path.write_text(text, encoding="utf-8")
print(f"Hexo url={url} root={root}")
