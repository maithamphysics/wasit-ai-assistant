# Wasit AI Citizen Assistant

## Overview
The Wasit AI Citizen Assistant is a prototype application designed to help citizens of Wasit Governorate, Iraq access government services, find information, and submit requests. The system provides information about procedures, required documents, and processing times for various government services through an intuitive chat interface.

![Wasit AI Citizen Assistant](https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Iraq.svg/320px-Flag_of_Iraq.svg.png)

## Features
- **Interactive Chat Interface**: User-friendly conversational interface for citizens to ask questions
- **Comprehensive Knowledge Base**: Detailed information about government services in Wasit
- **Service Categories**: Organized information about citizen services, business services, infrastructure, and agriculture
- **Bilingual Support**: Interface supports both English and Arabic (Arabic content to be expanded)
- **AI-Powered Responses**: Combines rule-based responses with advanced AI capabilities
- **Quick Links**: Fast access to commonly requested information

## Service Categories
1. **Citizen Services**
   - Birth Certificate
   - Marriage Certificate
   - Death Certificate
   - ID Card Renewal
   - Passport Application
   - Residence Permit

2. **Business Services**
   - Business Registration
   - Trade License
   - Construction Permit
   - Tax Filing
   - Import/Export License

3. **Infrastructure**
   - Road Maintenance Request
   - Water Supply Issues
   - Electricity Problems
   - Waste Collection
   - Public Lighting

4. **Agriculture**
   - Farming Subsidies
   - Agricultural Permits
   - Water Rights
   - Crop Disease Reporting
   - Market Access Programs

## Technology Stack
- **Frontend & Backend**: Streamlit (Python web framework)
- **AI Components**: LangChain, OpenAI (optional for enhanced capabilities)
- **Data Storage**: Local knowledge base (expandable to database)

## Getting Started
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`
4. Access the application at http://localhost:8501

For detailed deployment instructions, see [deployment_instructions.md](deployment_instructions.md).

## Enhanced AI Capabilities
For enhanced AI capabilities, you can provide an OpenAI API key:
1. Create a `.env` file in the root directory
2. Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`
3. Restart the application

## Future Enhancements
- Full Arabic language support
- Integration with government databases
- Mobile application version
- Document upload and processing
- Appointment scheduling
- Service status tracking
- Citizen feedback collection

## About This Project
This prototype was developed as part of a digital transformation initiative for Wasit Governorate to demonstrate the potential of AI in improving government service delivery and citizen engagement.

## License
This project is proprietary and confidential. Unauthorized copying, distribution, or use is prohibited.

© 2025 Wasit Governorate - AI Citizen Assistant Prototype
