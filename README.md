# 🚀 Databricks FastAPI App Template

A modern, full-stack application template for building Databricks Apps with Python FastAPI backend and React TypeScript frontend.

![Databricks Apps](https://img.shields.io/badge/Databricks-Apps-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green)
![React](https://img.shields.io/badge/React-18+-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5+-blue)

## ✨ Features

- **🔥 Hot Reloading** - Instant updates for both Python backend and React frontend
- **🔄 Auto-Generated API Client** - TypeScript client automatically generated from FastAPI OpenAPI spec
- **🔐 Databricks Authentication** - Integrated with Databricks SDK for seamless workspace integration
- **🎨 Modern UI** - Beautiful components using shadcn/ui + Tailwind CSS
- **📦 Package Management** - uv for Python, bun for frontend
- **🚀 Databricks Apps Ready** - Pre-configured for deployment to Databricks Apps platform
- **🤖 Claude Integration** - Natural language development commands documented

## 🏗️ Project Structure

```
├── server/                    # FastAPI backend
│   ├── app.py                 # Main application
│   ├── routers/               # API route handlers
│   │   └── __init__.py        # Example router
│   └── services/              # Business logic
│
├── client/                    # React frontend
│   ├── src/
│   │   ├── pages/            # React pages
│   │   ├── components/       # UI components
│   │   ├── lib/             # Utilities
│   │   └── fastapi_client/  # Generated API client
│   ├── package.json         # Frontend dependencies
│   └── vite.config.ts       # Vite configuration
│
├── scripts/                   # Development automation
│   ├── setup.sh             # Environment setup
│   ├── watch.sh             # Development server
│   ├── fix.sh               # Code formatting
│   └── deploy.sh            # Deployment
│
├── pyproject.toml            # Python dependencies
├── app.yaml                  # Databricks Apps config
└── CLAUDE.md                 # Development guide
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
./setup.sh
```

This interactive script will:
- Set up Databricks authentication (PAT or profile)
- Install Python dependencies with uv
- Install frontend dependencies with bun
- Configure environment variables

### 2. Start Development

```bash
./watch.sh
```

This runs both servers in the background:
- **Frontend**: http://localhost:3000
- **Backend**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### 3. View Your App

Open http://localhost:3000 to see the beautiful welcome page with:
- Getting Started guide
- Claude Commands reference
- Tech Stack overview
- Project Structure visualization
- Current user information from Databricks

## 🧠 Claude Commands

This template includes natural language commands that Claude understands:

### Development Lifecycle
- `"start the devserver"` → Runs development servers
- `"kill the devserver"` → Stops background processes
- `"fix the code"` → Formats Python and TypeScript code
- `"deploy the app"` → Deploys to Databricks Apps

### Development Tasks
- `"add a new API endpoint"` → Creates FastAPI routes
- `"create a new React component"` → Builds UI components
- `"open the UI in playwright"` → Opens app in browser for testing
- `"debug this error"` → Analyzes logs and fixes issues

See `CLAUDE.md` for the complete development guide.

## 🛠️ Development Commands

| Command | Description |
|---------|-------------|
| `./setup.sh` | Interactive environment setup |
| `./watch.sh` | Start dev servers (background) |
| `./fix.sh` | Format code (Python + TypeScript) |
| `./deploy.sh` | Deploy to Databricks Apps |

## 🧪 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **uv** - Ultra-fast Python package management
- **Databricks SDK** - Workspace integration
- **Automatic OpenAPI** - Generated documentation

### Frontend
- **React 18** - Modern React with TypeScript
- **Vite** - Lightning-fast build tool
- **shadcn/ui** - Beautiful, accessible components
- **Tailwind CSS** - Utility-first styling
- **React Query** - Server state management
- **bun** - Fast package manager

### Development
- **Hot Reloading** - Instant feedback loop
- **Type Safety** - Full TypeScript coverage
- **Code Quality** - ruff (Python) + prettier (TypeScript)
- **Background Processes** - nohup with comprehensive logging

## 🔐 Authentication

Supports both Databricks authentication methods:

1. **Personal Access Token (PAT)** - For development
2. **CLI Profile** - For production environments

The setup script guides you through configuration.

## 🚀 Deployment

Deploy to Databricks Apps:

```bash
./deploy.sh
```

This automatically:
- Builds the frontend
- Generates Python requirements
- Configures app.yaml
- Deploys via Databricks CLI

## 📝 Customization

1. **Update branding** in `client/src/pages/WelcomePage.tsx`
2. **Add new API endpoints** in `server/routers/`
3. **Create UI components** in `client/src/components/`
4. **Modify authentication** in `scripts/setup.sh`

## 🐛 Troubleshooting

- **Check logs**: `tail -f /tmp/databricks-app-watch.log`
- **View processes**: `ps aux | grep watch`
- **Kill processes**: `pkill -f watch.sh`
- **Reset environment**: Re-run `./setup.sh`

## 📚 Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Databricks Apps](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html)
- [shadcn/ui Components](https://ui.shadcn.com/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `./fix.sh` to format code
5. Submit a pull request

---

**Ready to build something amazing?** 🎉

Start with `./setup.sh` and let this template accelerate your Databricks app development!