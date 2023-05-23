# Use an official Python runtime as the base image
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir --upgrade pip
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /code/

# Set environment variables if necessary
# ENV VARIABLE_NAME value

# Expose the port your Django app will run on
EXPOSE 8000

# Define the command to run your Django app
CMD python manage.py runserver 0.0.0.0:8000