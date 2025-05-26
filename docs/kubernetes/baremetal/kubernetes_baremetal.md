# 🖥️ Bare Metal Kubernetes Clusters

A **bare metal Kubernetes cluster** is deployed directly onto physical servers, rather than virtual machines or cloud infrastructure. This approach is often chosen for maximum performance, control, and cost efficiency—especially in environments where low latency, high throughput, or data sovereignty are critical.

Bare metal deployments are common in:

- On-premises data centers
- Edge computing environments
- High-performance computing (HPC) clusters

---

## 🏆 Popular Bare Metal Kubernetes Distributions

Below are some of the most widely used Kubernetes distros for bare metal deployments:

| Distro      | Lightweight | HA Support | Enterprise Features | Easy Install | Docs/Links         |
|-------------|:-----------:|:----------:|:------------------:|:------------:|--------------------|
| **MicroK8s**    | ✅          | ✅         | ❌                 | ✅           | [Docs](https://microk8s.io/docs) |
| **k3s**         | ✅          | ✅         | ❌                 | ✅           | [Docs](https://docs.k3s.io/)     |
| **RKE**         | ❌          | ✅         | ❌                 | ✅           | [Docs](https://rancher.com/docs/rke/latest/en/) |
| **OpenShift**   | ❌          | ✅         | ✅                 | ⚠️           | [Docs](https://docs.openshift.com/) |
| **Kubespray**   | ❌          | ✅         | ❌                 | ⚠️ (Ansible) | [Docs](https://kubespray.io/)    |

1. **⚡ MicroK8s**  
   - *A lightweight, production-grade Kubernetes distribution from Canonical (the makers of Ubuntu). MicroK8s is easy to install, supports high availability, and is great for both development and production on bare metal.*  
   [Docs](https://microk8s.io/docs)

2. **🥇 k3s**  
   - *A highly efficient, CNCF-certified Kubernetes distribution designed for resource-constrained environments. k3s is ideal for edge, IoT, and bare metal clusters where simplicity and low overhead are priorities.*  
   [Docs](https://docs.k3s.io/)

3. **🏢 Rancher Kubernetes Engine (RKE)**  
   - *A simple, lightning-fast Kubernetes installer that works on bare metal and virtualized servers. Maintained by Rancher, known for ease of use and flexibility.*  
   [Docs](https://rancher.com/docs/rke/latest/en/)

4. **🏗️ OpenShift**  
   - *Red Hat OpenShift is an enterprise Kubernetes platform that can be deployed on bare metal, providing advanced features for security, developer experience, and multi-tenancy.*  
   [Docs](https://docs.openshift.com/)

5. **🛠️ Kubespray**  
   - *An open-source project that uses Ansible playbooks to deploy production-ready Kubernetes clusters on bare metal or any infrastructure. Highly customizable and supports advanced networking and storage options.*  
   [Docs](https://kubespray.io/)

---

> **When to use which?**  
> - Use **MicroK8s** or **k3s** for lightweight, fast setups or edge/IoT.  
> - Use **RKE** for Rancher-managed clusters.  
> - Use **OpenShift** for enterprise features and support.  
> - Use **Kubespray** for maximum flexibility and custom networking/storage.

> 🔒 **Security Tip:** Bare metal clusters require you to manage your own OS and network security. Always follow [Kubernetes security best practices](https://kubernetes.io/docs/concepts/security/overview/).

## 📚 Further Reading

- [Kubernetes Official Documentation](https://kubernetes.io/docs/setup/production-environment/tools/)
- [CNCF Landscape: Kubernetes Installers](https://landscape.cncf.io/?category=platform&format=card-mode&grouping=category)

---

Each of these distributions is well-suited for running Kubernetes on physical servers, offering a range of features from lightweight simplicity to full enterprise capabilities. Choose the one that best fits your operational needs and expertise.