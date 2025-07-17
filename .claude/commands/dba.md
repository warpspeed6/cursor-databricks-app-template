---
description: "Create a new Databricks app using the databricks-app-template"
---

# Databricks App Creator

I'm helping you create a new Databricks application: **$ARGUMENTS**

**First, let me check if you're in the right place:**

[I'll check if the current directory is a git repository by running `git rev-parse --is-inside-work-tree` and `git remote get-url origin`]

**If you're in the `databricks-solutions/claude-databricks-app-template` repository:**
[I'll check if the current user is nsthorat by running `whoami`]

If you're **nsthorat**: You can test the `/dba` workflow directly in this template repository.

If you're **not nsthorat**: You're in the template repository! To create your own Databricks app:

1. **Go to GitHub**: https://github.com/databricks-solutions/claude-databricks-app-template
2. **Click "Use this template"** → "Create a new repository"
3. **Create your repository** with your desired name
4. **Clone your new repository** locally
5. **Navigate to your cloned repository** and run `/dba` again

**If you're in a Databricks app project created from the template:**
Perfect! You're already in a Databricks app project. I'll help you set up and customize your app.

**If you're not in a Databricks app repository:**
It looks like you're not in a Databricks app project. To get started:

1. **Go to the template**: https://github.com/databricks-solutions/claude-databricks-app-template
2. **Use the template** to create your own repository
3. **Clone your new repository** locally
4. **Navigate to your cloned repository** and run `/dba` again

---

**If you're in a template-based Databricks app project, let's get started:**

## ⚠️ IMPORTANT: Progress Display Instructions

**At each step, make sure you show all steps and the bolded line showing which step we're on**

Show this Progress Overview before each step:

Step 1: Databricks App Setup

Step 2: Product Requirements Document (PRD) Creation  

Step 3: Technical Architecture Planning

Step 4: Implementation Planning

**Bold the current step** and add a **⏺** dot next to the one we're on, and add a **✅** checkmark next to completed steps. Show the sub-steps (a, b, c) only for the current step, bold exactly which sub-step they are on, and add checkmarks next to completed sub-steps like this:

✅ Step 0: Previous Step (if any were completed)

⏺ **Step 1: Databricks App Setup**
   - ✅ a) Interactive Setup ← (checkmark if complete)
   - **b) Deploy & Test** ← (bold if current sub-step)

*Step 2: Product Requirements Document (PRD) Creation*
   - a) Initial Product Vision
   - b) Collaborative PRD Development
   - c) Final PRD Generation

*Step 3: Technical Architecture Planning*
   - a) Data Sources
   - b) External Integrations
   - c) Scale Requirements

*Step 4: Implementation Planning*

---

## Step 1: Databricks App Setup

**Now that you're in your Databricks app project, let me first set up the development environment:**

**a) Interactive Setup**

I'll run the interactive setup script to configure your app:

1. I'll use `osascript` to open a new terminal window in your project directory
2. Run `./setup.sh --auto-close` which will guide you through:
   - Databricks authentication (PAT or profile)
   - Environment variable configuration
   - Python and frontend dependency installation
   - Claude MCP Playwright setup
3. When setup completes, the terminal will close automatically
4. I'll confirm the setup was successful

**Command I'll execute:**
```bash
osascript -e "tell application \"Terminal\" to do script \"cd '$(pwd)' && ./setup.sh --auto-close\"" -e 'tell application "Terminal" to activate'
```

**Note:** The setup script requires interactive input, so it must run in a separate terminal window that you can interact with.

*I'll wait for the setup to complete before proceeding to the next step.*

**b) App Creation & Deploy**

After the setup completes, I'll check if your Databricks app exists and create it if needed:

1. **Check for existing app:**
   - I'll read the app name from `.env.local` (DATABRICKS_APP_NAME)
   - Run `databricks apps list | grep DATABRICKS_APP_NAME` to check if it exists
   - **I'll use `./app_status.sh` to get comprehensive app status and display it nicely**
   - **I'll always display:**
     - **App Name:** [app name from .env.local]
     - **App URL:** [app url from app_status.sh]

2. **Create app if needed:**
   - If the app doesn't exist, I'll ask if you want me to create it
   - If yes, I'll use `./deploy.sh --create` which will:
     - Create the app automatically (this can take several minutes)
     - Then deploy the template to the newly created app
   - **I'll use `./app_status.sh` to verify creation and show status**
   - **I'll always display:**
     - **App Name:** [app name from .env.local]
     - **App URL:** [app url from app_status.sh]

3. **Test the app locally before deployment:**
   - **I'll first test the app locally to catch any issues before deploying**
   - **I'll run `./run_app_local.sh` in background and log to `/tmp/local-app-test.log`**
   - **I'll read the log file to verify the app builds and starts successfully**
   - **If local testing fails, I'll debug the issues before proceeding to deployment**
   - **I'll always display:**
     - **App Name:** [app name from .env.local]
     - **Local test status:** [success/failure with details]

4. **Deploy the template app:**
   - **IMPORTANT: I will ONLY use `./deploy.sh` to deploy - no other deployment method**
   - **I'll only proceed with deployment if the local test was successful**
   - If the app already exists, I'll run `./deploy.sh` from your project directory to deploy the base template to Databricks Apps
   - If the app was just created in step 2, this step is already complete from the `./deploy.sh --create` command
   - This will:
     - Build the frontend application
     - Generate Python requirements
     - Deploy to your Databricks workspace
   - I'll verify the deployment was successful
   - **I'll use `./app_status.sh` to check deployment status and confirm the app is running**
   - **I'll tell you "Deployment successful!" only when `./app_status.sh` shows the app status as RUNNING**
   - **If the app status shows deployment failed or is not running, I'll use `./app_status.sh --verbose` to check if the right files are in the workspace**
   - **For further debugging, I can use `./run_app_local.sh` to run the app locally with debug mode**
   - **If CLI commands are missing (like `run-local`), I'll suggest updating the Databricks CLI with: `pip install --upgrade databricks-cli`**
   - **I'll always display:**
     - **App Name:** [app name from .env.local]
     - **App URL:** [app url from app_status.sh]
   - **Please verify that you can see the template UI at the provided URL**

**This ensures your Databricks app exists, works locally, and deploys successfully before we add custom features.**

*I'll wait for the app creation, local testing, and deployment to complete and show you the app URL for verification.*

---

## Step 2: Product Requirements Document (PRD) Creation

**I'll work with you to create a comprehensive Product Requirements Document (PRD) through iterative collaboration. This will be saved to `docs/product.md` after we refine your vision together.**

**a) Initial Product Vision**

**Question:**
Describe your app idea in your own words. What do you want to build?

**I'll help you by:**
- Asking clarifying questions to understand your vision
- Suggesting improvements and additional features you might not have considered
- Helping you identify potential user pain points
- Providing examples of similar successful applications
- Offering technical possibilities within the Databricks ecosystem

*Please describe your app idea, and I'll ask follow-up questions to help develop it further.*

**b) Collaborative PRD Development**

Based on your description, I'll engage in iterative dialogue to refine your product vision:

1. **Ask targeted questions** to clarify ambiguous aspects
2. **Suggest enhancements** based on Databricks capabilities and best practices
3. **Help you prioritize** features by impact and feasibility
4. **Identify edge cases** and potential challenges
5. **Refine the vision** through natural language conversation

You can refine any aspect by saying things like:
- "Actually, change the target users to..."
- "Add a feature that allows..."
- "Remove the part about..."
- "Make it more focused on..."

**c) Final PRD Generation**

Once we've refined your vision together, I'll create a structured PRD in `docs/product.md` containing:
- **Executive Summary** - Clear problem statement and solution
- **Target Users** - Detailed user personas and use cases
- **Feature Specifications** - Core and nice-to-have features
- **Success Metrics** - How you'll measure success
- **Technical Considerations** - Databricks-specific opportunities
- **Implementation Priority** - Recommended development phases

**Note:** This is a collaborative planning process. I will NOT start implementing features yet - we're building a solid foundation for development.

---

## Step 3: Technical Architecture Planning

**I'll engage in "ultrathinking" with you to design both the high-level architecture and detailed implementation plan. This will be saved to `docs/design.md` after our collaborative design session.**

**a) High-Level Architecture Design**

Based on your product requirements from Step 2, I'll work with you to design:

**Technology Stack & Libraries:**
- Backend framework choices (FastAPI features to use)
- Frontend libraries (React components, state management)
- Database/storage solutions
- Authentication and authorization
- API design patterns
- UI/UX frameworks (shadcn/ui components)

**Questions I'll ask:**
- What data sources will this app need to access? (Tables, APIs, files, etc.)
- What external systems will it integrate with?
- How many users? How much data? Response time requirements?
- What Databricks-specific features should we leverage?

**b) Ultrathinking Collaborative Design**

I'll engage in deep technical thinking with you to refine:

1. **Architecture decisions** - Why specific libraries and patterns
2. **Data flow design** - How data moves through the system
3. **Component structure** - Frontend and backend organization
4. **Integration patterns** - How to connect with external systems
5. **Performance considerations** - Optimization strategies
6. **Security architecture** - Authentication, authorization, data protection

You can refine any aspect by saying:
- "Let's use a different approach for..."
- "Add caching layer for..."
- "Change the database design to..."
- "Simplify the authentication to..."

**c) Implementation Plan Creation**

Once we've designed the architecture, I'll create a detailed implementation plan with:

**Phase-by-phase breakdown:**
- Phase 1: Core features and basic functionality
- Phase 2: Advanced features and integrations
- Phase 3: Optimization and polish

**Development workflow:**
- Specific files to create/modify
- Order of implementation
- Testing strategies
- Deployment considerations

**Final deliverable:** `docs/design.md` containing both high-level architecture and step-by-step implementation plan.

**d) Implementation Decision**

After completing the design, I'll ask: **"Are you ready to implement this design now?"**

- **If yes:** I'll begin implementing according to the plan
- **If no:** I'll provide guidance on how to implement parts of the design later by referencing `docs/product.md` and `docs/design.md`

**Note:** This is where we transition from planning to potential implementation.

---

## Step 4: Implementation Planning

**a) Project Creation**

**I will:**
1. Copy template files from `./databricks-app-template/` to your project directory
2. Set up the project planning documentation system in `docs/` directory:
   - `project-description.md` - Overall project overview and context
   - `project-spec.md` - Detailed technical specifications from your answers
   - `todos.md` - Customized todo list based on MLflow trends template
   - `workflow-core.md` - Development workflow and phases
   - `workflow-troubleshooting.md` - Common issues and solutions
   - `project-reference.md` - Technical reference and patterns
3. Create initial work tracking structure with `docs/work/` directory
4. Set up `docs/done/` directory for completed task documentation
5. Open all the planning documentation files in VS Code so you can review the project plan
6. Commit and push all files to your GitHub repository

**Then I'll move to Phase 2: Testing the First Version**

**b) Final Confirmation**

**Question:**
Are you ready for me to create the project based on all your previous answers?

**If you need clarification on what I'll create or want to modify any aspect of the implementation plan, please ask now.**

*Type "proceed" when you're ready for me to create the project.*

---

## Phase 2: Testing the First Version

**After project setup, I'll verify the template works by testing the basic functionality:**

**Step 2.1: Interactive Setup**
1. Ask you to run `./setup.sh` script outside of Claude (it requires interactive input)
2. You'll need to tell me when the setup is complete
3. I'll check for any setup errors or issues

**Step 2.2: Development Server Testing**
1. Read the CLAUDE.md from your new project to understand the development workflow
2. Start the development server using `./watch.sh` in the background
3. Monitor server startup and ensure it's running correctly

**Step 2.3: Playwright Automation Testing**
1. Check if you have Playwright MCP available for UI automation
2. If not available, I'll provide the command to add it: `npx @anthropic-ai/mcp-playwright install`
3. Use Playwright to automate basic UI testing of the running application
4. Verify the template's core functionality works as expected

**Step 2.4: Testing Summary**
1. Report on what's working and any issues found
2. Provide next steps for development
3. Confirm the project is ready for active development

*This comprehensive testing ensures your new Databricks app is properly set up and functional before you begin development.*

---

## Phase 3: Development Iteration

**After testing confirms the basic template works, I'll iterate on the application until it matches your product specification:**

**Step 3.1: Implementation Loop**
- Review the product specification from your earlier answers
- Identify gaps between current template and desired functionality
- Implement features iteratively using the development workflow
- Test each change using Playwright automation
- Check logs and UI to ensure everything works as expected

**Step 3.2: Continuous Validation**
- Run the application after each change
- Verify UI matches the product requirements
- Check server logs for any errors or issues
- Ensure all specified features are working properly

**Step 3.3: Refinement**
- Polish the UI to match your specifications
- Fix any bugs or issues discovered during testing
- Optimize performance and user experience
- Continue until the application fully meets your requirements

*I'll continue this iteration process until the UI and logs show the application works exactly as specified in your product requirements.*

---

## Phase 4: Deployment

**Once the application is working according to your specifications, I'll deploy it:**

**Step 4.1: Databricks App Setup**
- Review the `setup.sh` script to find the required Databricks app creation links
- Ask you to create a new Databricks app in your workspace (I'll provide the specific links from setup.sh)
- Wait for confirmation that the Databricks app is created and you have the app details

**Step 4.2: Deployment Process**
- Review the `deploy.sh` script to understand the deployment process
- Execute the deployment using the deploy script
- Monitor the deployment process for any issues
- Verify the application is successfully deployed to Databricks

**Step 4.3: Deployment Verification**
- Test the deployed application in the Databricks environment
- Confirm all functionality works in the production environment
- Provide you with the deployment details and access information

*This completes the full end-to-end process: from specification to working deployed application.*

---

## Template Information:
- **Template Repository**: `databricks-solutions/claude-databricks-app-template`
- **Template URL**: `https://github.com/databricks-solutions/claude-databricks-app-template`
- **Creation Method**: GitHub template repository (not manual file copying)
- **Output Location**: `[current-directory]/`

**Template Creation:**
This command uses GitHub's template functionality to create new repositories:
1. Creates a new repository from the template using GitHub's "Use this template" button
2. Automatically includes all template files, structure, and configuration
3. Provides a clean starting point without Git history from the template
4. No manual file copying or setup required

**Documentation System:**
The project will be set up with a comprehensive planning and tracking system based on the MLflow trends todo workflow:
- Structured documentation in `docs/` directory
- Todo system for task management
- Work tracking with `docs/work/` and `docs/done/` directories
- Development workflow documentation
- Technical reference and troubleshooting guides

**Project Resume Detection:**
The command will check the current directory for existing projects that might match your description:
- Search for similar directory names
- Check for projects with related keywords
- Look for existing `docs/project-description.md` files to match content
- Offer to continue existing projects or create new ones

**Let's start with Step 1!**