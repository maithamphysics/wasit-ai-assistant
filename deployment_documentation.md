# Wasit AI Citizen Assistant - Deployment Documentation

This comprehensive guide provides all the information needed to deploy and maintain the Wasit AI Citizen Assistant as a permanent website.

## Table of Contents
1. [Overview](#overview)
2. [GitHub Repository Setup](#github-repository-setup)
3. [Streamlit Cloud Deployment](#streamlit-cloud-deployment)
4. [Configuration Settings](#configuration-settings)
5. [Testing Procedures](#testing-procedures)
6. [Maintenance and Updates](#maintenance-and-updates)
7. [Troubleshooting](#troubleshooting)
8. [Additional Resources](#additional-resources)

## Overview

The Wasit AI Citizen Assistant is a web application built with Streamlit that provides an AI-powered interface for citizens to access information about government services in Wasit Governorate. This documentation covers the complete process of deploying the application as a permanent website using GitHub and Streamlit Cloud.

## GitHub Repository Setup

### Creating a Repository

1. Go to https://github.com/new
2. Set repository name: `wasit-ai-assistant`
3. Add description: "AI Citizen Assistant for Wasit Local Government"
4. Choose visibility: Public (or Private if preferred)
5. Check "Add a README file"
6. Click "Create repository"

### Uploading Application Files

**Option 1: Using Git Commands**
1. Open VS Code on your MacBook
2. Open Terminal (Terminal > New Terminal)
3. Navigate to desired location: `cd Documents` or another folder
4. Clone the repository:
   ```bash
   git clone https://github.com/maithamphysics/wasit-ai-assistant.git
   cd wasit-ai-assistant
   ```
5. Copy all application files to this folder
6. Add, commit, and push:
   ```bash
   git add .
   git commit -m "Initial commit of Wasit AI Assistant"
   git push origin main
   ```

**Option 2: Using GitHub Web Interface**
1. Go to your repository on GitHub
2. Click "Add file" > "Upload files"
3. Drag and drop all application files
4. Maintain the folder structure, especially the .streamlit folder
5. Click "Commit changes"

### Required Files

Ensure your repository includes these files:
- `app.py` - Main application file
- `chatbot.py` - Chatbot logic
- `knowledge_base.py` - Information about Wasit services
- `requirements.txt` - Dependencies
- `.streamlit/config.toml` - Theme customization
- `.gitignore` - Git configuration

## Streamlit Cloud Deployment

### Deploying the Application

1. Go to https://streamlit.io/cloud
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository (maithamphysics/wasit-ai-assistant)
5. Set main file path to: `app.py`
6. Click "Deploy!"

### Adding OpenAI API Key (Optional)

To enable enhanced AI capabilities:
1. In your deployed app settings, find "Secrets"
2. Add the following:
   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```
3. Click "Save"
4. Reboot your app

### Customizing Your App URL

1. In app settings, find "General"
2. Look for "Custom subdomain"
3. Enter preferred subdomain (e.g., "wasit-assistant")
4. Your app will be available at: https://wasit-assistant.streamlit.app

## Configuration Settings

### Theme Customization

The application uses a custom theme defined in `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#1E5631"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Advanced Configuration Options

For more advanced configuration:
1. Custom domain setup
2. Resource allocation
3. Authentication (if needed)
4. Analytics integration

See `streamlit_cloud_configuration_guide.md` for detailed instructions.

## Testing Procedures

### Basic Functionality Testing

Test the following core features:
- Interface loading and appearance
- Chat functionality
- Service category selection
- Quick links

### Content Testing

Test specific questions for each service category:
- Citizen services (birth certificates, ID cards, etc.)
- Business services (registration, licenses, etc.)
- Infrastructure (roads, water, electricity, etc.)
- Agriculture (subsidies, permits, etc.)

### Cross-Device Testing

- Test on desktop browsers (Chrome, Firefox, Safari)
- Test on mobile devices (iOS and Android)
- Verify responsive design works correctly

See `testing_guide.md` for a comprehensive testing checklist.

## Maintenance and Updates

### Updating the Application

1. Make changes to files in your local repository
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```
3. Streamlit Cloud will automatically detect changes and rebuild

### Monitoring Usage

1. Go to your app dashboard in Streamlit Cloud
2. Click on "Analytics" tab
3. Review metrics like visitor count and session duration

## Troubleshooting

### Common Issues and Solutions

1. **App shows "Please wait..." indefinitely**
   - Check app logs in Streamlit Cloud settings
   - Verify all required packages are in requirements.txt

2. **Enhanced AI features not working**
   - Verify OpenAI API key is correct
   - Check for error messages in app logs

3. **Changes not appearing after update**
   - Force refresh browser (Ctrl+F5 or Cmd+Shift+R)
   - Reboot app from Streamlit Cloud settings

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [GitHub Documentation](https://docs.github.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

---

This documentation provides a complete reference for deploying and maintaining the Wasit AI Citizen Assistant. For any additional questions or support, please contact the development team.
