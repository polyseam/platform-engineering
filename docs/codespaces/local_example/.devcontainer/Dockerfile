# Use the official Ubuntu 22.04 LTS base image
FROM ubuntu:22.04

# Set a default locale to avoid locale-related issues
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Update and install essential dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    curl \
    gnupg \
    software-properties-common \
    wget \
    git \
    docker.io && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list && \
    apt-get update && apt-get install -y --no-install-recommends terraform && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Dagger CLI
RUN curl -L https://dl.dagger.io/dagger/install.sh | bash

# Install the Bicep CLI using the Azure CLI
RUN az bicep install

# Verify Terraform installation
RUN terraform --version

# Verify Azure CLI installation
RUN az version

# Verify Bicep CLI installation
RUN az bicep version

# Verify Dagger CLI installation
RUN dagger version