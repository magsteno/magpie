# magpie
stenographic theory for Shavian input

Magpie theory is an orthographic input system primarily for the Shavian alphabet.
It is currently in early days but I hope to bring something more soon.

## Status
Magpie is currently in an intermediary state, with a lot of changes being made and potential bugs to be fixed. Working on a system, but currently system related content is mainly found in testlib\\\_\_init\_\_.py

To-do:
- finish porting necessarybriefs.json into mainbriefs.json
- implement the changes as a system rather than individual files

## How to use
testlib\\testshav.py, testlib\\testlatin.py and mainbriefs.json are dictionary files for [Plover](https://github.com/openstenoproject/plover). the two testlib dictionaries require the plover-python-dictionary plugin (which can be added within Plover using the in-built plugins manager under Tools).

Also install the plover-dict-commands plugin if you want to be able to use the stroke EUFGT to automatically switch between the two. It's currently expected that these dictionaries remain in the folder .\\testlib\\ with \_\_init\_\_.py, located in plover's main directory. I have only tried these so far on Windows, in a portable plover configuration.

testlib\\testlatin.py expects the existence of the folder .\\shavian\\ within plover's main directory, containing a config file (tsv.cfg) listing paths to latin–shavian dictionaries (with frequency data) in tsv format (latin\\tshavian\\tfrequency). testlib\\testshav.py will use the same files for 'standardisation' (spellings useful for steno differentiation like 𐑣𐑢𐑪𐑑 will automatically be converted into the standard spelling 𐑢𐑪𐑑 to allow for the same muscle memory to be used when outputting shavian and latin)
