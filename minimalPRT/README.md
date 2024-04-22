# minimal pyprt as gptool demo

## running in arggis pro
1. create conda environment in arcgis pro
    - install pyprt
2. run the `minimalPRT.pyt` toolbox
3. observe that the output in tool messages is an list of length 0

## running in command line
1. use the same conda environment created above
2. run the `python minimalPRT.pyt` file 
3. observe that the printed output is an list of length 1



## minimalPRT,pyt
runs the rpk directly from itself
- running from command line gives an array of 1 geometry as response from pyprt
- running from arcgis gives empty array as response from pyprt

## minimalPRT2.pyt
runs the rpk directly from itself and attempts to run on command line using subprocess
- running from command line gives an array of 1 geometry as response from pyprt for both the subprocess and itself
- running from arcgis gives error for subprocess, and empty array for its own response

```
b'Traceback (most recent call last):\r\n  File "C:\\Users\\SEED110\\Documents\\geoService\\minimalPRT\\minimalPRT.pyt", line 16, in <module>\r\n    import pyprt\r\n  File "C:\\Users\\SEED110\\AppData\\Local\\ESRI\\conda\\envs\\arcgispro-py3-clone\\Lib\\site-packages\\pyprt\\__init__.py", line 16, in <module>\r\n    from .pyprt import *\r\n  File "C:\\Users\\SEED110\\AppData\\Local\\ESRI\\conda\\envs\\arcgispro-py3-clone\\Lib\\site-packages\\pyprt\\pyprt\\__init__.py", line 16, in <module>\r\n    from .bin.pyprt import *\r\nModuleNotFoundError: No module named \'pyprt.pyprt.bin.pyprt\'\r\n'
```


