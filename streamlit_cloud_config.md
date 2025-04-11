# Streamlit Cloud Deployment Configuration

This file contains instructions for configuring your Streamlit Cloud deployment.

## Secrets Management

To enable the enhanced AI capabilities using OpenAI, you'll need to add your API key to Streamlit Cloud secrets.

1. After connecting your GitHub repository to Streamlit Cloud, go to the app settings
2. Find the "Secrets" section
3. Add the following configuration:

```toml
# .streamlit/secrets.toml
OPENAI_API_KEY = "your-openai-api-key-here"
```

## Advanced Configuration

### Custom Domain (Optional)
If you want to use a custom domain instead of the default streamlit.app domain:

1. Go to app settings
2. Find the "Custom domain" section
3. Follow the instructions to configure your domain

### Resource Allocation
The free tier of Streamlit Cloud should be sufficient for demonstration purposes. If you need more resources:

1. Go to app settings
2. Find the "Resources" section
3. Adjust the memory and CPU allocation as needed (may require a paid plan)

### Theme Customization
To customize the appearance of your Streamlit app:

1. Create a `.streamlit` folder in your repository
2. Add a `config.toml` file with the following content:

```toml
[theme]
primaryColor = "#1E5631"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

## Monitoring and Analytics

Streamlit Cloud provides basic app analytics. To access them:

1. Go to your app dashboard
2. Click on the "Analytics" tab
3. View metrics like visitor count, session duration, etc.

For more advanced analytics, consider integrating a third-party service like Google Analytics.
