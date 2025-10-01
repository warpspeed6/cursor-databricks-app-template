# /dba — Databricks App Helper

Use this command inside Cursor to scaffold, run, test, and deploy the Databricks App in this repo.  
**Trigger:** Type `/dba` in Cursor and select this command.

## What this command does
- Installs local tooling (uv, bun, Node, Playwright, Databricks CLI) using the repo's scripts.
- Runs the FastAPI backend and React frontend locally with hot reload.
- Deploys (or redeploys) the App to your Databricks workspace as defined in `app.yaml`.
- Provides quick troubleshooting steps for common issues (auth, missing tools, ports).

## Pre-reqs (once per machine)
- Databricks Personal Access Token (PAT) or configured `databricks` CLI profile with workspace access.
- Shell with `bash` and permission to execute `*.sh` scripts.
- Internet access for package/tool downloads.

## Quick Start
1. **Install tools & setup project**
   ```bash
   chmod +x ./setup.sh ./run_app_local.sh ./deploy.sh || true
   ./setup.sh
   ```

2. **Run locally (dev mode)**
   ```bash
   ./run_app_local.sh
   ```
   - Backend: http://localhost:8000
   - Frontend: http://localhost:5173
   - API docs: http://localhost:8000/docs

3. **Deploy to Databricks**
   ```bash
   ./deploy.sh
   ```

## Troubleshooting
- **Auth issues**: Run `databricks auth login` or set `DATABRICKS_TOKEN` env var
- **Port conflicts**: Kill processes on 8000/5173 or modify ports in scripts
- **Missing tools**: Re-run `./setup.sh` to install missing dependencies
- **Build errors**: Check `client/package.json` and `pyproject.toml` for version conflicts

## Scripts Reference
- `setup.sh` - Installs all required tools and dependencies
- `run_app_local.sh` - Starts local development servers
- `deploy.sh` - Deploys app to Databricks workspace
- `watch.sh` - Runs app with file watching for development
- `fix.sh` - Fixes common issues and regenerates client code
