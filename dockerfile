# # Use a lightweight base image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the Python script into the container
# COPY script.py /app

# # Run commands to install any dependencies required for the Python script
# # In this case, we're not installing any additional dependencies

# # Command to start the container
# CMD ["python", "script.py"]

FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /home
RUN mkdir -p /home/data /home/output

# Copy the Python script into the container
COPY . /home/data
# Copy result.txt to /home/output
RUN touch /home/output/result.txt

# Give execute permissions to script
RUN chmod +x /home/data/cloud.py
RUN chmod +w /home/output/result.txt

# Create the required directories


# Set the command to run the script
CMD ["python3", "/home/data/cloud.py"]
