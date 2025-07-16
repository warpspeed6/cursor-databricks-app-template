---
description: "Create a new Databricks app using the databricks-app-template"
---

# Databricks App Creator

I'm helping you create a new Databricks application: **$ARGUMENTS**

**First, let me check if you're in an existing Databricks app project:**

[I'll check if the current directory is a git repository by running `git rev-parse --is-inside-work-tree` and `git remote get-url origin`]

**If you're in a git repository:**
- If it's the `databricks-solutions/claude-databricks-app-template` repository → I'll help you create a new project from here (using the current directory as the template source)
- If it's any other git repository → I'll check if it looks like a Databricks app project (has `server/app.py`, `client/`, `CLAUDE.md`, etc.)
  - If it's a Databricks app project: "It looks like you're already in a Databricks app project. Do you want to continue working on this existing project or create a new one?"
  - If it's not a Databricks app project: "You're in a git repository that doesn't appear to be a Databricks app. I'll help you create a new Databricks app project."

**If you're not in a git repository:**
- I'll ask you where you want to create the new Databricks app project

---

**Based on the analysis above, I'll either:**
1. **Continue with existing project** - Skip to Step 4 (Product Requirements) if you choose to continue
2. **Create new project** - Proceed with Step 1 below if you want to create a new project

---

**If creating a new project, let me break this down into clear steps:**

## ⚠️ IMPORTANT: Progress Display Instructions

**At each step, make sure you show all steps and the bolded line showing which step we're on**

Show this Progress Overview before each step:

Step 1: GitHub Repository Setup

Step 2: Databricks App Setup

Step 3: Product Requirements Gathering  

Step 4: Technical Architecture Planning

Step 5: Implementation Planning

**Bold the current step** and add a **⏺** dot next to the one we're on, and add a **✅** checkmark next to completed steps. Show the sub-steps (a, b, c) only for the current step, bold exactly which sub-step they are on, and add checkmarks next to completed sub-steps like this:

✅ Step 0: Previous Step (if any were completed)

⏺ **Step 1: GitHub Repository Setup**
   - ✅ a) GitHub Account Selection ← (checkmark if complete)
   - **b) Repository Name & Location** ← (bold if current sub-step)
   - *c) Local Project Location* ← (italics if not yet done)
   - *d) Create Repository from Template* ← (italics if not yet done)
   - *e) Success & Next Steps* ← (italics if not yet done)

*Step 2: Databricks App Setup*
   - a) Interactive Setup
   - b) Deploy & Test

*Step 3: Product Requirements Gathering*
   - a) Problem Definition
   - b) Target Users  
   - c) Key Features

*Step 4: Technical Architecture Planning*
   - a) Data Sources
   - b) External Integrations
   - c) Scale Requirements

*Step 5: Implementation Planning*

---

## Step 1: GitHub Repository Setup

**a) GitHub Account Selection**

[I'll run this command to detect all GitHub accounts: `grep -E "^Host github" ~/.ssh/config | awk '{print $2}' | while read host; do echo "git@$host" | xargs -I {} ssh -T {} 2>&1 | grep -o "Hi [^!]*" | sed "s/Hi //" | paste -d" -> git@" - <(echo "$host"); done | nl`]

Available GitHub accounts:
[The actual accounts will be displayed here based on your SSH configuration]

**Question:**
Which GitHub account would you like to use? (Enter the number from the list above)

*Please answer this question before I proceed with the next step.*

**b) Repository Name & Location**

[I'll create a sanitized project name from "$ARGUMENTS" by converting to lowercase, replacing spaces with hyphens, and removing special characters]

**Your repository will be created at:**
`github.com/[selected-username]/[sanitized-name-from-arguments]`

**Question:**
Does this repository name and location work for you? If not, explain what I need to fix.

[If you don't accept, I'll take your English feedback, generate a new name, and ask again until you accept]

*Please answer this question before I proceed with the next step.*

**c) Local Project Location**

**Question:**
Where would you like to create the new project? (Provide the full path, e.g., `/Users/yourname/Code/` or `~/projects/`)

*Please answer this question before I proceed with the next step.*

**d) Create Repository from Template**

Once you've confirmed the GitHub account, repository name, and local location, I'll:

1. Create a new **private** GitHub repository using the `databricks-solutions/claude-databricks-app-template` template
2. Use the `gh` command to create the repository with your selected account: `gh repo create [username]/[repo-name] --template databricks-solutions/claude-databricks-app-template --private`
3. Clone the new repository to your specified local directory
4. The repository will automatically include all template files and structure
5. You're ready to start customizing your Databricks app!

**Note:** The repository will be created as **private** by default. You can make it public later by going to the repository settings on GitHub, or ask me to do it for you after creation.

*This uses GitHub's template functionality to create a clean, up-to-date copy of the template.*

**e) Success & Next Steps**

After successfully creating your repository and cloning it locally, I'll show you:

🎉 **Repository Created Successfully!**
- **GitHub Repository**: `https://github.com/[selected-username]/[repo-name]`
- **Local Directory**: `[specified-path]/[repo-name]/`

**What's Next?**
You can either:
1. **Continue here** - I'll proceed with the product requirements gathering to customize your new app
2. **Go to your new project** - Navigate to `[specified-path]/[repo-name]/` and run `/dba` again in that context

*The choice is yours! Both paths will lead to the same comprehensive setup process.*

---

## Step 2: Databricks App Setup

**a) Interactive Setup**

Now that your repository is created, I'll run the interactive setup script to configure your Databricks app:

1. I'll use `osascript` to open a new terminal window in your project directory
2. Run `cd [specified-path]/[repo-name] && ./setup.sh --auto-close` which will guide you through:
   - Databricks authentication (PAT or profile)
   - Environment variable configuration
   - Python and frontend dependency installation
   - Claude MCP Playwright setup
3. When setup completes, the terminal will close automatically
4. I'll confirm the setup was successful

**Command I'll execute:**
```bash
osascript -e 'tell application "Terminal" to do script "cd [specified-path]/[repo-name] && ./setup.sh --auto-close"' -e 'tell application "Terminal" to activate'
```

**Note:** The setup script requires interactive input, so it must run in a separate terminal window that you can interact with.

*I'll wait for the setup to complete before proceeding to the next step.*

**b) Deploy & Test**

After the setup completes, I'll deploy the template app to make sure everything works:

1. I'll run `./deploy.sh` from your project directory to deploy the base template to Databricks Apps
2. This will:
   - Build the frontend application
   - Generate Python requirements
   - Deploy to your Databricks workspace
   - Provide you with the app URL
3. I'll verify the deployment was successful
4. You can test the basic template functionality before we customize it

**This ensures your development environment and deployment pipeline are working correctly before we add custom features.**

*I'll wait for the deployment to complete and show you the app URL.*

---

## Step 3: Product Requirements Gathering

**a) Problem Definition**

**Question:**
What is the main problem this application will solve? (Type "skip" to skip this question)

**If this question is unclear or you need help thinking through this aspect, please ask for clarification.**

*Please provide a detailed answer or type "skip" before I proceed to the next question.*

**b) Target Users**

**Question:**
Who will use this application? (Data scientists, engineers, business users, etc.) (Type "skip" to skip this question)

*Please provide a detailed answer or type "skip" before I proceed to the next question.*

**c) Key Features**

**Question:**
What are the 3-5 most important features this app must have? (Type "skip" to skip this question)

*Please provide a detailed answer or type "skip" before I proceed to the next question.*

---

## Step 3: Technical Architecture Planning

**a) Data Sources**

**Question:**
What data will this app need to access? (Tables, APIs, files, etc.) (Type "skip" to skip this question)

**If this technical aspect is unclear or you need help designing the architecture, please ask for clarification.**

*Please provide technical details or type "skip" before I proceed to the next question.*

**b) External Integrations**

**Question:**
What external systems will it integrate with? (Type "skip" to skip this question)

*Please provide technical details or type "skip" before I proceed to the next question.*

**c) Scale Requirements**

**Question:**
How many users? How much data? Response time requirements? (Type "skip" to skip this question)

*Please provide technical details or type "skip" before I proceed to the next question.*

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
- **Output Location**: `[specified-path]/{project-name}/`

**Template Creation:**
This command uses GitHub's template functionality to create new repositories:
1. Creates a new repository from the template using `gh repo create --template`
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