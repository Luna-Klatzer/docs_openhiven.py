# Troubleshooting

---

!!! Warning

    **This documentation page is not finished yet! Information can be outdated or entirely not available!**

!!! Bug "Important"

    Before even starting troubleshooting and testing, it is strongly recommended to activate logging as already shown in
    [Getting Started](../getting_started/logging.html)!

## Issues Downloading the Module

If you encounter issues with downloading OpenHiven.py there can be multiple reasons for that.
Here is a small list of known issues and possible solutions to solve them:

- ??? note "PEP 517 Error" 
  
        The PEP 517 Error or also Wheel Build Error usually occurs when the python environment does not contain a working
        C++ Compiler which is used to build the dependecies using modern PEP 517 and PEP 427 wheels. 

        Possible Solutions:
  
        * If you are using linux or the gcc-compiler try installing the newest version of the gcc compiler which should 
          automatically be used for the building of the wheels.
        * If you are using Windows if the Microsoft C++ Build Tools are working correctly


## Unexpected behavior

If you encounter unexpected behavior and functionality that is not working like wanted this can either be of a bug of
OpenHiven.py, Connection or Hiven Server error or an issue relating the configuration. If you receive results different 
from those in the documentation we first recommend you looking into the logs and activate `DEBUG` mode to see what could 
have caused the issue. 

If you are using a function, or a method that executes a request there might be an issue with the HTTP request that 
caused an unexpected result. If this is not the case try to look into the input, debug the program and inspect data
for possible issues. If there are no issues found with the data and everything seems fine, please open an issue on
the [GitHub page](https://github.com/FrostbyteSpace/openhiven.py/issues) for further investigation. We will try to help 
you and also possibly find the error that caused that issue.
