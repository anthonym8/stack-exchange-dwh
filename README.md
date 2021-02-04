stack-exchange-dwh
==============================

Local data warehouse containing Stack Exchange data for practicing analytics and data science.

By default, the dataset included in the docker image is from [Data Science Stack Exchange](https://datascience.stackexchange.com/). You can also build a docker image using data from other Stack Exchange websites. Just follow the instructions below.


Usage
------------
1. Make sure docker is installed in your computer
1. Run this command to spin up the sample data warehouse:
> `docker run -p 5439:5432 -d rmasi/misc:stack-exchange-dwh`
1. Connect your SQL client or data visualization tool to the database:
    - username: `user`
    - password: `password`
    - hostname: `localhost`
    - port: `5439`
1. Time to practice SQL!


Building the docker image
------------
1. Clone the repository:
> `git clone https://github.com/r-mas/stack-exchange-dwh.git`
1. Set the working directory:
> `cd stack-exchange-dwh`
1. Create a new conda environment:
> `conda create -n python==3.7.5 stack-exchange-dwh`
1. Activate this conda environment:
> `conda activate stack-exchange-dwh`
1. Install the required python packages:
> `pip install -r requirements.txt`
1. Run the ETL scripts:
> `python -m src.etl.<TEMPORARY>`
1. Build the docker image:
> `docker build -t stack-exchange-dwh .`
1. You can now run this local image via:
> `docker run -p 5439:5432 -d stack-exchange-dwh`

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        └── data           <- Scripts to download or generate data

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
