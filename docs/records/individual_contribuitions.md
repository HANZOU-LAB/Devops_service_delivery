cat << 'EOF' > docs/records/individual_contributions.md
# Individual Contribution Log & Reflection

## Student A — HANZOU-LAB
- **Completed Tasks:**
  - **Linux Administration:** Configured Ubuntu VM, created `studenta` and `studentb`, set `/opt/devops-app` (`775`, group `docker`), enabled UFW firewall (`22/tcp`, `5000/tcp`), verified `df -h` / `free -m` / `systemctl is-active docker`, and created snapshot `Base-Environment-Ready`.
  - **Implementation & CI:** Authored PR #1 (Flask service and non-root `Dockerfile`) and PR #3 (induced CI failure, fix, and version bump); resolved uppercase GHCR tag error in `.github/workflows/ci.yml`.
  - **Peer Reviews:** Reviewed and approved PR #2 and PR #4.
  - **Operations:** Executed `./deploy.sh cb128cd4095629584654b588ebf26b152876053b`, simulated `docker stop` outage, and performed timed rollback.
- **Personal Difficulty & Reflection:** Initially, the GitHub Actions `docker/build-push-action` failed because `${{ github.repository_owner }}` expanded to uppercase `HANZOU-LAB`, which Docker rejects for registry paths. I diagnosed the buildx log, enforced lowercase `ghcr.io/hanzou-lab/devops-app` in both `ci.yml` and `deploy.sh`, and verified the green build. For future projects, I would add a pre-build validation step or lowercase string filter (`tr '[:upper:]' '[:lower:]'`) directly in the workflow environment variables.

## Student B — Account 2 (Teammate Role)
- **Completed Tasks:**
  - **Testing & CI Pipeline:** Authored PR #2 (`test_app.py` with 3 unit tests covering `/`, `/health`, and 404 edge case, plus `.github/workflows/ci.yml`).
  - **Automation & Documentation:** Authored PR #4 (`deploy.sh` wrapper with automated `/health` check, `README.md` runbook, and `docs/records/` audit logs).
  - **Peer Reviews:** Reviewed and approved PR #1 and PR #3.
- **Personal Difficulty & Reflection:** Manual 4-step Docker deployments (`pull`, `stop`, `rm`, `run`) were slow (~35s) and prone to flag omissions during rollback tests. Encapsulating the deployment and health verification inside `deploy.sh` reduced cutover time to ~3.4 seconds and eliminated configuration drift. Next time, I would extend `deploy.sh` to automatically save the previously running image tag to a state file (`.last_good_sha`) for one-click rollback without copying SHA hashes manually.
EOF