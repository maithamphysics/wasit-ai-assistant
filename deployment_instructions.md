# Wasit AI Citizen Assistant - Deployment Instructions

## Overview
This document provides instructions for deploying the Wasit AI Citizen Assistant prototype application. The application is built using Streamlit and can be deployed either locally for testing or to a cloud platform for demonstration to the Wasit local government.

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for version control)
- OpenAI API key (optional, for enhanced AI capabilities)

## Local Deployment

### Step 1: Clone or Download the Repository
If using Git:
```bash
git clone [repository-url]
cd wasit_ai_app
```

Or simply download and extract the files to a folder named `wasit_ai_app`.

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables (Optional)
For enhanced AI capabilities using OpenAI:
1. Create a `.env` file in the root directory
2. Add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will start and be available at `http://localhost:8501` in your web browser.

## Cloud Deployment

### Streamlit Cloud Deployment
1. Create an account on [Streamlit Cloud](https://streamlit.io/cloud)
2. Connect your GitHub repository containing the application
3. Configure the deployment:
   - Set the main file path to `app.py`
   - Add any required secrets (like OPENAI_API_KEY)
4. Deploy the application

### Heroku Deployment
1. Create a `Procfile` with the following content:
```
web: streamlit run app.py
```

2. Create a `runtime.txt` file:
```
python-3.10.x
```

3. Deploy to Heroku:
```bash
heroku create wasit-ai-assistant
git push heroku main
```

## Configuration Options

### Language Support
The application includes a language toggle between English and Arabic. Full Arabic support would require:
1. Translating the knowledge base
2. Adding Arabic language detection
3. Implementing RTL (right-to-left) text support

### Customizing the Knowledge Base
To update the information in the knowledge base:
1. Edit the `knowledge_base.py` file
2. Add or modify entries in the `WASIT_KNOWLEDGE` dictionary
3. Restart the application to apply changes

### Adding New Service Categories
To add new service categories:
1. Update the `services` dictionary in `app.py`
2. Add corresponding information to the knowledge base
3. Update the chatbot response logic in `chatbot.py` if needed

## Security Considerations
For a production deployment:
1. Never expose API keys in client-side code
2. Implement proper authentication for administrative functions
3. Use HTTPS for all communications
4. Implement rate limiting to prevent abuse
5. Regularly update dependencies to patch security vulnerabilities

## Maintenance and Updates
Regular maintenance should include:
1. Updating the knowledge base with current information
2. Monitoring usage patterns to improve responses
3. Updating dependencies for security and performance improvements
4. Backing up application data and configurations

## Troubleshooting
Common issues and solutions:
- **Application won't start**: Check Python version and installed dependencies
- **API key errors**: Verify the OpenAI API key is correctly set in the environment variables
- **Slow responses**: Consider optimizing the knowledge base or upgrading the hosting plan
- **Memory errors**: Reduce the conversation history size or upgrade to a hosting plan with more memory

## Support
For technical support with this application, please contact:
- Email: [your-email@example.com]
- Phone: [your-phone-number]
