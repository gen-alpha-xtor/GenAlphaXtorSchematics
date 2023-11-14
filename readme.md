
# Generation Alpha Transistor Schematic Editor

Edit real, working IC schematics live in VsCode. 

## Preview Release

GenAlphaXtor is available on a private preview basis. Contact [dan@fritch.mn](mailto:dan@fritch.mn) if you are interested in joining the trial! 

## Opening a Schematic or Symbol

With a database configured, just open the `sch.oa` or `symbol.oa` file in VsCode's file explorer. 
Or run `code {path}/{to}/sch.oa` from the command line.

## Setting up a Database

Configuring a database requires two primary pieces of information: 

- The library definitions. Each OpenAccess library has an associated directory on disk. Mappings from library-names to directories are dictated in a text format file defined by OpenAccess. By convention they have the filename `lib.defs`, although some popular programs will call them `cds.lib`. 
- Any environment variables required by the library definitions file. (They usually do depend on environment variables.)

GenAlphaXtor will accept environment variable definitions in either of two formats: 

- The popular [dotenv](https://www.dotenv.org/docs/security/env) format, supported by libraries such as [python-dotenv](https://pypi.org/project/python-dotenv/) and the original (JS) [dotenv](https://github.com/motdotla/dotenv) itself. 
- JSON, in the format `{ "VAR_NAME": "VAR_VALUE" }`.

GenAlphaXtor will attempt to auto-configure a database from your VsCode workspace directory. It will search for both library-definitions and environment variables starting in the workspace root, and then in each parent directory until it reaches the filesystem root. 

- Library definition files named either `lib.defs` or `cds.lib` will be auto-loaded. 
  - If your library definitions are in any other path, run the `GenAlphaXtor: Set Library Definitions` VsCode command and select their file.  
- Environment variable files named either `.env` (in dotenv format) or `.env.json` (in JSON format) will be auto-loaded.
  - If your environment file is at any other path, run the `GenAlphaXtor: Set Environment File` VsCode command to select it.

After configuring a schematic database, `GenAlphaXtor` will write a resolution-file name `db.resolved.json` in the workspace root. This file contains the absolute paths to the library definitions and environment variables files that were loaded. It will also often be the best source of debug information if you're having trouble getting a database to load. The resolution-file attempts to catalog any information (typically variable-values) that it needed, but couldn't find. 

Example successful resolution-file:

```json
{
  "schemaVersion": 1,
  "env": {
    "vars": {
      "DESIGNDATA": "/designdata/"
    },
    "file": {
      "path": "/designdata/env.json",
      "fmt": "json"
    }
  },
  "libdefs": {
    "path": "/designdata/cds.lib",
    "warnings": [],
    "libs": {
      "mylib": "/designdata/mylib"
    },
    "unresolved": {
      "libs": [],
      "includes": [],
      "vars": []
    }
  }
}
```

Note running the popular Unix `env` utility *can*, but often doesn't, produce output compatible with the `dotenv` file format. Particularly `env` often includes special characters (and whitespace) which is not escaped or quoted. If running `env` to produce a `dotenv` file, expect to have to do some manual editing. JSON encoding, particularly when written by popular libraries, should avoid this problem. For example the (two-line) Python script [env.py]() will produce a JSON file compatible with GenAlphaXtor: 

```python
import os, json
open("env.json", "w").write(json.dumps(dict(os.environ), indent=4))
```

## Issues and Feature Requests

Please report any issues or feature requests to [gen-alpha-xtor/GenAlphaXtorSchematics](https://github.com/gen-alpha-xtor/GenAlphaXtorSchematics). Note this is not the source code repository.
