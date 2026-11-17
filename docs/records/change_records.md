# Change Control Records

## Change Record #001: Initial Service & Non-Root Container Release (v1.0.0)
- **Author:** Student A (HANZOU-LAB)
- **Reviewer:** Student B (Account 2 — Approved via PR #1 & PR #2)
- **Proposed Modification:** Deploy initial Flask information service (`/`, `/health`) packaged in a non-root Python 3.11 container image (`ghcr.io/hanzou-lab/devops-app:e3607902dc10ac8dffbd61fa2043c326949a61a5`).
- **Impact Analysis:** Low risk. New isolated service bound to port 5000 on private lab network.
- **Testing & Verification:** Passed Flake8 static analysis and 3 Pytest unit tests in CI; verified HTTP 200 on `/health`.
- **Approval Status:** Approved and deployed.
- **Recovery / Rollback Plan:** Stop and remove container (`docker rm -f devops-service`) or restore VM snapshot `Base-Environment-Ready`.

## Change Record #002: Release v1.1.0 Upgrade & Automated Deployment Script
- **Author:** Student B (Account 2)
- **Reviewer:** Student A (HANZOU-LAB — Approved via PR #3 & PR #4)
- **Proposed Modification:** Bump displayed service version to `v1.1.0` (`ghcr.io/hanzou-lab/devops-app:546af988f26fbd7b62c66dc8d983332791c556a6`) and introduce `deploy.sh` wrapper for single-command image pull, container replacement, and automated health verification.
- **Impact Analysis:** Medium risk. Replaces running `v1.0.0` container instance during cutover (~3 seconds downtime).
- **Testing & Verification:** Verified CI failure/recovery cycle on PR #3; validated `/health` returns `{"status":"healthy"}` post-deployment.
- **Approval Status:** Approved and deployed.
- **Recovery / Rollback Plan:** Execute `./deploy.sh e3607902dc10ac8dffbd61fa2043c326949a61a5` to immediately revert to the verified `v1.0.0` GHCR image.