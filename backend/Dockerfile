FROM python:3.11-slim

ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /code

# Copy pyproject & lock file first for layer caching
COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-interaction --no-ansi --no-root

# Now copy the app code
COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
