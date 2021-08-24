# Pulumi project to create a simple resource and test the Azure Devops Pipeline

import pulumi
from pulumi_azure_native import resources


location = 'WestEurope'

# Create an Azure Resource Group
resource_group = resources.ResourceGroup('resource_group',
    resource_group_name='rsg-pulumi-pipeline',
    location=location)