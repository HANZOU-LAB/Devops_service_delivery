# Incident & Rollback Record (INC-2026-01)

## Part A: Controlled Service Failure & Recovery
- **Detection Time:** Day 1, 14:10 UTC
- **Detected By:** Operator health probe (`curl -i http://localhost:5000/health`)
- **Symptoms:** Probe failed with `curl: (7) Failed to connect to localhost port 5000: Connection refused`.
- **Diagnostic Evidence:**
  - `docker ps -a` showed container `devops-service` in `Exited (137)` state.
  - `docker logs devops-service` showed termination signal (`Handling signal: term`).
- **Recovery Action:** Executed `docker start devops-service`.
- **Verification & Recovery Time:** Confirmed HTTP 200 `{"status":"healthy"}` via `curl -s http://localhost:5000/health`. Actual recovery time: **~2 seconds**.

## Part B: Release Rollback Demonstration (v1.1.0 -> v1.0.0)
- **Trigger:** Simulated release rollback requirement from `v1.1.0` (`546af988f26fbd7b62c66dc8d983332791c556a6`) to prior working artifact `v1.0.0` (`e3607902dc10ac8dffbd61fa2043c326949a61a5`).
- **Rollback Command:** `./deploy.sh e3607902dc10ac8dffbd61fa2043c326949a61a5`
- **Verification:**
  - `curl -s http://localhost:5000/` confirmed displayed version reverted to `e3607902dc10ac8dffbd61fa2043c326949a61a5` (`v1.0.0`).
  - `curl -s http://localhost:5000/health` returned `{"status":"healthy"}`.
- **Actual Rollback Time:** **~3.4 seconds**.