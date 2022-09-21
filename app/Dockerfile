# Pick a low configuration python base image
FROM python:3.9.14-alpine3.16

#  Expose the port 5000 of the docker container
EXPOSE 5000

# Create a folder app in container and work inside it
WORKDIR /app

# COPY requirements.txt .

# Install all the requirements
RUN pip3 install flask

# Copy all the flask project files into the WORKDIR
COPY . .

# Execute flask application inside the container
CMD python3 app.py