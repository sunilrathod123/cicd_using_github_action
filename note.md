1. generatea access token from github and then linked git in databricks


Step 1: Create the GitHub repository secrets
Open your repository:
GitHub → Settings → Secrets and variables → ActionsClick New repository secret and create these four secrets.


Step 1: Create a production environment
Open your repository's environment settings:
Open GitHub Environments settings1. Click New environment.
2. Enter the name production.
3. Click Configure environment.
Step 2: Add the approver
On the production environment configuration page:



1. Find Deployment protection rules.
2. Select Required reviewers.
3. Search for the GitHub username of your manager or approver.
4. Add that person as a reviewer.
5. Enable Prevent self-review if you want someone other than the person who triggered deployment to approve it.
6. Click Save protection rules.