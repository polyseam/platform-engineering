# 🚀 Using Dagger for Reusable, Portable CI/CD Pipelines

Welcome to the documentation on [Dagger](https://docs.dagger.io/), an **open-source runtime for composable workflows**. But what does that mean exactly? Dagger is very intriguing if you think about the current developer workflow for CI/CD pipelines. Using something like GitHub Actions, we need to define a YAML template (and we all know how much developers love YAML 😉) and push it as many times as it takes to get a initial CI/CD pipeline working.

There are many factors that play into why this is challenging. To name one, the workflow agent (ie: the compute running the pipeline) where the CI/CD pipeline will run is very likely not the same as the environment you develop in, leading to ‘dependency hell’. Debugging is painful since you often have to test by pushing your code, waiting for it to run, and then troubleshooting errors from logs. This slow feedback loop makes iteration cumbersome. Additionally, declarative pipeline definitions, while powerful, can be limiting when handling complex logic, and there’s often no straightforward way to test them locally before deployment.

This is where Dagger comes in to save the day 🦸. In Dagger, CI/CD pipelines are containerized, making them incredibly portable. They run the same way locally as they do in the cloud, eliminating environmental inconsistencies. By enabling developers to run pipelines locally before committing changes, Dagger provides immediate feedback, significantly reducing the time spent debugging and improving development efficiency.

From the creators of Docker, let’s have a look at how Dagger works in practice.

## 🏗️ Introduction to Dagger’s Approach to CI/CD as Code

As mentioned above, Dagger is an **open-source runtime for composable workflows**, designed to create **repeatable, modular, observable, and cross-platform CI/CD pipelines**. By defining CI/CD workflows as code, Dagger enables:

✅ **Reusable Workflows** – Define once, use anywhere across projects and teams.
✅ **Portable Execution** – Run workflows **locally, in any CI system, or in the cloud** without modifications.
✅ **Optimized Performance** – Leverage **automatic artifact caching** for efficient execution.
✅ **Built-in Observability** – Gain real-time insights via **logs, tracing, and metrics**.

Since Dagger leverages containers, what runs locally is will be the same as what runs in the cloud (ie: GitHub Actions). This solves a huge challenge for developers making the writing, testing, and deployment of CI/CD pipelines much easier. Dagger is also platform agnostic allowing you to switch platforms as needed, avoiding CI lock-in

---

## 📌 Dagger Components Overview

The **Dagger Engine** is the core runtime, responsible for executing workflows using a **universal type system** and **data layer**. It runs on any OCI-compatible system and is controlled via the Dagger API. Dagger has the following key components:

- **Dagger Engine**: The core runtime that powers Dagger pipelines.
- **Dagger SDKs**: Use Python, Go, or Node.js to define pipelines.
- **Containerized Execution**: Each step runs in an isolated, reproducible environment.
- **Dagger API**: A GraphQL-based universal type system for defining workflows.
- **DaggerVerse**: An easy way to search and consume modules

---

## 🌍 Real-World Example: Deploying Terraform with Dagger

In the below example, we will create a Dagger pipeline that will deploy some Terraform code and we will see how useful being able to run CI/CD pipelines locally makes the development process.

### 🎯 Expected Outcome

✅ Terraform initializes and validates the configuration.
✅ Infrastructure is provisioned automatically.
✅ The same pipeline can be executed locally or in CI/CD environments without modification.

### 🔨 Implementation

The below steps were taken to implement a CI/CD pipeline in Dagger that deploys Terraform. All the code for the below can be found [here](https://github.com/codetocloudinc/platform-engineering/tree/main/docs/dagger)

Make sure you have installed the [Dagger CLI](https://docs.dagger.io/ci/quickstart/cli/), the repo is cloned and you are in the dagger directory:

```bash
# Clone the repository from GitHub
git clone https://github.com/codetocloudinc/platform-engineering.git

# Change directory to the Terraform Dagger pipeline documentation folder
cd ./docs/dagger/
```

#### Step 1: Create Terraform Files

First, we need to create the base Terraform configuration file that will deploy an Azure Blob Storage Account to an existing resource group. This will be our main.tf file in the root of the dagger folder.

```terraform
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.23.0"
    }
  }
}

provider "azurerm" {
  resource_provider_registrations = "none"
  features {}
}

resource "azurerm_storage_account" "example" {
  name                     = "daggertestingsa"
  resource_group_name      = "dagger"
  location                 = "West US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

Lets Daggerize this Terraform file!

#### Step 2: Initialize Dagger 🧑‍💻🗡️

Inside of the same Dagger directory, we are going to run a few Dagger CLI commands to get going:

```bash
# Initialize a new module at the given path
dagger init --sdk=python --source=./terraform_dagger_pipeine --name=platform_engineering
```

The above Dagger CLI command initializes the new module, and you will note we are passing through a few command line arguments:

- sdk: Dagger makes available a few SDKs. They have support for Go, Python, TypeScript, PHP, and Java. In this case, we are using Python.
- source: Source directory used by the installed sdk. In our case, we are asking Dagger to initialize in the ./terraform_dagger_pipeine directory
- name: Name of the new module

All this together will create a new directory in our Dagger folder called ‘terraform_dagger_pipeine’ with some default configurations.

To get this working for our use case and deploy some Terraform code, we will need to make some configuration changes.

#### Step 3: Update the Dagger Configuration ⚙️

In the main.py file that was generated by the Dagger CLI (ie:docs\dagger\terraform_dagger_pipeine\src\platform_engineering\main.py), we need to make some configuration changes to deploy our Terraform code.


```bash
dagger call publish --source=.
```


## 🎉 Conclusion

Dagger provides an innovative way to write, manage, and execute CI/CD pipelines as code. By leveraging its graph-based execution model, containerized steps, and multi-platform support, platform engineers can:

🚀 Build reusable and scalable pipelines
🌎 Run workflows anywhere (local/cloud/CI systems)
🔄 Ensure consistency across deployments
🛠️ Easily integrate Terraform, OpenTofu, or Pulumi

With Dagger, your CI/CD logic stays the same, whether you’re deploying locally or on a cloud platform. Happy building! 🏗️🚀
