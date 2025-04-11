import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from chatbot import WasitChatbot
from datetime import datetime

# Load environment variables - for local development
load_dotenv()

# For Streamlit Cloud deployment
def get_api_key():
    # Try to get from Streamlit secrets first (for cloud deployment)
    try:
        return st.secrets["OPENAI_API_KEY"]
    except:
        # Fall back to environment variable (for local development)
        return os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="Wasit AI Assistant",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E5631;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #1E5631;
        margin-bottom: 1rem;
    }
    .chat-container {
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        margin-bottom: 20px;
    }
    .user-message {
        background-color: #DCF8C6;
        padding: 10px 15px;
        border-radius: 10px;
        margin: 5px 0;
        text-align: right;
        margin-left: 20%;
    }
    .bot-message {
        background-color: #FFFFFF;
        padding: 10px 15px;
        border-radius: 10px;
        margin: 5px 0;
        border-left: 4px solid #1E5631;
        margin-right: 20%;
    }
    .stButton button {
        background-color: #1E5631;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .sidebar-content {
        padding: 20px;
    }
    .alert-box {
        background-color: #FFF3CD;
        border-left: 4px solid #FFC107;
        padding: 10px 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #D1ECF1;
        border-left: 4px solid #17A2B8;
        padding: 10px 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .metric-container {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #1E5631;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #666;
    }
    .resource-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .resource-card h4 {
        color: #1E5631;
        margin-top: 0;
    }
    .rice-advice {
        background-color: #E8F5E9;
        border-left: 4px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize chatbot
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = WasitChatbot()

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Chat"

if 'services' not in st.session_state:
    st.session_state.services = {
        "Citizen Services": [
            "Birth Certificate",
            "Marriage Certificate",
            "Death Certificate",
            "ID Card Renewal",
            "Passport Application",
            "Residence Permit"
        ],
        "Business Services": [
            "Business Registration",
            "Trade License",
            "Construction Permit",
            "Tax Filing",
            "Import/Export License"
        ],
        "Infrastructure": [
            "Road Maintenance Request",
            "Water Supply Issues",
            "Electricity Problems",
            "Waste Collection",
            "Public Lighting"
        ],
        "Agriculture": [
            "Farming Subsidies",
            "Agricultural Permits",
            "Water Rights",
            "Crop Disease Reporting",
            "Market Access Programs",
            "Rice Growing Advice"  # Added new service
        ],
        "Environmental": [
            "Water Conservation",
            "Heat Safety",
            "Agricultural Adaptation",
            "Emergency Resources",
            "Climate Information"
        ]
    }

# Initialize environmental data
if 'environmental_data' not in st.session_state:
    st.session_state.environmental_data = {
        "current_temperature": 42,
        "heat_warning_level": "Warning",
        "water_status": "Shortage",
        "water_schedule": {
            "Al-Kut": "6:00-9:00 AM, 6:00-8:00 PM",
            "Al-Hai": "7:00-10:00 AM, 7:00-9:00 PM",
            "Al-Aziziyah": "5:00-8:00 AM, 5:00-7:00 PM",
            "Badra": "8:00-11:00 AM, 8:00-10:00 PM",
            "Numaniyah": "6:30-9:30 AM, 6:30-8:30 PM",
            "Suwaira": "7:30-10:30 AM, 7:30-9:30 PM"
        },
        "cooling_centers": [
            {"name": "Al-Kut Community Center", "address": "Main Street, Al-Kut", "hours": "10:00 AM - 8:00 PM"},
            {"name": "Al-Hai Public Library", "address": "Central Square, Al-Hai", "hours": "9:00 AM - 7:00 PM"},
            {"name": "Wasit University Hall", "address": "University Campus, Al-Kut", "hours": "8:00 AM - 6:00 PM"},
            {"name": "Al-Aziziyah Health Center", "address": "Hospital Road, Al-Aziziyah", "hours": "24 hours"},
            {"name": "Numaniyah Shopping Mall", "address": "Commercial District, Numaniyah", "hours": "10:00 AM - 10:00 PM"}
        ],
        "emergency_contacts": {
            "Water Emergency": "+964 7XX XXX XXX",
            "Heat Health Hotline": "+964 7XX XXX XXX",
            "Agricultural Support": "+964 7XX XXX XXX"
        },
        "rice_growing": {  # Added rice growing data
            "Al-Kut": {"planting": "April 15 - May 15", "harvest": "September - October", "variety": "Amber 33"},
            "Al-Hai": {"planting": "April 20 - May 20", "harvest": "September - October", "variety": "Najaf 1"},
            "Al-Aziziyah": {"planting": "May 1 - June 1", "harvest": "October - November", "variety": "Najaf 1"},
            "Badra": {"planting": "May 1 - June 1", "harvest": "October - November", "variety": "Amber 33"},
            "Numaniyah": {"planting": "April 25 - May 25", "harvest": "September - October", "variety": "Amber 33"},
            "Suwaira": {"planting": "April 20 - May 20", "harvest": "September - October", "variety": "Najaf 1"}
        }
    }

# Initialize LangChain components if OpenAI API key is available
api_key = get_api_key()
if api_key:
    if 'llm' not in st.session_state:
        st.session_state.llm = OpenAI(temperature=0.7, openai_api_key=api_key)
    
    if 'memory' not in st.session_state:
        st.session_state.memory = ConversationBufferMemory()
    
    if 'conversation' not in st.session_state:
        st.session_state.conversation = ConversationChain(
            llm=st.session_state.llm,
            memory=st.session_state.memory,
            verbose=True
        )

# Sidebar content
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Iraq.svg/1200px-Flag_of_Iraq.svg.png", width=100)
    st.markdown("<h2 style='text-align: center;'>Wasit Governorate</h2>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    
    # Environmental Alert Section
    st.markdown("### Environmental Alerts")
    
    # Temperature Alert
    temp = st.session_state.environmental_data["current_temperature"]
    warning_level = st.session_state.environmental_data["heat_warning_level"]
    
    if warning_level == "Warning" or warning_level == "Danger":
        st.markdown(f"""
        <div class='alert-box'>
        <strong>🔥 Heat {warning_level}:</strong> Current temperature is {temp}°C. 
        Limit outdoor activities and stay hydrated.
        </div>
        """, unsafe_allow_html=True)
    
    # Water Alert
    water_status = st.session_state.environmental_data["water_status"]
    if water_status == "Shortage":
        st.markdown(f"""
        <div class='alert-box'>
        <strong>💧 Water {water_status}:</strong> Conservation measures in effect.
        Check district schedule for availability.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### Available Services")
    
    # Display service categories in the sidebar
    selected_category = st.selectbox("Select Service Category", list(st.session_state.services.keys()))
    
    # Display services in the selected category
    selected_service = st.selectbox("Select Service", st.session_state.services[selected_category])
    
    if st.button("Ask about this service"):
        user_input = f"I need information about {selected_service}"
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get response from chatbot
        ai_response = st.session_state.chatbot.get_response(user_input)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        st.rerun()
    
    st.markdown("### Language / اللغة")
    language = st.radio("", ["English", "العربية"], horizontal=True)
    
    st.markdown("### Contact Information")
    st.markdown("📍 Al-Kut, Wasit Governorate, Iraq")
    st.markdown("📞 +964 123 456 789")
    st.markdown("📧 info@wasit.gov.iq")
    
    # Add OpenAI API key input for demo purposes - only for local development
    if not api_key:
        st.markdown("### AI Configuration")
        api_key_input = st.text_input("OpenAI API Key (for enhanced AI)", type="password", value="")
        if api_key_input:
            os.environ["OPENAI_API_KEY"] = api_key_input
            st.success("API key updated! Enhanced AI capabilities activated.")
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Main content
st.markdown("<h1 class='main-header'>Wasit AI Citizen Assistant</h1>", unsafe_allow_html=True)

# Tabs for different sections
tabs = ["Chat", "Water Resources", "Heat Safety", "Emergency Resources", "Agriculture"]  # Added Agriculture tab
st.session_state.current_tab = st.radio("", tabs, horizontal=True)

if st.session_state.current_tab == "Chat":
    # Introduction text
    st.markdown("""
    This AI assistant helps citizens of Wasit Governorate access government services, 
    find information, and submit requests. The system can answer questions about procedures, 
    required documents, processing times, and environmental challenges like water scarcity and high temperatures.
    """)

    # Chat interface
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    st.markdown("<h2 class='sub-header'>How can I help you today?</h2>", unsafe_allow_html=True)

    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"<div class='user-message'>{message['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-message'>{message['content']}</div>", unsafe_allow_html=True)

    # Input for new message
    user_input = st.text_input("Type your question here...", key="user_input")

    if st.button("Send"):
        if user_input:
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Get response from chatbot
            if api_key and "how can ai help wasit" in user_input.lower():
                # Use LangChain for more advanced AI responses when appropriate
                ai_response = st.session_state.conversation.predict(input=f"""
                The user is asking about how AI can help Wasit local government. Provide a detailed response based on these facts:
                - Wasit is a governorate in eastern Iraq with approximately 1.45 million people
                - The local government has been improving governance and completing infrastructure projects
                - AI can help with document management, citizen services, agricultural optimization, and infrastructure monitoring
                - Wasit has limited digital infrastructure but is working on improvement
                - The government is interested in digital transformation initiatives
                - Wasit faces significant water scarcity challenges with decreasing water allocation
                - The region experiences extremely high temperatures reaching up to 48°C in summer
                
                Provide specific examples of how AI can improve government operations and citizen services in Wasit, particularly in addressing water scarcity and high temperature challenges.
                """)
            else:
                # Use rule-based chatbot for standard queries
                ai_response = st.session_state.chatbot.get_response(user_input)
            
            # Add AI response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            
            # Rerun to update the display with new messages
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Quick links section
    st.markdown("<h2 class='sub-header'>Quick Links</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Water Conservation"):
            st.session_state.chat_history.append({"role": "user", "content": "How can I conserve water during the shortage?"})
            ai_response = "Here are key water conservation tips for Wasit residents:\n\n- Fix leaky faucets and pipes (saves up to 20 liters per day)\n- Take shorter showers (reducing by 2 minutes saves 15-20 liters)\n- Collect and reuse gray water for plants and cleaning\n- Water gardens only during early morning or evening to reduce evaporation\n- Use a bucket instead of a hose for washing cars\n- Run washing machines and dishwashers only when full\n- Install water-efficient fixtures if possible\n\nFor agricultural water conservation, consider drip irrigation systems which are 90-95% efficient compared to traditional methods. The current water distribution schedule for your district can be found in the Water Resources tab."
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            st.rerun()

    with col2:
        if st.button("Heat Safety"):
            st.session_state.chat_history.append({"role": "user", "content": "How can I stay safe during extreme heat?"})
            ai_response = "During Wasit's extreme heat (currently 42°C), follow these safety guidelines:\n\n- Drink plenty of water (2-4 liters daily) even if not thirsty\n- Avoid outdoor activities between 11am-4pm\n- Wear lightweight, light-colored, loose-fitting clothing\n- Use cooling techniques: damp cloths on neck/wrists, cool showers\n- Know the signs of heat illness: dizziness, nausea, headache, rapid heartbeat\n\nIf you need relief from the heat, cooling centers are available throughout Wasit. See the Heat Safety tab for locations and hours. For heat-related emergencies, call the Heat Health Hotline at +964 7XX XXX XXX."
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            st.rerun()

    with col3:
        if st.button("Agricultural Advice"):
            st.session_state.chat_history.append({"role": "user", "content": "What agricultural adaptations are recommended for current conditions?"})
            ai_response = "For Wasit farmers dealing with current water scarcity and high temperatures:\n\n**Water Management:**\n- Implement drip irrigation (90-95% efficiency vs. 60-70% for traditional methods)\n- Schedule irrigation during early morning or evening to reduce evaporation\n- Use soil moisture monitoring to optimize irrigation timing\n- Apply mulching to reduce soil water evaporation by up to 25%\n\n**Heat Adaptation:**\n- Consider heat-resistant crop varieties (contact Agricultural Department for specific recommendations)\n- Use shade cloth for sensitive crops during peak heat\n- Increase plant spacing to reduce competition for water\n- Apply white kaolin clay spray to reduce leaf temperature\n\nFor technical assistance with agricultural adaptations, contact the Agricultural Support line at +964 7XX XXX XXX."
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            st.rerun()

    with col4:
        if st.button("Emergency Contacts"):
            st.session_state.chat_history.append({"role": "user", "content": "What emergency contacts should I have for environmental issues?"})
            ai_response = "**Emergency Contacts for Environmental Issues in Wasit:**\n\n- **Water Emergency Hotline:** +964 7XX XXX XXX\n  *For water outages, contamination, or infrastructure failures*\n\n- **Heat Health Hotline:** +964 7XX XXX XXX\n  *For heat-related health emergencies or cooling center information*\n\n- **Agricultural Support Line:** +964 7XX XXX XXX\n  *For urgent agricultural assistance during extreme conditions*\n\n- **General Emergency:** 104 (Police), 122 (Ambulance)\n\nAll emergency services operate 24/7. For non-emergency environmental inquiries, call during regular government hours (Sunday-Thursday, 9am-3pm)."
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
            st.rerun()

elif st.session_state.current_tab == "Water Resources":
    # ... [Previous Water Resources tab content remains the same] ...

elif st.session_state.current_tab == "Heat Safety":
    # ... [Previous Heat Safety tab content remains the same] ...

elif st.session_state.current_tab == "Emergency Resources":
    # ... [Previous Emergency Resources tab content remains the same] ...

elif st.session_state.current_tab == "Agriculture":
    st.markdown("<h2 class='sub-header'>Agricultural Resources</h2>", unsafe_allow_html=True)
    
    # Rice Growing Advice Section
    st.markdown("### 🌾 Rice Growing Guide for Wasit")
    
    # Get user input
    district = st.selectbox("Select your district:", 
                          list(st.session_state.environmental_data["rice_growing"].keys()))
    
    # Get current date
    today = datetime.now()
    current_month = today.month
    
    # Get rice data for selected district
    rice_data = st.session_state.environmental_data["rice_growing"][district]
    planting_start = datetime.strptime(rice_data["planting"].split(" - ")[0], "%B %d").month
    planting_end = datetime.strptime(rice_data["planting"].split(" - ")[1], "%B %d").month
    
    # Determine current planting status
    if current_month >= planting_start and current_month <= planting_end:
        planting_status = "✅ Currently in planting season"
        status_color = "green"
    else:
        planting_status = "❌ Not currently planting season"
        status_color = "red"
    
    # Display rice growing advice
    st.markdown(f"""
    <div class='rice-advice'>
        <h3>Rice Cultivation for {district}</h3>
        <p><strong>Recommended Variety:</strong> {rice_data['variety']}</p>
        <p><strong>Planting Window:</strong> {rice_data['planting']}</p>
        <p><strong>Harvest Time:</strong> {rice_data['harvest']}</p>
        <p style='color:{status_color};'><strong>Status:</strong> {planting_status}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Detailed growing advice
    st.markdown("#### Growing Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Water Management**")
        st.markdown("""
        - Requires 1200-1500mm water per growing season
        - Maintain 5-7cm standing water during vegetative stage
        - Gradually reduce water 2 weeks before harvest
        - Use alternate wetting/drying to save 15-30% water
        """)
    
    with col2:
        st.markdown("**Soil Preparation**")
        st.markdown("""
        - Level fields carefully (max 3cm variation)
        - Apply 10-15 tons/ha organic matter
        - Maintain soil pH 5.5-6.5
        - Conduct soil test for micronutrients
        """)
    
    st.markdown("#### Current Season Advice")
    if current_month >= planting_start and current_month <= planting_end:
        st.markdown("""
        - Prepare fields with proper leveling
        - Soak seeds for 24 hours before sowing
        - Maintain nursery for 25-30 days before transplanting
        - Apply basal fertilizer (NPK 15-15-15 at 200kg/ha)
        """)
    elif current_month > planting_end and current_month <= datetime.strptime(rice_data["harvest"].split(" - ")[1], "%B").month:
        st.markdown("""
        - Monitor for pests (stem borers, leaf folders)
        - Apply top dressing at tillering stage
        - Maintain consistent water level
        - Watch for nutrient deficiencies
        """)
    else:
        st.markdown("""
        - Prepare land for next season
        - Conduct soil tests
        - Repair irrigation systems
        - Plan crop rotation strategy
        """)
    
    # Rice water requirements calculator
    st.markdown("#### Water Requirements Calculator")
    area = st.number_input("Enter field area (hectares)", min_value=0.1, max_value=100.0, value=1.0)
    growth_stage = st.selectbox("Select growth stage", 
                              ["Nursery", "Land Preparation", "Vegetative", "Reproductive", "Ripening"])
    
    water_needs = {
        "Nursery": 25,
        "Land Preparation": 50,
        "Vegetative": 35,
        "Reproductive": 30,
        "Ripening": 20
    }
    
    total_water = area * water_needs[growth_stage]
    st.metric(f"Daily Water Requirement for {growth_stage} Stage", f"{total_water} m³/day")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p>© 2025 Wasit Governorate - AI Citizen Assistant</p>
    <p>Developed as part of the Wasit Digital Transformation Initiative</p>
</div>
""", unsafe_allow_html=True)