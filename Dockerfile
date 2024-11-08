FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Copy the datadex project and dependencies
RUN git clone https://github.com/datonic/datadex.git $HOME/app && \
    cd $HOME/app && \
    chown -R user:user .

# Create a data directory and set ownership
RUN mkdir -p $HOME/app/data && chown -R user:user $HOME/app/data

# Set the working directory
WORKDIR $HOME/app

# Sync the dependencies
RUN [ "uv", "sync" ]

# Run the Dagster server
CMD [ "uv", "run", "dagster-webserver", "--read-only", "-h", "0.0.0.0", "-p", "7860" ]
