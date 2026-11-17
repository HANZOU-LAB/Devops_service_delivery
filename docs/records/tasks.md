# Project Task Plan & Weekly Work Record

| Date | Task Planned | Task Completed | Owner | Status | Evidence Link | Problem & Next Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Day 1 | Linux VM setup, named accounts, UFW firewall, snapshot | Configured `studenta`/`studentb`, `/opt/devops-app` (`775`), UFW (`22`, `5000`), VM snapshot | Student A | Complete | `docs/records/evidence_index.md` | None; proceed to containerization |
| Day 1 | Develop Flask service (`/`, `/health`), unit tests, non-root Dockerfile | Created `app.py`, `test_app.py`, `Dockerfile` (`USER appuser`) | Student B | Complete | PR #1 | None; configure CI workflow |
| Day 1 | Configure GitHub Actions CI/CD & GHCR push | Created `.github/workflows/ci.yml` with Flake8, Pytest, GHCR build | Student B | Complete | PR #2 | Enabled Workflow Read/Write permissions |
| Day 1 | Simulate CI failure & recovery | Induced broken `/health` response, verified failed CI run, fixed & merged to `v1.1.0` | Student A | Complete | PR #3 | None; proceed to deployment |
| Day 1 | Deploy `v1.0.0` & `v1.1.0`, incident simulation, rollback & `deploy.sh` | Deployed both SHAs, simulated outage, executed rollback, created `deploy.sh` | Student A & B | Complete | PR #4 & `incident_record.md` | Package final submission |