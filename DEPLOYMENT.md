# GitHub Pages Deployment Guide

This Pelican blog is configured to deploy automatically to GitHub Pages using GitHub Actions.

## Setup Instructions

### 1. Enable GitHub Pages
1. Go to your repository settings on GitHub
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select "Deploy from a branch"
4. Choose the `gh-pages` branch and `/ (root)` folder
5. Click "Save"

### 2. Configure Repository Settings
1. In repository settings, go to "Actions" → "General"
2. Under "Workflow permissions", select "Read and write permissions"
3. Check "Allow GitHub Actions to create and approve pull requests"
4. Click "Save"

### 3. Push Your Changes
The GitHub Actions workflow will automatically:
- Build your Pelican site when you push to the `main` branch
- Deploy the built site to the `gh-pages` branch
- Make your site available at `https://vaurenw.github.io`

## Manual Deployment

If you need to deploy manually:

```bash
# Build the site
make publish

# The output will be in the `output/` directory
# You can then manually push this to the gh-pages branch
```

## Configuration

- **Site URL**: Set to `https://vaurenw.github.io` in `publishconf.py`
- **Build Output**: Generated in `output/` directory
- **GitHub Actions**: Configured in `.github/workflows/deploy.yml`

## Troubleshooting

- If the site doesn't appear, check the GitHub Actions tab for build errors
- Ensure the `gh-pages` branch is created and contains the built site
- Verify that GitHub Pages is enabled and pointing to the correct branch 