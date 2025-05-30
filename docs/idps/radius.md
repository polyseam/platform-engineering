# 🌐 Radius: Application-Centric Platform Engineering

## 📝 Overview

[Radius](https://radapp.io/) is an open-source, application-centric Internal Developer Platform (IDP) designed to simplify cloud-native development and deployment. It provides a unified experience for building, deploying, and managing applications across environments, focusing on the application as the primary unit rather than just infrastructure.

---

## ✨ Key Features

- 🏗️ **Application-centric abstractions:** Developers define and manage applications, not just infrastructure.
- 🔄 **Unified experience:** Consistent workflows across Azure, AWS, GCP, and on-premises clusters.
- 🛡️ **Built-in policies, security, and compliance:** Guardrails are integrated by default.
- 🧩 **Extensible:** Supports custom resources and integrations for advanced use cases.
- 📦 **Recipe-based provisioning:** Utilizes recipes built on Terraform and Bicep to standardize and automate infrastructure provisioning.

---

## 💡 Why Radius?

Radius enables platform teams to build IDPs that are truly application-centric. By focusing on the application, Radius reduces developer friction, accelerates onboarding, and ensures security and compliance are built-in from the start.

> “Radius enables platform teams to build IDPs that are truly application-centric, not just infrastructure-centric. By focusing on the application as the primary unit, Radius allows developers to define, deploy, and manage their apps with minimal friction, regardless of the underlying cloud or cluster. This approach reduces cognitive load, accelerates onboarding, and ensures that security and compliance are built-in from the start.”  
> — [Radius Blog, May 2025](https://blog.radapp.io/posts/2025/05/13/platform-engineering-with-radius-to-build-application-centric-idps/)

---

## 🛠️ How Radius Uses Recipes

Radius leverages **recipes**—predefined, reusable infrastructure templates—to automate and standardize resource provisioning. These recipes are built using popular Infrastructure as Code (IaC) tools like **Terraform** and **Bicep**:
- **Terraform recipes** allow Radius to provision resources across multiple clouds using HashiCorp’s widely adopted IaC language.
- **Bicep recipes** provide native, declarative resource deployment for Azure, following Azure best practices.

By using recipes, platform teams can ensure consistency, compliance, and repeatability in how infrastructure is provisioned, while giving developers a simple, application-focused interface.

For more technical details and examples, see the [Radius GitHub repository](https://github.com/radius-project/radius?tab=readme-ov-file#radius).

---

## 🚦 Getting Started

- [📖 Official Radius Documentation](https://docs.radapp.io/)
- [📝 Radius Blog: Platform Engineering with Radius](https://blog.radapp.io/posts/2025/05/13/platform-engineering-with-radius-to-build-application-centric-idps/)
- [💻 Radius GitHub Repository](https://github.com/radius-project/radius?tab=readme-ov-file#radius)

---

## 🏗️ Use Cases

- 🌥️ Organizations seeking to abstract cloud complexity for developers.
- 🔄 Teams wanting a consistent, application-focused workflow across multiple clouds.
- 🛡️ Enterprises needing built-in security, compliance, and policy enforcement.

---

## 🔗 See Also

- [⬅️ Back to IDP Overview](../internal_development_platforms.md)