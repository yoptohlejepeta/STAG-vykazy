# Use official Python image as a base
FROM python:3.11

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install Python dependencies with Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy the rest of your application code
COPY . .

# Expose the port FastAPI uses (default is 8000)
EXPOSE 8000

# Command to run the FastAPI server
# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]