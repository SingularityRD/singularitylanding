FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY . .

# Install Python dependencies
RUN uv sync --locked

# Export frontend
RUN uv run reflex export --frontend-only --no-zip

# Expose port
EXPOSE 3000 8000

# Start the app
CMD ["uv", "run", "reflex", "run", "--env", "prod", "--loglevel", "info"]
