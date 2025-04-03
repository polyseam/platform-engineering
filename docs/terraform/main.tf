terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.23.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_storage_account" "example" {
  name                     = "davidteststorage1537892"
  resource_group_name      = "david-personal"
  location                 = "West US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

