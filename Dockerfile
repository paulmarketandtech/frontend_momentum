# streamlit/Dockerfile

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# Copy dependency files first (better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy application code
COPY . .

# Expose Streamlit default port
EXPOSE 8502

# Run streamlit
CMD ["uv", "run", "streamlit", "run", "main.py", "--server.address", "0.0.0.0", "--server.port", "8502"]
