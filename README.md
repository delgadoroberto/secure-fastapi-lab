# Secure FastAPI Lab

A hands-on DevSecOps and Application Security laboratory focused on identifying, exploiting, and remediating common security vulnerabilities in a modern Python API using FastAPI, Docker, and GitHub Actions.

This project demonstrates practical secure coding, CI/CD security automation, dependency scanning, secret detection, container hardening, and vulnerability remediation workflows commonly used in real-world DevSecOps environments.

---

# Objectives

This lab was created to practice:

- Secure coding in Python
- FastAPI security best practices
- GitHub Actions pipelines
- Static Application Security Testing (SAST)
- Secret scanning
- Dependency vulnerability scanning (SCA)
- Docker hardening
- Vulnerability remediation workflows
- DevSecOps automation

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend language |
| FastAPI | API framework |
| Docker | Containerization |
| GitHub Actions | CI/CD pipeline |
| Bandit | Python SAST |
| pip-audit | Dependency vulnerability scanning |
| Trivy | Filesystem vulnerability scanning |
| Gitleaks | Secret detection |
| Hadolint | Dockerfile linting |

---

# Project Structure

```text
secure-fastapi-lab/
├── .github/
│   └── workflows/
│       └── security.yml
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

---

# Security Vulnerabilities Included

The initial version of this application intentionally contains insecure code and configurations for educational purposes.

During the lab, each issue is identified through GitHub Actions and progressively remediated.

| Vulnerability | Description |
|--------------|-------------|
| Hardcoded Secret | API token stored directly in the source code |
| Unsafe Deserialization | Insecure use of `pickle.loads()` |
| Debug Mode Enabled | Debug mode enabled in production configuration |
| Vulnerable Dependencies | Outdated FastAPI and Uvicorn packages |
| Weak Dockerfile | Insecure Docker image configuration |

---

# Security Tools

## Bandit

Static Application Security Testing (SAST) for Python.

Detects insecure coding patterns including:

- Unsafe deserialization
- Debug mode
- Insecure subprocess usage
- Hardcoded secrets
- Weak security practices

---

## pip-audit

Software Composition Analysis (SCA) tool that identifies vulnerable Python dependencies using public vulnerability databases.

---

## Trivy

Filesystem vulnerability scanner capable of detecting:

- Vulnerable dependencies
- Secrets
- Misconfigurations
- Filesystem issues

---

## Gitleaks

Detects accidentally committed secrets such as:

- API keys
- Access tokens
- Passwords
- Cloud credentials
- Private keys

---

## Hadolint

Dockerfile linter that validates Docker security best practices.

Examples include:

- Base image selection
- Layer optimization
- Root user detection
- Package installation practices

---

# CI/CD Pipeline

The GitHub Actions workflow performs automated security verification on every push to the `main` branch.

Pipeline stages:

1. Checkout source code
2. Configure Python environment
3. Execute Bandit (SAST)
4. Execute pip-audit (Dependency Scanning)
5. Execute Trivy Filesystem Scan
6. Execute Gitleaks Secret Scan
7. Execute Hadolint Dockerfile Analysis

---

# Running the Project

## Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/secure-fastapi-lab.git

cd secure-fastapi-lab
```

---

## Create a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the application

```bash
python app.py
```

---

# Running Security Tools Manually

## Bandit

```bash
bandit -r . -ll
```

---

## pip-audit

```bash
pip-audit -r requirements.txt
```

---

## Trivy

```bash
trivy fs .
```

---

## Gitleaks

```bash
gitleaks detect
```

---

## Hadolint

```bash
hadolint Dockerfile
```

---

# Running with Docker

## Build the image

```bash
docker build -t secure-fastapi-lab .
```

---

## Run the container

```bash
docker run -p 8000:8000 secure-fastapi-lab
```

---

# Security Remediation Workflow

The lab is designed to progressively fix each vulnerability.

## Phase 1

Remove hardcoded secrets.

---

## Phase 2

Replace unsafe deserialization (`pickle.loads()`).

---

## Phase 3

Disable debug mode.

---

## Phase 4

Update vulnerable dependencies.

---

## Phase 5

Harden the Dockerfile by:

- Using a pinned base image
- Running as a non-root user
- Reducing image size
- Removing unnecessary cache

---

# Learning Outcomes

After completing this lab, you will have practical experience with:

- Secure Python development
- FastAPI security
- GitHub Actions
- CI/CD security automation
- Application Security (AppSec)
- Software Composition Analysis (SCA)
- Secret detection
- Secure dependency management
- Container hardening
- Docker security
- Secure SDLC
- Vulnerability remediation
- DevSecOps workflows

---

# Repository Roadmap

Future improvements may include:

- CodeQL integration
- Semgrep integration
- SBOM generation
- SARIF report uploads
- Container image scanning
- DAST integration with OWASP ZAP
- Kubernetes deployment
- Runtime security monitoring
- Supply chain security enhancements

---

# Disclaimer

This project intentionally contains insecure code during the initial stages of the lab.

Its sole purpose is educational and should **never** be deployed in production without completing all remediation steps.

---

# Contributing

Contributions are welcome.

Possible improvements include:

- Additional vulnerable scenarios
- New GitHub Actions workflows
- Improved documentation
- Additional security scanners
- FastAPI security examples
- CI/CD enhancements

Please open an issue before submitting major changes.

---

# License

This project is released under the MIT License.

---

# Author

**Roberto Delgado**

Cybersecurity Engineer
