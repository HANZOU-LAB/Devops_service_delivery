mkdir -p docs/records && cat << 'EOF' > docs/records/risk_register.md
# Project Risk Register

| Risk ID | Risk Description | Likelihood | Impact | Mitigation / Control | Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R-01 | Broken code or failing tests pushed directly to `main` | Medium | High | Branch protection via PR reviews + GitHub Actions CI blocking image build on Flake8/Pytest failure | Student B | Mitigated |
| R-02 | Container running as `root` increases host compromise impact | Low | High | Defined dedicated non-root `appuser` inside `Dockerfile` (`USER appuser`) | Student A | Mitigated |
| R-03 | Accidental exposure of PATs or registry tokens in Git | Low | High | `.gitignore` configured; CI uses ephemeral `secrets.GITHUB_TOKEN` with least-privilege permissions | Student A & B | Mitigated |
| R-04 | Service downtime during release upgrade or bad deployment | Medium | Medium | Automated `deploy.sh` health probe + verified rollback to prior GHCR SHA (`cb128cd4095629584654b588ebf26b152876053b`) | Student A & B | Mitigated |
| R-05 | Unauthorized network access to lab VM ports | Medium | Medium | UFW firewall configured with default `deny incoming`, allowing only `22/tcp` and `5000/tcp` | Student A | Mitigated |
EOF