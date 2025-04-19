import dagger
from dagger import dag, function, object_type, Doc
from typing import Annotated

@object_type
class AgentExample:
    @function
    async def terraform_agent(
        self,
        assignment: str,
        directory_arg: dagger.Directory,
        client_id: dagger.Secret,
        client_secret: dagger.Secret,
        subscription_id: dagger.Secret,
        tenant_id: dagger.Secret,
        ) -> str:
        
        environment = (
            dag.env()
            .with_string_input("assignment", assignment, "the assignment to complete")
            .with_container_input(
                "terraform_runner",
                dag.container().from_("hashicorp/terraform:1.11").with_workdir("/mnt")
                .with_mounted_directory("/mnt", directory_arg)
                .with_workdir("/mnt")
                .with_secret_variable("ARM_CLIENT_ID", client_id)
                .with_secret_variable("ARM_CLIENT_SECRET", client_secret)
                .with_secret_variable("ARM_SUBSCRIPTION_ID", subscription_id)
                .with_secret_variable("ARM_TENANT_ID", tenant_id)
                .with_exec(["terraform", "init"])
                .with_exec(["terraform", "plan"]),
                "a container to use for running the terraform init & plan"
                
            )
            .with_container_output(
                "completed", "the completed assignment in the Terraform container"
            )
        )
    
        analyze_results = (
            dag.llm()
            .with_env(environment)
            .with_prompt_file(dag.current_module().source().file("terraformer.txt"))
        )
        
        return await analyze_results.last_reply()
