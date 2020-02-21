## Install python 3
```
1. Install homebrew
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. export PATH="/usr/local/opt/python/libexec/bin:$PATH"

3. brew install python

```

## Intsall Python gRPC Tools

### Install/Update pip
    python -m pip install --upgrade pip

### Install virtual environment
    python -m pip install virtualenv

### Move to a desired working directory and create a virtual environemnt
    virtualenv venv

### Activate the virtual env
    source venv/bin/activate

### Install gRPC

    python -m pip install grpcio // This will install the gRPC within the virtal env only

    sudo python -m pip install grpcio // Use this command if you wish to install gRPC system wide

### Install gRPC tools
    python -m pip install grpcio-tools
