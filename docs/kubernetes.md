# ☸️ Kubernetes Overview

Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. Originally developed by Google and now maintained by the Cloud Native Computing Foundation (CNCF), Kubernetes has rapidly become the **de facto standard** for platform engineering teams seeking to build scalable, resilient, and portable infrastructure for modern applications.

> 🖼️ **[See a visual overview of Kubernetes architecture](https://kubernetes.io/docs/concepts/overview/components/#diagram)**

---

## 🚀 Why Kubernetes Is the Platform Engineering Standard

Kubernetes provides a unified API and control plane for managing application workloads, networking, and storage across diverse environments. Its extensibility, strong community support, and robust ecosystem have made it the foundation for many internal developer platforms (IDPs) and cloud-native solutions.

**Platform engineering teams leverage Kubernetes to:**

- ⚡ **Automate** application deployment and scaling  
- 🛠️ **Enable self-service** infrastructure for developers  
- 🔒 **Enforce security, compliance, and operational best practices**  
- 🌎 **Abstract away** underlying infrastructure differences (cloud, on-premises, hybrid)  

---

## 🚦 Getting Started with Kubernetes

- [Install kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Create your first cluster](https://kubernetes.io/docs/setup/)
- [Hello World Deployment Example](https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/)

---

## 🏗️ Kubernetes Architecture: Clusters & Distros

Kubernetes is architected around the concept of a **cluster**, which consists of:

- 🧠 **Control Plane:** API server, scheduler, controller manager  
- 🖥️ **Worker Nodes:** Run application containers

Kubernetes itself is not a single binary or product; it is distributed as a set of components that can be packaged and delivered in different ways, known as **distributions** (distros).

---

### 📦 What Are Kubernetes Distros?

A **Kubernetes distribution (distro)** is a packaged version of Kubernetes, often bundled with additional tools, configuration, and integrations to simplify installation and management. Distros can vary in features, supported platforms, and operational tooling, but all provide the core Kubernetes APIs and functionality.

> **All Kubernetes distros should support the [Open Container Initiative (OCI)](https://opencontainers.org/), a set of open standards for container formats and runtimes developed by the Linux Foundation.**

#### 🏷️ Why the OCI Matters

The **OCI** ensures that containers built and run on different Kubernetes distributions are interoperable and portable. By adhering to OCI standards, distros guarantee that your container images and runtimes will work consistently across local, on-premises, and cloud environments—reducing vendor lock-in and improving developer experience.

- Learn more about the OCI and its specifications at the [Open Container Initiative website](https://opencontainers.org/).

---

## 🌍 Where Can You Deploy Kubernetes?

Kubernetes is highly portable and can be deployed in a variety of environments. For detailed guides, see:

- 💻 **[Locally (Laptop/Workstation)](/docs/kubernetes/local/kubernetes_local.md):**  
  Run a full Kubernetes cluster on your laptop for development and testing.  
  🛠️ These distros are often used in conjunction with your local IDE, such as Visual Studio Code.  
  See our [Local Developer Experience guide](../../../development_setup.md) for further setup and integration tips.

- 🖥️ **[On-Premises / Bare Metal](/docs/kubernetes/baremetal/kubernetes_baremetal.md):**  
  Deploy Kubernetes on physical servers or private data centers.

- ☁️ **[In the Cloud (Hyperscalers)](/docs/kubernetes//hyperscaler/kubernentes_hyperscaler.md):**  
  Use managed Kubernetes services from major cloud providers like Azure, AWS, and Google Cloud.

---

## 🖥️ Interacting with Kubernetes: The `kubectl` CLI

The main way to interact with a Kubernetes cluster is through the [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) command-line tool. `kubectl` lets you deploy applications, inspect and manage cluster resources, and view logs directly from your terminal.

### 🔹 Common `kubectl` Commands

| Action                  | Command                                 |
|-------------------------|-----------------------------------------|
| Check cluster status    | `kubectl cluster-info`                  |
| List nodes              | `kubectl get nodes`                     |
| List pods               | `kubectl get pods`                      |
| Apply config file       | `kubectl apply -f <file.yaml>`          |
| View pod logs           | `kubectl logs <pod-name>`               |

For more commands and advanced usage, see the official [kubectl documentation (CNCF)](https://kubernetes.io/docs/reference/kubectl/).

---

> 🔒 **Security Tip:** Always follow [Kubernetes security best practices](https://kubernetes.io/docs/concepts/security/overview/) when deploying clusters in production.

## 📚 Further Reading

- [Kubernetes Official Documentation](https://kubernetes.io/docs/)
- [CNCF Kubernetes Project Page](https://www.cncf.io/projects/kubernetes/)
- [Kubernetes Blog](https://kubernetes.io/blog/)

---

## 📝 Summary

Kubernetes has become the backbone of modern platform engineering, enabling teams to deliver reliable, scalable, and portable applications across any environment. Whether running locally for development, on bare metal for performance, or in the cloud for scalability, Kubernetes and its many distributions provide the flexibility and power needed for today’s software delivery challenges.