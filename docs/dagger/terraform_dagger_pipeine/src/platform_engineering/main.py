import dagger
from dagger import dag, function, object_type


@object_type
class PlatformEngineering:
    @function
    async def publish(self, source: dagger.Directory) -> str:
        """Publish the application container after building and testing it on-the-fly"""
        terraform_output = await self.run_terraform(source)
        return f"Terraform Plan Output:\n{terraform_output}"

    @function
    async def run_terraform(self, directory_arg: dagger.Directory) -> str:
        """Runs Terraform init and plan with Azure authentication via environment variables"""
        container = (
            dag.container()
            .from_("hashicorp/terraform:1.11")
            .with_mounted_directory("/mnt", directory_arg)
            .with_workdir("/mnt")
            .with_env_variable("ARM_CLIENT_ID", "")
            .with_env_variable("ARM_CLIENT_SECRET", "")
            .with_env_variable("ARM_SUBSCRIPTION_ID", "")
            .with_env_variable("ARM_TENANT_ID", "")
            .with_exec(["terraform", "init"])
            .with_exec(["terraform", "plan"])
        )
        return await container.stdout()


