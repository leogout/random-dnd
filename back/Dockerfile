FROM ghcr.io/astral-sh/uv:alpine
LABEL authors="leogout"

WORKDIR /app

COPY pyproject.toml .python-version uv.lock ./

RUN uv sync --no-dev --no-cache

COPY . .

EXPOSE 8000

# using --no-sync so that uv does not try to install the dev dependencies,
# see https://github.com/astral-sh/uv/issues/12558
CMD ["uv", "run", "--no-sync", "fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]


