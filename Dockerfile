FROM python:3
LABEL maintainer="pramitsawant"

# Set work directory
RUN mkdir /app
WORKDIR /app

# Install dependencies into a virtualenv
# RUN pip install --upgrade pipenv
# COPY ./Pipfile .
# COPY ./Pipfile.lock .
# RUN pipenv install
# RUN pipenv shell
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project code
COPY . /app/