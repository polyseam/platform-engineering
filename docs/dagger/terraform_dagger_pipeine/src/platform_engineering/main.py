from typing import Annotated
import dagger
from dagger import dag, function, object_type, Doc, Secret


@object_type
class PlatformEngineering:
    @function
    async def publish(
        self,
        source: dagger.Directory,
        client_id: Annotated[dagger.Secret, Doc("Azure Client ID")],
        client_secret: Annotated[dagger.Secret, Doc("Azure Client Secret")],
        subscription_id: Annotated[dagger.Secret, Doc("Azure Subscription ID")],
        tenant_id: Annotated[dagger.Secret, Doc("Azure Tenant ID")],
    ) -> str:
        """
        Publish the application container after building and testing it on-the-fly.

        This function first runs the Terraform plan using Azure credentials stored as secrets.
        Then, it returns the output of the Terraform execution.
        """
        terraform_output = await self.run_terraform(
            source, client_id, client_secret, subscription_id, tenant_id
        )
        return f"Terraform Plan Output:\n{terraform_output}"

    @function
    async def run_terraform(
        self,
        directory_arg: dagger.Directory,
        client_id: dagger.Secret,
        client_secret: dagger.Secret,
        subscription_id: dagger.Secret,
        tenant_id: dagger.Secret,
    ) -> str:
        """
        Runs Terraform init and plan with Azure authentication.

        This function mounts the Terraform directory inside a Dagger container,
        injects Azure credentials securely using Dagger secrets, and executes Terraform commands.
        """
        container = (
            dag.container()
            # Use official Terraform image
            .from_("hashicorp/terraform:1.11")
            # Mount the working directory
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            # Inject Azure credentials as secrets
            .with_secret_variable("ARM_CLIENT_ID", client_id)
            .with_secret_variable("ARM_CLIENT_SECRET", client_secret)
            .with_secret_variable("ARM_SUBSCRIPTION_ID", subscription_id)
            .with_secret_variable("ARM_TENANT_ID", tenant_id)
            # Initialize Terraform and create a plan
            .with_exec(["terraform", "init"])
            .with_exec(["terraform", "plan"])
        )
        # Capture and return the Terraform output
        return await container.stdout()