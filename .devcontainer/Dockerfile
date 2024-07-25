FROM continuumio/miniconda3:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    git \
    wget \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Bazelisk
RUN wget https://github.com/bazelbuild/bazelisk/releases/download/v1.11.0/bazelisk-linux-amd64 \
    && mv bazelisk-linux-amd64 /usr/local/bin/bazel \
    && chmod +x /usr/local/bin/bazel

COPY environment.yml /tmp/environment.yml
# Create a new conda environment
RUN conda env create -f /tmp/environment.yml

# Initialize conda in bash config files
RUN conda init bash

# Activate conda environment in .bashrc
RUN echo "conda activate homl3" >> ~/.bashrc

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "homl3", "/bin/bash", "-c"]

# Activate conda environment by default
CMD ["conda", "run", "--no-capture-output", "-n", "homl3", "/bin/bash"]