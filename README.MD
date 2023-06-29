# A poor man's tqdm - no progress bar, only numbers, no configuration options

## pip install tqma

#### Tested against Windows 10 / Python 3.10 / Anaconda

- No progress bar, only numbers (printed to stderr)
- No configuration options
- Only 10 lines of code 
- Only one import: sys 
- No dependencies 


```python
from tqma import tqma
from time import sleep
f=0

for r in tqma(range(10)):
    f = f + r
    sleep(2)
print(f)
```