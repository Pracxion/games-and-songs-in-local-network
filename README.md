# Getting Started 

## Starting with Server

### Installing the dependencies

I recommend to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for a separate virtual environment. After installing you can create a virtual environment with `conda create --name {Name} python=3.9`, so for me it was `conda create --name games-and-songs-in-local-network python=3.9`. After creating the environment you can activate it with `conda activate {Name}`. Now navigate to the `Server` directory and execute `pip install -r requirements.txt`, this will install the necessary dependencies for this project.

### Starting the server

After installing all the dependencies you can run the `server.py`, this will boot up the flask server.

## Starting with Client

### `npm start`

After starting you can access the website on `http://127.0.0.1:3000`.

