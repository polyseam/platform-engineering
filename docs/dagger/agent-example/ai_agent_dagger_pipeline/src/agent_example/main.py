import dagger
from dagger import dag, function, object_type, Doc
from typing import Annotated
import os

@object_type
class AgentExample:
    async def comment_on_pr(
        self,
        repo: str,
        comment_body: str,
        github_token: dagger.Secret,
    ) -> str:
        container = (
            dag.container()
            .from_("alpine:latest")
            .with_secret_variable("GITHUB_TOKEN", github_token)
            .with_exec(["apk", "add", "--no-cache", "curl", "bash", "git", "openssl"])
            .with_exec([
                "sh", "-c",
                (
                    "curl -fsSL https://github.com/cli/cli/releases/download/v2.70.0/gh_2.70.0_linux_amd64.tar.gz "
                    "| tar -xz && mv gh_2.70.0_linux_amd64/bin/gh /usr/local/bin/"
                )
            ])
            # Clone the repo
            .with_exec(["git", "clone", f"https://github.com/{repo}.git"])
            # Move into the repo directory and run the commands
            .with_workdir(repo.split("/")[-1])
            .with_exec([
                "sh", "-c",
                (
                    "LATEST_PR=$(gh pr list --author \"@me\" --limit 1 --json number --jq '.[0].number') && "
                    f"gh api repos/{repo}/issues/$LATEST_PR/comments -f body='{comment_body}'"
                )
            ])
        )
        
        return await container.stdout()
    
    @function
    async def terraform_agent(
        self,
        assignment: str,
        directory_arg: dagger.Directory,
        client_id: dagger.Secret,
        client_secret: dagger.Secret,
        subscription_id: dagger.Secret,
        tenant_id: dagger.Secret,
        github_token: dagger.Secret
        ) -> str:
        
        environment = (
             dag.env()
             .with_string_input("assignment", assignment, "the assignment to complete")
             .with_container_input(
                 "terraform_runner",
                 dag.container().from_("hashicorp/terraform:1.11")
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
        
        
        await self.comment_on_pr("codetocloudinc/platform-engineering", await analyze_results.last_reply(), github_token)
        
        return await analyze_results.last_reply()