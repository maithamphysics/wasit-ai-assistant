# Streamlit Cloud Deployment - Configuration Guide

This guide provides detailed instructions for configuring your Streamlit Cloud deployment after you've deployed the Wasit AI Citizen Assistant.

## Adding Secrets for OpenAI API

To enable the enhanced AI capabilities, you need to add your OpenAI API key to Streamlit Cloud:

1. Go to your Streamlit Cloud dashboard: https://share.streamlit.io/
2. Find your deployed app (wasit-ai-assistant)
3. Click on the three dots (⋮) next to your app
4. Select "Settings"
5. Scroll down to the "Secrets" section
6. Click "Edit Secrets"
7. Add the following in the editor:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key-here"
   ```
8. Click "Save"
9. Restart your app by clicking "Reboot app" in the app settings

## Verifying the Deployment

After deployment, you should verify that everything is working correctly:

1. Visit your app's URL (e.g., https://wasit-ai-assistant.streamlit.app)
2. Test the basic functionality:
   - Try asking a simple question like "What are the government working hours?"
   - Test the service category selection in the sidebar
   - Click on the quick links at the bottom
3. If you added an OpenAI API key, test the enhanced AI capabilities:
   - Ask "How can AI help Wasit?" to trigger the LangChain integration

## Customizing Your App URL

To make your app more professional and easier to share:

1. Go to your app settings
2. Find the "General" section
3. Look for "Custom subdomain"
4. Enter your preferred subdomain (e.g., "wasit-assistant")
5. Click "Save"
6. Your app will now be available at: https://wasit-assistant.streamlit.app

## Setting Up a Custom Domain (Advanced)

For a fully professional appearance, you can use your own domain:

1. Purchase a domain (if you don't already have one)
2. In your Streamlit Cloud app settings, find "Custom domain"
3. Enter your domain (e.g., assistant.wasit.gov.iq)
4. Follow the DNS configuration instructions provided
5. Verify ownership and wait for DNS propagation (can take 24-48 hours)

## Monitoring Usage and Analytics

To track how your app is being used:

1. Go to your app dashboard
2. Click on the "Analytics" tab
3. View metrics like:
   - Number of visitors
   - Session duration
   - Most active times
   - Error rates

## Updating Your Application

When you need to make changes to your application:

1. Update the files in your GitHub repository
2. Streamlit Cloud will automatically detect changes and rebuild your app
3. For major changes, you may want to manually reboot the app from settings

## Troubleshooting Common Issues

If you encounter problems with your deployment:

1. **App shows "Please wait..." indefinitely**
   - Check the app logs in Streamlit Cloud settings
   - Verify that all required packages are in requirements.txt
   - Ensure your secrets are configured correctly

2. **Enhanced AI features not working**
   - Verify your OpenAI API key is correct
   - Check that the key has sufficient credits
   - Look for error messages in the app logs

3. **App is slow to load**
   - This is normal for the first load after inactivity
   - Subsequent loads should be faster
   - Consider upgrading to a paid plan for better performance

4. **Changes not appearing after update**
   - Force refresh your browser (Ctrl+F5 or Cmd+Shift+R)
   - Reboot the app from Streamlit Cloud settings

## Resource Management

The free tier of Streamlit Cloud has some limitations:

- Apps go to sleep after inactivity
- Limited computing resources
- Public repositories only (unless on Team/Enterprise plan)

If you need more resources, consider upgrading to a paid plan or exploring other hosting options like Heroku or AWS.
