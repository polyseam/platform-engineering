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

The above Dagger CLI command called `init` initializes the new module, and you will note we are passing through a few command line arguments:

- sdk: dagger makes available a few SDKs. They have support for Go, Python, TypeScript, PHP, and Java. In this case, we are using Python.
- source: source directory used by the installed sdk. In our case, we are asking Dagger to initialize in the ./terraform_dagger_pipeine directory
- name: name of the new module

All this together will create a new directory in our Dagger folder called ‘terraform_dagger_pipeine’ with some default configurations.

To get this working for our use case and deploy some Terraform code, we will need to make some configuration changes.

#### Step 3: Update the Dagger Configuration ⚙️

In the main.py file that was generated by the Dagger CLI (locate at: docs\dagger\terraform_dagger_pipeine\src\platform_engineering\main.py), we need to make some configuration changes to deploy our Terraform code. Before we do that, there are a few key concepts we need to understand. As mentioned earlier, we are going to deploy some Terraform code against an Azure resource group. There are a few things we need to consider to do this successfully.

**Things to consider** 🤔

- How will we securely store our secrets to authenticate to Azure?
- How will we provide Dagger the ability to run Terraform?

We can solve the first challenge by using **[Dagger Secrets](https://docs.dagger.io/features/secrets)**. Let's briefly explore how Dagger manages sensitive credentials securely.

**Using Secrets in Dagger** 🔒

Dagger supports the use of confidential information, such as passwords, API keys, SSH keys, access tokens, and other sensitive data in your pipelines. Instead of exposing secrets in environment variables or configuration files, Dagger provides built-in secret management, allowing us to:

- Store secrets securely in the host environment.
- Read secrets from files on the host system.
- Fetch secrets dynamically from external providers like 1Password and Vault.

For our use case, we will store Azure authentication credentials (client_id, client_secret, subscription_id, tenant_id) as Dagger Secrets and inject them securely into our Terraform container. In the repo you will notice a .env.sample file (located at: docs\dagger\terraform_dagger_pipeine\src\platform_engineering\.env.sample) that can be filled out with your service principal client_id and client_secret, along with your tenant_id and subscription_id. Simply make a copy of that file and call it .env.

**Running Terraform with Dagger’s Containerized Approach** 🏗️

As for the challenge around 'How will we provide Dagger the ability to run Terraform?':

Since Dagger executes workflows in containers, we don’t need to install Terraform on our local machine or the CI/CD runner. Instead, we use the official hashicorp/terraform container image to ensure a consistent runtime environment. This approach provides several benefits:

✅ Eliminates Local Setup Hassles – No need to install or manage Terraform versions manually.
✅ Ensures Environment Consistency – The same Terraform version runs in development and CI/CD.
✅ Enhances Security – The container isolates Terraform execution, reducing the risk of dependency conflicts.

By leveraging Dagger’s containerized execution, we can run Terraform commands (init, plan, apply) inside a predefined, reproducible environment. This makes our pipeline more portable, repeatable, and platform-agnostic. 🚀

**Dagger Python Implementation** ⚒️

Here’s how we modify main.py to leverage Dagger Secrets and a Terraform Docker image to execute our Terraform:

```python
from typing import Annotated
import dagger
from dagger import dag, function, object_type, Doc, Secret


@object_type
class PlatformEngineering:
    @function
    async def plan(
        self,
        source: dagger.Directory,
        client_id: Annotated[dagger.Secret, Doc("Azure Client ID")],
        client_secret: Annotated[dagger.Secret, Doc("Azure Client Secret")],
        subscription_id: Annotated[dagger.Secret, Doc("Azure Subscription ID")],
        tenant_id: Annotated[dagger.Secret, Doc("Azure Tenant ID")],
    ) -> str:
        """
        Runs `terraform plan` using Azure credentials stored as secrets.

        This function executes Terraform inside a container, securely passing in Azure authentication credentials.
        It returns the Terraform plan output for review.
        """
        return await self.run_terraform("plan", source, client_id, client_secret, subscription_id, tenant_id)

    @function
    async def apply(
        self,
        source: dagger.Directory,
        client_id: Annotated[dagger.Secret, Doc("Azure Client ID")],
        client_secret: Annotated[dagger.Secret, Doc("Azure Client Secret")],
        subscription_id: Annotated[dagger.Secret, Doc("Azure Subscription ID")],
        tenant_id: Annotated[dagger.Secret, Doc("Azure Tenant ID")],
    ) -> str:
        """
        Runs `terraform apply` to apply the planned changes using Azure authentication.

        This function first ensures Terraform is initialized, then executes the apply step.
        The execution is done inside a container, securely injecting the necessary secrets.
        """
        return await self.run_terraform("apply", source, client_id, client_secret, subscription_id, tenant_id)

    async def run_terraform(
        self,
        command: str,
        directory_arg: dagger.Directory,
        client_id: dagger.Secret,
        client_secret: dagger.Secret,
        subscription_id: dagger.Secret,
        tenant_id: dagger.Secret,
    ) -> str:
        """
        Runs Terraform (`plan` or `apply`) with Azure authentication.

        - Mounts the Terraform directory inside a Dagger container.
        - Injects Azure credentials securely as environment variables.
        - Executes Terraform commands (`terraform init`, then `terraform plan` or `terraform apply`).
        """
        terraform_command = ["terraform", command]
        
        # Add auto-approve if it's an apply command
        if command == "apply":
            terraform_command.append("-auto-approve")

        container = (
            dag.container()
            .from_("hashicorp/terraform:1.11")  # Use official Terraform image
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            .with_secret_variable("ARM_CLIENT_ID", client_id)
            .with_secret_variable("ARM_CLIENT_SECRET", client_secret)
            .with_secret_variable("ARM_SUBSCRIPTION_ID", subscription_id)
            .with_secret_variable("ARM_TENANT_ID", tenant_id)
            .with_exec(["terraform", "init"])
            .with_exec(terraform_command)
        )
        return await container.stdout()
```

**How This Works** 🔍

1. Injecting Secrets
    - We replace plain environment variables with dagger.Secret, ensuring that Azure credentials are never exposed in logs or outputs.
    - Secrets are passed as arguments to both the publish and run_terraform functions.

2. Mounting the Terraform Directory
    - The Terraform directory is mounted inside the container at /mnt, ensuring Terraform can access required configuration files.

3. Executing Terraform Securely
    - The container runs terraform init and terraform plan/apply depending on what function we call. It also authenticates securely with the injected Azure credentials.

Now that we have all this setup, we can run this pipeline locally to make sure it works before pushing to GitHub. Lets see how we can do that by running a Terraform plan and apply.

#### Step 4: Running the Dagger Pipeline Locally 🧑‍💻

To execute our Dagger pipeline locally, we can leverage the Dagger CLI again this time using the `call` command. This will call one or more functions, interconnected into a pipeline. In thise case, we are calling our `plan` function defined above in our main.py file. This will run a Terraform plan for us that will echo the changes to be made in our Azure resource group. In this case, a new blob storage account.

```bash
dagger call plan --source=. --client-id="ARM_CLIENT_ID" --client-secret="ARM_CLIENT_SECRET" --subscription-id="ARM_SUBSCRIPTION_ID" --tenant-id="ARM_TENANT_ID"
```

You will note we are passing through a few command line arguments being used here:

- source: source directory used by the installed sdk. In our case, we are asking Dagger to initialize in the ./terraform_dagger_pipeine directory
- env vars: all of the required environment variables to enable Terraform to connect to Azure

The output of that command will be similar to the below:

![Terraform Plan Output](docs/dagger/assets/dagger_call_plan_local.png)

The output of the plan is looking good, but instead of running the apply locally, lets get our existing functionality into GitHub actions and run our pipeline there!

#### Step 5: Running our Dagger Pipeline in GitHub Actions 🐙

---

## 🎉 Conclusion

Dagger provides an innovative way to write, manage, and execute CI/CD pipelines as code. By leveraging its graph-based execution model, containerized steps, and multi-platform support, platform engineers can:

🚀 Build reusable and scalable pipelines
🌎 Run workflows anywhere (local/cloud/CI systems)
🔄 Ensure consistency across deployments
🛠️ Easily integrate Terraform, OpenTofu, or Pulumi

With Dagger, your CI/CD logic stays the same, whether you’re deploying locally or on a cloud platform. Happy building! 🏗️🚀
