# Evidence Index & Assistance Disclosure

## 1. Repository & Releases
- **Repository URL:** `https://github.com/HANZOU-LAB/Devops_service_delivery`
- **Release Tags:** `v1.0.0` and `v1.1.0`

## 2. Pull Requests & Peer Reviews
- **PR #1 (`feature/initial-app`):** Initial Flask service and non-root Dockerfile — Authored by HANZOU-LAB (Account 1), Reviewed & Approved by Account 2.
- **PR #2 (`feature/ci-pipeline`):** Pytest suite and GitHub Actions CI/CD workflow — Authored by Account 2, Reviewed & Approved by HANZOU-LAB (Account 1).
- **PR #3 (`feature/ci-failure-demo`):** Intentional CI failure demonstration, fix, and `v1.1.0` bump — Authored by HANZOU-LAB (Account 1), Reviewed & Approved by Account 2.
- **PR #4 (`feature/deploy-and-docs`):** Automated `deploy.sh` script and project audit records — Authored by Account 2, Reviewed & Approved by HANZOU-LAB (Account 1).

## 3. CI/CD Pipeline Runs & Artifacts
- **Failed CI Run:** Actions workflow run on PR #3 initial commit (blocked artifact build on failed Pytest assertion).
- **Successful CI Run:** Actions workflow run on PR #3 fix commit and `main` merge.
- **Artifact 1 (`v1.0.0`):** `ghcr.io/hanzou-lab/devops-app:e3607902dc10ac8dffbd61fa2043c326949a61a5`
- **Artifact 2 (`v1.1.0`):** `ghcr.io/hanzou-lab/devops-app:546af988f26fbd7b62c66dc8d983332791c556a6`

## 4. Process Improvement (Before vs. After)
- **Before:** Manual 4-step deployment (`docker pull`, `docker stop`, `docker rm`, `docker run` with manual port/env flags), taking ~35 seconds and prone to flag typos.
- **After:** Single-command `./deploy.sh <SHA>` execution with built-in `/health` verification, verified in ~3.2 seconds.

## 5. Assistance & References Disclosure
- Official Flask, Pytest, Docker, and GitHub Actions documentation referenced for configuration syntax.
- AI assistance was used to structure boilerplate templates and documentation formatting; all code, pipelines, Linux configurations, and operational tests were executed and verified directly by the student.