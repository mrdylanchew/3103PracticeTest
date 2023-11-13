# Use an official Python runtime as a parent image
FROM python:3.10


# Install Git
RUN apt-get update && apt-get install -y git

# Set up Git account identity
RUN git config --global user.name "dylan chew"
RUN git config --global user.email "2101110@sit.singaporetech.edu.sg"

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
