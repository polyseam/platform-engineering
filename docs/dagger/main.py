import dagger
import asyncio

async def run_terraform():
    async with dagger.Connection() as client:
        # Define the Terraform container
        tf_container = (
            client.container()
            .from_("hashicorp/terraform:latest")  # Use Terraform image
            .with_mounted_directory("/app", client.host().directory("."))  # Mount current dir
            .with_workdir("/app")
            .with_exec(["init"])  # Run terraform init
            .with_exec(["plan"])  # Run terraform plan
        )

        # Execute the plan
        result = await tf_container.stdout()
        print(result)

# Run the Dagger pipeline
asyncio.run(run_terraform())
