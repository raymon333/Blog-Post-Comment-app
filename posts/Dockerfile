# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the Django project files into the container
COPY . /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (assuming it runs on port 8000)
EXPOSE 8001

# Define the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

