# Define the base image to use for the build
FROM python:3.11.2-slim-buster as compiler
ENV PYTHONUNBUFFERED 1

# Set the working directory for the application
WORKDIR /todo_list

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN python -m venv /opt/venv

# Add the virtual environment to the system path
ENV PATH="/opt/venv/bin:$PATH"

# Install the dependencies in requirements.txt and gunicorn server
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn

# Define a new image for running the application
FROM python:3.11.2-slim-buster as runner

# Set the working directory for the application
WORKDIR /todo_list

# Copy the virtual environment from the compiler stage to the runner stage
COPY --from=compiler /opt/venv /opt/venv

# Add the virtual environment to the system path
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application code to the image
COPY . /todo_list/

# Initialize the database
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Set the start_app.sh script to be executable
RUN chmod +x start_app.sh
