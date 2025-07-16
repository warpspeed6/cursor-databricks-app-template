# Databricks App Template Development Guide

## Project Memory

This is a modern full-stack application template for Databricks Apps, featuring FastAPI backend with React TypeScript frontend and modern development tooling.

## Tech Stack

**Backend:**
- Python with `uv` for package management
- FastAPI for API framework
- Databricks SDK for workspace integration
- OpenAPI automatic client generation

**Frontend:**
- TypeScript with React
- Vite for fast development and hot reloading
- shadcn/ui components with Tailwind CSS
- React Query for API state management
- Bun for package management

## Development Workflow

### Package Management
- Use `uv add/remove` for Python dependencies, not manual edits to pyproject.toml
- Use `bun add/remove` for frontend dependencies, not manual package.json edits
- Always check if dependencies exist in the project before adding new ones

### Development Commands
- `./setup.sh` - Interactive environment setup and dependency installation
- `./watch.sh` - Start development servers with hot reloading (frontend:3000, backend:8000)
- `./fix.sh` - Format code (ruff for Python, prettier for TypeScript)
- `./deploy.sh` - Deploy to Databricks Apps

### 🚨 IMPORTANT: NEVER RUN THE SERVER MANUALLY 🚨

**ALWAYS use the watch script with nohup and logging:**

```bash
# Start development servers (REQUIRED COMMAND)
nohup ./watch.sh > /tmp/databricks-app-watch.log 2>&1 &

# Or for production mode
nohup ./watch.sh --prod > /tmp/databricks-app-watch.log 2>&1 &
```

**NEVER run uvicorn or the server directly!** Always use `./watch.sh` as it:
- Configures environment variables properly
- Starts both frontend and backend correctly
- Generates TypeScript client automatically
- Handles authentication setup
- Provides proper logging and error handling

### 🚨 PYTHON EXECUTION RULE 🚨

**NEVER run `python` directly - ALWAYS use `uv run`:**

```bash
# ✅ CORRECT - Always use uv run
uv run python script.py
uv run uvicorn server.app:app
uv run scripts/make_fastapi_client.py

# ❌ WRONG - Never use python directly
python script.py
uvicorn server.app:app
python scripts/make_fastapi_client.py
```

### Claude Natural Language Commands
Claude understands natural language commands for common development tasks:

**Development Lifecycle:**
- "start the devserver" → Runs `./watch.sh` in background with logging
- "kill the devserver" → Stops all background development processes
- "fix the code" → Runs `./fix.sh` to format Python and TypeScript code
- "deploy the app" → Runs `./deploy.sh` to deploy to Databricks Apps

**Development Tasks:**
- "add a new API endpoint" → Creates FastAPI routes with proper patterns
- "create a new React component" → Builds UI components using shadcn/ui
- "debug this error" → Analyzes logs and fixes issues
- "install [package]" → Adds dependencies using uv (Python) or bun (frontend)
- "generate the TypeScript client" → Regenerates API client from OpenAPI spec
- "open the UI in playwright" → Opens the frontend app in Playwright browser for testing

### Development Server
- **ALWAYS** run `./watch.sh` with nohup in background and log to file for debugging
- Watch script automatically runs in background and logs to `/tmp/databricks-app-watch.log`
- Frontend runs on http://localhost:3000
- Backend runs on http://localhost:8000
- API docs available at http://localhost:8000/docs
- Supports hot reloading for both frontend and backend
- Automatically generates TypeScript client from FastAPI OpenAPI spec
- **Check logs**: `tail -f /tmp/databricks-app-watch.log`
- **Stop processes**: `pkill -f "watch.sh"` or check PID file

### Code Quality
- Use `./fix.sh` for code formatting before commits
- Python: ruff for formatting and linting
- TypeScript: prettier for formatting, ESLint for linting
- Type checking with TypeScript

### API Development
- FastAPI automatically generates OpenAPI spec
- TypeScript client is auto-generated from OpenAPI spec
- Test endpoints with curl or FastAPI docs
- Check server logs after requests
- Verify response includes expected fields

### Frontend Development
- Use shadcn/ui components for consistent UI
- Follow React Query patterns for API calls
- Use TypeScript strictly - no `any` types
- Import from auto-generated client: `import { apiClient } from '@/fastapi_client'`
- Client uses shadcn/ui components with proper TypeScript configuration
- shadcn components must be added with: npx shadcn@latest add <component-name>

### Testing Methodology
- Test API endpoints using FastAPI docs interface
- Use browser dev tools for frontend debugging
- Check network tab for API request/response inspection
- Verify console for any JavaScript errors

### Deployment
- Use `./deploy.sh` for Databricks Apps deployment
- Automatically builds frontend and generates requirements.txt
- Configures app.yaml with environment variables
- Verifies deployment through Databricks CLI
- **IMPORTANT**: After deployment, monitor `/logz` endpoint of your Databricks app to check for installation issues
- App logs are available at: `https://<app-url>/logz` (visit in browser - requires OAuth authentication)

### Environment Configuration
- Use `.env.local` for local development configuration
- Set environment variables and Databricks credentials
- Never commit `.env.local` to version control
- Use `./setup.sh` to create and update environment configuration

### Debugging Tips
- Verify environment variables are set correctly
- Use FastAPI docs for API testing: http://localhost:8000/docs
- Check browser console for frontend errors
- Use React Query DevTools for API state inspection
- **Check watch logs**: `tail -f /tmp/databricks-app-watch.log` for all development server output
- **Check process status**: `ps aux | grep databricks-app` or check PID file at `/tmp/databricks-app-watch.pid`
- **Force stop**: `kill $(cat /tmp/databricks-app-watch.pid)` or `pkill -f watch.sh`

### Key Files
- `server/app.py` - FastAPI application entry point
- `server/routers/` - API endpoint routers
- `client/src/App.tsx` - React application entry point
- `client/src/pages/` - React page components
- `scripts/make_fastapi_client.py` - TypeScript client generator
- `pyproject.toml` - Python dependencies and project configuration
- `client/package.json` - Frontend dependencies and scripts

### Common Issues
- If TypeScript client is not found, run the client generation script manually
- If hot reload not working, restart `./watch.sh`
- If dependencies missing, run `./setup.sh` to reinstall

Remember: This is a development template focused on rapid iteration and modern tooling.