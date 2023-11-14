import os, json 
open("env.json", "w").write(json.dumps(dict(os.environ), indent=4))