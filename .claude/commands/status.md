---
description: "Check health status of development and deployed app"
---

# Check App Status

I'll check the health status of both your local development environment and deployed Databricks app.

## What I'll check:

1. **Development Environment** - Local development server status
2. **Authentication** - Databricks connectivity and credentials
3. **Deployed App** - Production app health and status
4. **System Health** - Dependencies and configuration
5. **Provide Summary** - Clear status report with next steps

## Status Check Workflow

**Step 1: Development Environment Status**
```bash
# Check if development servers are running
ps aux | grep databricks-app

# Check PID file
cat /tmp/databricks-app-watch.pid

# Check recent logs
tail -10 /tmp/databricks-app-watch.log
```

**Step 2: Authentication Status**
```bash
# Test Databricks authentication
databricks current-user me

# Test with profile if configured
databricks current-user me --profile "$DATABRICKS_CONFIG_PROFILE"

# Check .env.local configuration
cat .env.local
```

**Step 3: Deployed App Status**
```bash
# Check app status with nice formatting
./app_status.sh

# Get detailed app information
databricks apps get "$DATABRICKS_APP_NAME"
```

**Step 4: System Health Check**
```bash
# Check required tools
uv --version
bun --version
databricks --version

# Check project structure
ls -la server/app.py
ls -la client/package.json
ls -la .env.local
```

## Status Dashboard

### 🖥️ Development Environment

**Development Servers:**
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

**Status Indicators:**
- ✅ **RUNNING** - Servers are active and responding
- ⏸️ **STOPPED** - Servers are not running
- ❌ **ERROR** - Servers failed to start or crashed

**Quick Actions:**
- Start: `nohup ./watch.sh > /tmp/databricks-app-watch.log 2>&1 &`
- Stop: `kill $(cat /tmp/databricks-app-watch.pid) || pkill -f watch.sh`
- Restart: Stop, then start
- Logs: `tail -f /tmp/databricks-app-watch.log`

### 🔐 Authentication Status

**Authentication Method:**
- 🔑 **PAT** - Personal Access Token
- 👤 **Profile** - CLI Profile authentication

**Status Indicators:**
- ✅ **AUTHENTICATED** - Successfully connected to Databricks
- ❌ **FAILED** - Authentication failed or expired
- ⚠️ **MISSING** - No credentials configured

**Quick Actions:**
- Test: `databricks current-user me`
- Reconfigure: `./setup.sh`
- Check config: `cat .env.local`

### 🚀 Deployed App Status

**App Information:**
- Name: `$DATABRICKS_APP_NAME`
- URL: [Retrieved from databricks apps get]
- Status: [RUNNING/UNAVAILABLE/STARTING/FAILED]

**Status Indicators:**
- ✅ **RUNNING** - App is active and serving requests
- ⏳ **STARTING** - App is deploying or starting up
- ❌ **UNAVAILABLE** - App failed to start or crashed
- ⚠️ **NOT_DEPLOYED** - App exists but no deployment

**Quick Actions:**
- Deploy: `./deploy.sh`
- Logs: Visit app URL + `/logz` in browser
- Debug: `./run_app_local.sh --verbose`

### 🔧 System Health

**Required Tools:**
- ✅ **uv** - Python package manager
- ✅ **bun** - JavaScript package manager  
- ✅ **databricks** - CLI tool
- ✅ **python** - Runtime environment

**Configuration Files:**
- ✅ **`.env.local`** - Environment configuration
- ✅ **`server/app.py`** - Backend application
- ✅ **`client/package.json`** - Frontend configuration

## Quick Status Summary

I'll provide a visual summary like this:

```
🏠 DEVELOPMENT ENVIRONMENT
   Frontend (3000):  ✅ RUNNING
   Backend (8000):   ✅ RUNNING
   Hot Reload:       ✅ ACTIVE
   
🔐 AUTHENTICATION
   Method:           🔑 PAT
   Status:           ✅ AUTHENTICATED
   User:             user@company.com
   
🚀 DEPLOYED APP
   Name:             my-databricks-app
   Status:           ✅ RUNNING
   URL:              https://my-app.databricksapps.com
   Last Deploy:      2 minutes ago
   
🔧 SYSTEM HEALTH
   Dependencies:     ✅ ALL GOOD
   Configuration:    ✅ VALID
   Permissions:      ✅ SUFFICIENT
```

## Common Status Issues

### Development Server Issues
- **Port conflicts**: Kill processes on ports 3000/8000
- **Startup failures**: Check `/tmp/databricks-app-watch.log`
- **Hot reload broken**: Restart development servers

### Authentication Issues
- **Token expired**: Generate new PAT or re-authenticate
- **Profile missing**: Configure with `databricks auth login`
- **Permission denied**: Check workspace access

### Deployment Issues
- **App not found**: Create with `./deploy.sh --create`
- **Deployment failed**: Check app logs at URL + `/logz`
- **App unavailable**: Redeploy or check for errors

### System Issues
- **Missing tools**: Install with package managers
- **Config missing**: Run `./setup.sh`
- **Permission problems**: Check file permissions

## Next Steps Based on Status

**If everything is ✅ GOOD:**
- Continue development
- Your app is ready for use

**If development is ❌ FAILED:**
- Use `/dev` to start development servers
- Check logs for specific errors

**If authentication is ❌ FAILED:**
- Run `./setup.sh` to reconfigure
- Check token validity

**If deployment is ❌ FAILED:**
- Use `/deploy` to redeploy
- Use `/debug` for comprehensive troubleshooting

**If system health is ❌ FAILED:**
- Install missing dependencies
- Run `./setup.sh` for configuration

## Monitoring Commands

**Real-time monitoring:**
```bash
# Watch development logs
tail -f /tmp/databricks-app-watch.log

# Monitor app status
watch -n 30 ./app_status.sh

# Check system resources
top -p $(cat /tmp/databricks-app-watch.pid)
```

Your status report is ready! 📊