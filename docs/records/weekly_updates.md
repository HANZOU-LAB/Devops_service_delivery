cat << 'EOF' > docs/records/weekly_updates.md
# Stakeholder Weekly Status Updates

## Update 1 — Environment & Application Baseline
- **Completed Work:** Provisioned isolated Ubuntu lab VM, created named accounts (`studenta`, `studentb`), configured `/opt/devops-app` (`775`), enabled UFW (`22/tcp`, `5000/tcp`), captured snapshot `Base-Environment-Ready`, and merged PR #1 (Flask app + non-root `Dockerfile`).
- **Next Work:** Configure GitHub Actions CI/CD pipeline (`Flake8`, `Pytest`, GHCR image push) and demonstrate CI failure/recovery.
- **Current Risks:** Docker registry tag casing constraints on GHCR (mitigated by enforcing lowercase `ghcr.io/hanzou-lab/devops-app`).
- **Decisions Needed:** None.

## Update 2 — CI/CD, Automated Deployment, Incident & Rollback
- **Completed Work:** Merged PR #2 (CI pipeline), demonstrated intentional CI failure and recovery in PR #3, published versioned GHCR artifacts, created `deploy.sh` (PR #4), and executed controlled `docker stop` outage recovery and timed rollback tests.
- **Next Work:** Finalize Word technical report and prepare 10-minute live demonstration.
- **Current Risks:** None; both release tags and rollback artifacts are verified and publicly pullable from GHCR.
EOF