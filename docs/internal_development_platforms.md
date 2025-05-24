# 🛠️ Internal Developer Platforms (IDPs): Overview & Guide

## 📚 Table of Contents
- [What is an Internal Developer Platform (IDP)?](#-what-is-an-internal-developer-platform-idp)
- [Why Do Platform Engineering Teams Deploy IDPs?](#-why-do-platform-engineering-teams-deploy-idps)
- [How Platform Engineering Improves Developer Experience with IDPs](#-how-platform-engineering-improves-developer-experience-with-idps)
- [Glossary](#-glossary)
- [Top 5 Internal Developer Platforms (IDPs)](#-top-5-internal-developer-platforms-idps)
- [Deep Dives: Popular IDPs](#-deep-dives-popular-idps)
- [Further Reading](#-further-reading)

---

## ❓ What is an Internal Developer Platform (IDP)?

An **Internal Developer Platform (IDP)** is not a single product, but a curated set of self-service tools, services, and automation built by platform engineering teams to streamline and standardize the software delivery process for developers within an organization. IDPs abstract away infrastructure complexity, standardize workflows, and empower developers to build, deploy, and manage applications efficiently and securely.

---

## 🚀 Why Do Platform Engineering Teams Deploy IDPs?

Platform engineering teams deploy IDPs to:
- ✨ **Improve Developer Experience:** Reduce cognitive load and context switching by providing easy-to-use interfaces and automation.
- ⚡ **Accelerate Delivery:** Enable faster, safer deployments with standardized pipelines and environments.
- 🛡️ **Increase Consistency:** Enforce best practices, security, and compliance across teams.
- 👩‍💻 **Empower Developers:** Allow developers to focus on writing code, not managing infrastructure.

> **Platform Engineering’s Role:**  
> Platform engineering is responsible for designing, building, and maintaining IDPs. Their goal is to provide “golden paths” and self-service capabilities that enable developers to deliver value quickly and safely, while ensuring organizational standards are met. ([Platform Engineering Community](https://platformengineering.org/))

---

## 🏗️ How Platform Engineering Improves Developer Experience with IDPs

- 🖥️ **Self-Service Portals:** Developers can provision environments, deploy apps, and manage resources without waiting for ops teams.
- 🛤️ **Golden Paths:** Predefined, organization-approved workflows and templates for common tasks.
- 📊 **Observability & Feedback:** Built-in monitoring, logging, and feedback loops.
- 🛡️ **Security & Compliance:** Automated policy enforcement and guardrails.
- 🔗 **Integration:** Seamless integration with CI/CD, cloud providers (including ☁️ Azure, AWS, GCP), and internal tools.

---

## 🗂️ Glossary

- **Golden Path:** A pre-approved, best-practice workflow or template for building and deploying software.
- **Service Catalog:** A centralized inventory of all software services, components, and APIs in an organization.
- **Self-Service:** The ability for developers to provision resources or deploy applications without manual intervention from operations teams.

---

# 🏆 Top 5 Internal Developer Platforms (IDPs)

Below are five leading IDPs, each with unique strengths and community support.  
For a quick comparison, see the table below.

| 🏷️ Platform  | 🆓 Open Source | ☁️ Cloud Support           | 🧩 Extensibility | 🌟 Notable For                        |
|--------------|---------------|---------------------------|-----------------|---------------------------------------|
| Backstage    | Yes           | Any (via plugins)         | High            | Software catalog, plugin ecosystem    |
| Humanitec    | No            | Kubernetes, Cloud         | Medium          | Dynamic environments, EaaS            |
| Port         | Yes           | Any (via integrations)    | High            | Flexible data modeling, UI            |
| Cortex       | No            | Any                       | Medium          | Service scorecards, reliability       |
| Radius       | Yes           | Azure, AWS, GCP           | High            | Application-centric, cloud-native     |

---

## 🔍 Deep Dives: Popular IDPs

For detailed breakdowns, best practices, and setup guides, see the following sub-readmes:

- [🚀 Backstage: Getting Started & Best Practices](./idps/backstage.md)
- [🏢 Humanitec: Features & Integration](./idps/humanitec.md)
- [🛠️ Port: Custom Workflows & Extensibility](./idps/port.md)
- [🏷️ Cortex: Service Catalog & Scorecards](./idps/cortex.md)
- [🌐 Radius: Application-Centric Platform Engineering](./idps/radius.md)

---

## 📖 Further Reading

- [🌍 Platform Engineering Community](https://platformengineering.org/)
- [📊 CNCF Bakcstage Project](https://www.cncf.io/projects/backstage/)
- [☁️ Azure Platform Engineering Guidance](https://learn.microsoft.com/en-us/platform-engineering/)
- [📝 Radius Blog: Platform Engineering with Radius](https://blog.radapp.io/posts/2025/05/13/platform-engineering-with-radius-to-build-application-centric-idps/)

---

> **ℹ️ Tip:**  
> This guide is designed to be accessible and actionable for platform engineers and developers exploring IDPs. For detailed setup and usage, see the sub-readmes linked above.
