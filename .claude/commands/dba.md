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

Step 2: Product Requirements Gathering  

Step 3: Technical Architecture Planning

Step 4: Implementation Planning

**Bold the current step** and add a **⏺** dot next to the one we're on, and add a **✅** checkmark next to completed steps. Show the sub-steps (a, b, c) only for the current step, bold exactly which sub-step they are on, and add checkmarks next to completed sub-steps like this:

✅ Step 0: Previous Step (if any were completed)

⏺ **Step 1: GitHub Repository Setup**
   - ✅ a) GitHub Account Selection ← (checkmark if complete)
   - **b) Repository Name & Location** ← (bold if current sub-step)
   - *c) Local Project Location* ← (italics if not yet done)
   - *d) Create Repository & Initialize Project* ← (italics if not yet done)

*Step 2: Product Requirements Gathering*

*Step 3: Technical Architecture Planning*

*Step 4: Implementation Planning*

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

**d) Create Repository & Initialize Project**

Once you've confirmed the GitHub account, repository name, and local location, I'll:

1. Create the new GitHub repository using the selected account
2. Clone the repository to your specified local directory
3. Copy all template files from the current databricks-app-template to your new project
4. Initialize the project with your specific details
5. Commit and push the initial template to your new repository

*This ensures your new project starts with a clean copy of the template.*

---

## Step 2: Product Requirements Gathering

**a) Problem Definition**

**Question:**
What is the main problem this application will solve?

**If this question is unclear or you need help thinking through this aspect, please ask for clarification.**

*Please provide a detailed answer before I proceed to the next question.*

**b) Target Users**

**Question:**
Who will use this application? (Data scientists, engineers, business users, etc.)

*Please provide a detailed answer before I proceed to the next question.*

**c) Key Features**

**Question:**
What are the 3-5 most important features this app must have?

*Please provide a detailed answer before I proceed to the next question.*

**d) Success Metrics**

**Question:**
How will you know if this app is successful?

*Please provide a detailed answer before I proceed to the next question.*

**e) Priority Level**

**Question:**
Is this a prototype, MVP, or production-ready application?

*Please provide a detailed answer before I proceed to the next question.*

---

## Step 3: Technical Architecture Planning

**a) Data Sources**

**Question:**
What data will this app need to access? (Tables, APIs, files, etc.)

**If this technical aspect is unclear or you need help designing the architecture, please ask for clarification.**

*Please provide technical details before I proceed to the next question.*

**b) External Integrations**

**Question:**
What external systems will it integrate with?

*Please provide technical details before I proceed to the next question.*

**c) Scale Requirements**

**Question:**
How many users? How much data? Response time requirements?

*Please provide technical details before I proceed to the next question.*

**d) Deployment Requirements**

**Question:**
Any special deployment requirements or constraints?

*Please provide technical details before I proceed to the next question.*

**e) Authentication**

**Question:**
How should users authenticate? (SSO, tokens, etc.)

*Please provide technical details before I proceed to the next question.*

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
- **Source**: `./databricks-app-template/` (or current directory if you're in the template repo)
- **Template Repository**: `git@github.com:databricks-solutions/claude-databricks-app-template.git`
- **Todo System**: `~/universe/mlflow/web/js/src/experiment-tracking/components/experiment-page/components/traces-v3/trends/docs/todos.md`
- **Output Location**: `[specified-path]/{project-name}/`

**Template Setup:**
If `./databricks-app-template/` doesn't exist, I'll ask you to:
1. Request permissions for the databricks-app-template repository if needed
2. Once you have access, I'll clone `git@github.com:databricks-solutions/claude-databricks-app-template.git` to `./databricks-app-template/`

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