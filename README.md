# Secure FastAPI Lab

A hands-on DevSecOps and Application Security laboratory focused on identifying, exploiting, and remediating common security vulnerabilities in a modern Python API using FastAPI, Docker, and GitHub Actions.

This project demonstrates practical secure coding, CI/CD security automation, dependency scanning, secret detection, container hardening, and vulnerability remediation workflows commonly used in real-world DevSecOps environments.

---

# Objectives

This lab was created to practice:

- Secure coding in Python
- FastAPI security best practices
- GitHub Actions pipelines
- SAST (Static Application Security Testing)
- Secret scanning
- Dependency vulnerability scanning
- Docker hardening
- Vulnerability remediation workflows
- DevSecOps automation

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend language |
| FastAPI | API framework |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |
| Bandit | Python SAST |
| pip-audit | Dependency scanning |
| Trivy | Filesystem vulnerability scanning |
| Gitleaks | Secret detection |
| Hadolint | Dockerfile linting |

---

# Project Structure

```text
secure-fastapi-lab/
├── app.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── security.yml
