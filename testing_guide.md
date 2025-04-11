# Wasit AI Citizen Assistant - Testing Guide

This guide provides a structured approach to testing your deployed Wasit AI Citizen Assistant to ensure it's functioning correctly before presenting it to the Wasit local government.

## Basic Functionality Testing

### 1. Interface Loading
- Verify the application loads completely
- Check that all UI elements are visible and properly styled
- Confirm the Iraq flag image loads in the sidebar
- Verify the main header and introduction text are displayed

### 2. Chat Functionality
- Type a simple greeting (e.g., "Hello") and verify you get a response
- Check that user messages appear in green bubbles on the right
- Check that AI responses appear in white bubbles with green border on the left
- Verify that long responses display properly without text overflow issues

### 3. Service Categories
- Click through each service category in the sidebar dropdown
- Verify that selecting a category updates the services dropdown
- Select a service and click "Ask about this service"
- Verify that the question appears in the chat and receives an appropriate response

### 4. Quick Links
- Test each quick link button at the bottom of the page
- Verify that clicking each button adds the appropriate question to the chat
- Confirm that each question receives a relevant response

### 5. Language Toggle
- Switch between English and Arabic in the sidebar
- Note: Full Arabic support will be implemented in a future update

## Content Testing

### 1. Citizen Services
Test questions about each citizen service:
- "What documents do I need for a birth certificate?"
- "How do I get a marriage certificate?"
- "What's the process for getting a death certificate?"
- "How can I renew my ID card?"
- "What's required for a passport application?"
- "How do I get a residence permit?"

### 2. Business Services
Test questions about business-related services:
- "How do I register a business in Wasit?"
- "What's needed for a trade license?"
- "How do I get a construction permit?"
- "When do I need to file business taxes?"
- "What's the process for an import/export license?"

### 3. Infrastructure
Test questions about infrastructure services:
- "How do I report a road that needs repair?"
- "What should I do if I have no water?"
- "Who do I contact about electricity problems?"
- "When is garbage collected in Wasit?"
- "How do I report a street light that's not working?"

### 4. Agriculture
Test questions about agricultural services:
- "What farming subsidies are available?"
- "How do I get an agricultural permit?"
- "How do I establish water rights for my farm?"
- "How do I report crop diseases?"
- "How can I sell my agricultural products?"

### 5. General Information
Test general questions about government services:
- "What are the government working hours?"
- "Where are government offices located?"
- "How much do government services cost?"
- "What documents do I need for government services?"

## Enhanced AI Testing (if OpenAI API key is configured)

Test the enhanced AI capabilities with more complex questions:
- "How can AI help improve governance in Wasit?"
- "What are the benefits of digital transformation for local government?"
- "How can technology improve agricultural productivity in Wasit?"

## Cross-Device Testing

### Desktop Testing
- Test on different browsers (Chrome, Firefox, Safari)
- Test at different screen resolutions
- Verify responsive layout adjusts appropriately

### Mobile Testing
- Test on a smartphone (iOS and Android if possible)
- Verify all elements are accessible on small screens
- Test chat functionality and service selection on mobile
- Verify text is readable without zooming

## Performance Testing

- Measure initial load time
- Test response time for simple queries
- Test response time for complex queries (with enhanced AI)
- Verify the application remains responsive after multiple interactions

## Error Handling

Test how the application handles:
- Empty messages (should not allow sending)
- Very long messages
- Special characters and non-Latin scripts
- Refreshing the page (chat history should persist)

## Security Testing

- Verify that the OpenAI API key is not exposed in the frontend
- Check that user inputs are properly sanitized
- Ensure no sensitive information is logged or stored inappropriately

## Documentation of Test Results

Create a simple spreadsheet or document to track:
- Test cases performed
- Pass/fail status
- Any issues discovered
- Screenshots of problems
- Notes for improvement

## Reporting Issues

If you encounter any issues during testing:
1. Take a screenshot of the problem
2. Note the exact steps to reproduce the issue
3. Record any error messages
4. Document the browser/device used
5. Submit the information for troubleshooting

This testing guide will help ensure your Wasit AI Citizen Assistant is functioning correctly and ready for presentation to the Wasit local government.
