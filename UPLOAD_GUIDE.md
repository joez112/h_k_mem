# How to Upload to GitHub

## Step 1: Login to GitHub
1. Go to https://github.com
2. Login with:
   - Username: joez112
   - Password: zz111111Z
   - Email: 27816@qq.com

## Step 2: Create Repository
1. Click "+" → "New repository"
2. Name: h_k_mem
3. Description: Hierarchical Knowledge Memory - Break Hermes Agent 2,200 character limit
4. Public repository
5. Add README: YES
6. Add .gitignore: Python
7. License: MIT
8. Click "Create repository"

## Step 3: Upload Files
### Method A: Web Upload
1. Go to your new repository
2. Click "Add file" → "Upload files"
3. Drag ALL files from this folder
4. Click "Commit changes"

### Method B: Git Commands
```bash
# Clone repository
git clone https://github.com/joez112/h_k_mem.git
cd h_k_mem

# Copy all files
cp -r /Users/mac/hermes-agent-independent/skills/h_k_mem_package/* .

# Configure git
git config user.name "joez112"
git config user.email "27816@qq.com"

# Add and commit
git add .
git commit -m "feat: Add h_k_mem skill v1.0.0"

# Push to GitHub
git push origin main
```

## Step 4: Final Setup
1. Go to repository Settings
2. Add topics: hermes-agent, memory-management, knowledge-base
3. Update description if needed

## Your Repository URL
https://github.com/joez112/h_k_mem

## Files to Upload
- SKILL.md
- README.md
- LICENSE
- package.json
- templates/ (folder with 6 files)
- scripts/ (folder with init script)

## Done! 🎉
Your skill is now available on GitHub for all Hermes Agent users!