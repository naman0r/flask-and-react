# how i did this and what I learned:

# setup:

- mkdir backenbd

  - touch server.py

- npm create vite@latest
  - react + js, named the project frontend

cd backend

python3 -m venv venv - this created a virtual environment

source venv/bin/activate - this activates the virtual environment

pip3 install Flask (within the venv)

    then we set up a server on port 5000 (flask apps run on default on 5000.)
    ( you can specify a port in the app.run command by adding , port=????)

# frontend integration:
