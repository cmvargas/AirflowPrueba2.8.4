FROM apache/airflow:2.8.4
ENV PYTHON_VERSION=3.11.0
USER root


RUN apt-get update && apt-get -y install libpq-dev gcc
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install build-essential \
        zlib1g-dev \
        libncurses5-dev \
        libgdbm-dev \
        libnss3-dev \
        libssl-dev \
        libreadline-dev \
        libffi-dev \
        libsqlite3-dev \
        libbz2-dev \
        wget \
    && export DEBIAN_FRONTEND=nointeractive \
    && apt-get purge -y imagemagick imagemagick-6-common
RUN cd /usr/src \
    && wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz \
    && tar -xzf Python-3.11.0.tgz \
    && cd Python-3.11.0 \
    && ./configure --enable-optimizations \
    && make altinstall
RUN update-alternatives --install /usr/bin/python python /usr/local/bin/python3.11 1
RUN ln -fs /usr/share/zoneinfo/America/Bogota /etc/localtime && \
    dpkg-reconfigure -f nointeractive tzdata
USER airflow
RUN pip install psycopg2-binary
COPY ./requirements.txt ./requirements.txt
COPY  ./.env ./.env
#RUN pip install -r ./requirements.txt


## codigo odbc
USER root
RUN apt-get update \
    && apt-get install -y gnupg2 \
    && apt-get install -y curl apt-transport-https \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev
## codigo odbc


ENV PIP_USER=false
RUN cd /usr/local/lib \ 
    && python3.11 -m venv /opt/airflow/porttracker_venv \ 
    && source /opt/airflow/porttracker_venv/bin/activate \ 
    && cd /opt/airflow \ 
    &&  /opt/airflow/porttracker_venv/bin/pip install --upgrade pip \ 
    && /opt/airflow/porttracker_venv/bin/pip install -r ./requirements.txt