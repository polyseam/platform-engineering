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