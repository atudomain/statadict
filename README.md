# statadict

Small package that allows reading Stata dictionary files (usually .dct extension).

Extracted information can be used with Pandas when calling read_fwf() function.

# Setup

To install package locally:
```
python3 -m pip install statadict --user
```
Or directly from repository:
```
make all
python3 -m pip install . --user 
```

# Usage

Having Stata dictionary file and related fixed width field csv file without headers, you can now use Pandas to read data:
```
import pandas as pd
from statadict import parse_stata_dict

stata_dict = parse_stata_dict(file="dictionary-file.dct")
data = pd.read_fwf("related-fwf-file.dat", names=stata_dict.names, colspecs=stata_dict.colspecs)
```
