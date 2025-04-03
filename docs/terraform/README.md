Example of Terraform CI/CD pipeline with GitHub Actions.

This deploys a azure storage account using the same terraform code in the `docs/dagger` directory.

1. install azure cli 
    - confirm installation with `az version`
2. run `az login`, this will prompt a browser
3. create a service principal
    - `az ad sp create-for-rbac -n MyExampleServicePrincipal --role Contributor --scopes /subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP_NAME`
4. copy the output and add it to the github secrets