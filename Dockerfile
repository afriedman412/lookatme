# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the app's dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app's files to the container
COPY . .

# Expose the port your app runs on
EXPOSE 8080

# Command to run the app
CMD ["python", "run.py"]