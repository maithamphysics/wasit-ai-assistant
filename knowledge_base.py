import streamlit as st

class WasitChatbot:
    def __init__(self):
        self.knowledge_base = self._initialize_knowledge_base()
        self.environmental_knowledge = self._initialize_environmental_knowledge()
        
    def _initialize_knowledge_base(self):
        return {
            "birth certificate": "To obtain a birth certificate in Wasit, you need to provide:\n1. Hospital birth record or midwife statement\n2. Parents' ID cards\n3. Marriage certificate of parents\n4. Completed application form\n\nThe process takes approximately 3-5 working days and costs 5,000 IQD. You can apply at any Civil Status Affairs office in Wasit.",
            
            "marriage certificate": "For a marriage certificate in Wasit, both parties must:\n1. Be present with original ID cards\n2. Provide blood test results (must be within 30 days)\n3. Have two witnesses present with their ID cards\n4. Complete the application form\n5. Pay the fee of 25,000 IQD\n\nThe certificate is typically issued the same day at the Personal Status Court.",
            
            "death certificate": "To obtain a death certificate in Wasit, you need:\n1. Medical report confirming the death\n2. Deceased person's ID card\n3. Applicant's ID card (must be a relative)\n4. Completed application form\n\nThe certificate is issued within 1-2 working days at the Civil Status Affairs office and costs 5,000 IQD.",
            
            "id card renewal": "To renew an ID card in Wasit, you need:\n1. Old ID card (even if expired)\n2. Recent color photographs (4 copies)\n3. Residence proof (electricity/water bill)\n4. Completed application form\n5. Fee of 10,000 IQD\n\nProcessing time is approximately 7-10 working days at the Civil Status Affairs office.",
            
            "passport application": "For a passport application in Wasit, you need:\n1. Original and copy of national ID card\n2. Recent color photographs (6 copies with blue background)\n3. Completed application form\n4. Fee of 50,000 IQD (standard) or 100,000 IQD (expedited)\n\nProcessing takes 2-3 weeks for standard or 1 week for expedited service. Apply at the Passport Office in Al-Kut.",
            
            "residence permit": "For a residence permit in Wasit, foreign nationals must provide:\n1. Valid passport with at least 6 months validity\n2. Entry visa or stamp\n3. Completed application form\n4. Sponsor letter (for work permits) or property documentation (for property owners)\n5. Health certificate from an approved center\n6. Fee varies based on nationality and permit type\n\nApply at the Residency Affairs Office in Al-Kut.",
            
            "business registration": "To register a business in Wasit, you need:\n1. Completed application form\n2. ID cards of all owners/partners\n3. Lease agreement or property deed for business location\n4. Initial capital deposit confirmation\n5. Business activity description\n6. Fee ranging from 50,000-500,000 IQD depending on business type\n\nThe process takes approximately 10-15 working days at the Chamber of Commerce.",
            
            "trade license": "For a trade license in Wasit, you need:\n1. Business registration certificate\n2. Tax clearance certificate\n3. Property deed or lease agreement\n4. Health certificate (for food-related businesses)\n5. Environmental approval (for industrial activities)\n6. Fee ranging from 30,000-200,000 IQD depending on trade type\n\nApply at the Trade Licensing Department in your district.",
            
            "construction permit": "To obtain a construction permit in Wasit, you need:\n1. Land deed or ownership proof\n2. Architectural and structural plans (4 copies) approved by a registered engineer\n3. Site plan showing boundaries and setbacks\n4. Neighbor notification acknowledgments\n5. Fee based on construction area (approximately 25,000 IQD per 100 square meters)\n\nProcessing takes 20-30 days at the Municipality Office.",
            
            "tax filing": "For tax filing in Wasit, businesses must submit:\n1. Annual financial statements\n2. Sales and purchase records\n3. Employee salary information\n4. Tax registration number\n5. Previous year's tax clearance\n\nThe deadline is March 31st each year for the previous fiscal year. File at the Tax Authority Office in Al-Kut.",
            
            "import/export license": "For an import/export license in Wasit, you need:\n1. Business registration certificate\n2. Tax clearance certificate\n3. Chamber of Commerce membership\n4. Bank statement showing financial capability\n5. List of goods to be imported/exported\n6. Fee of 150,000 IQD\n\nProcessing takes approximately 15-20 working days at the Trade Ministry branch office.",
            
            "road maintenance request": "To request road maintenance in Wasit, you can:\n1. Submit a written request to your district Municipality Office\n2. Use the online service portal at wasit.gov.iq/services\n3. Call the infrastructure hotline at 07XX-XXX-XXX\n\nInclude the exact location, description of the problem, and photos if possible. Requests are prioritized based on severity and available resources.",
            
            "water supply issues": "For water supply problems in Wasit, you can:\n1. Report to the Water Authority office in your district\n2. Call the water emergency hotline at 07XX-XXX-XXX\n3. Submit a report through the Wasit services portal\n\nProvide your address, the nature of the problem (low pressure, contamination, outage), and how long it has been occurring. Emergency issues are typically addressed within 24-48 hours.",
            
            "electricity problems": "To report electricity problems in Wasit, you can:\n1. Contact the Electricity Distribution Office in your district\n2. Call the power outage hotline at 07XX-XXX-XXX\n3. Report through the online services portal\n\nSpecify whether it's a complete outage, voltage issues, or infrastructure problem. Include your address and account number if available. Emergency responses typically occur within 4-24 hours.",
            
            "waste collection": "For waste collection services in Wasit:\n1. Regular collection occurs 3 times weekly in urban areas and twice weekly in rural areas\n2. For missed collections, contact the Sanitation Department at 07XX-XXX-XXX\n3. Bulky item collection requires a special request form from your district office\n\nWaste should be placed in proper containers before 6:00 AM on collection days.",
            
            "public lighting": "To report public lighting issues in Wasit, you can:\n1. Submit a maintenance request to your district Municipality Office\n2. Call the street lighting hotline at 07XX-XXX-XXX\n3. Report through the online services portal\n\nInclude the exact location (street name, nearest landmark) and the nature of the problem (lights out, flickering, damaged pole). Repairs typically occur within 5-10 working days.",
            
            "farming subsidies": "Wasit farmers can access several subsidies:\n1. Seed subsidies (50% reduction for wheat and barley)\n2. Fertilizer subsidies (40% reduction for registered farmers)\n3. Fuel subsidies during planting and harvest seasons\n4. Equipment purchase subsidies (up to 30% for locally manufactured equipment)\n\nApply at the Agricultural Directorate with your land deed, farmer ID card, and cultivation plan. Application periods are announced seasonally.",
            
            "agricultural permits": "For agricultural permits in Wasit, you need:\n1. Land ownership or lease documentation\n2. Farmer ID card\n3. Cultivation plan specifying crops and area\n4. Water rights documentation (for irrigated farming)\n5. Fee of 15,000-30,000 IQD depending on permit type\n\nApply at the Agricultural Directorate office in your district. Processing takes 7-14 days.",
            
            "water rights": "To establish water rights for agriculture in Wasit, you must:\n1. Submit an application to the Water Resources Directorate\n2. Provide land ownership documentation\n3. Submit a cultivation plan showing water requirements\n4. Pay the application fee of 25,000 IQD\n5. Await inspection by water engineers\n\nAllocation decisions are based on available resources, land area, crop type, and existing rights. The process takes 30-45 days.",
            
            "crop disease reporting": "To report crop diseases in Wasit, farmers should:\n1. Contact the Plant Protection Department at 07XX-XXX-XXX\n2. Provide samples of affected plants if possible\n3. Allow agricultural engineers to inspect the affected area\n\nEmergency response teams are available for serious outbreaks. Free diagnosis and treatment recommendations are provided, with subsidized pesticides available for registered farmers.",
            
            "market access programs": "Wasit farmers can benefit from market access programs including:\n1. Cooperative marketing associations for major crops\n2. Government purchasing programs for strategic crops (wheat, barley, rice)\n3. Export facilitation for high-value crops\n4. Farmers' markets in major towns (weekly schedule available at district offices)\n\nFor more information, contact the Agricultural Marketing Department at the Directorate of Agriculture.",
            
            "working hours": "Government offices in Wasit operate Sunday through Thursday from 9:00 AM to 3:00 PM. Service centers in major districts have extended hours until 5:00 PM. Offices are closed on Fridays, Saturdays, and national holidays. Some emergency services maintain 24-hour operations.",
            
            "document requirements": "Most government services in Wasit require:\n1. Original and copy of national ID card\n2. Recent color photographs\n3. Completed application forms (available at service centers or online)\n4. Service-specific documentation\n5. Applicable fees\n\nSome services may require additional documentation. It's recommended to check specific requirements before visiting government offices.",
            
            "office locations": "Main government offices in Wasit are located in Al-Kut, the provincial capital. District centers in Al-Hai, Al-Aziziyah, Badra, Numaniyah, and Suwaira also provide most common services. The Wasit Government Complex in Al-Kut houses most provincial directorates and is located on Government Street in the city center."
        }
    
    def _initialize_environmental_knowledge(self):
        return {
            "water conservation": """
Water conservation is critical in Wasit due to severe shortages. Here are effective conservation methods:

For households:
- Fix leaky faucets and pipes (saves up to 20 liters per day)
- Take shorter showers (reducing by 2 minutes saves 15-20 liters)
- Install water-efficient fixtures (reduces usage by 30-50%)
- Collect and reuse gray water for cleaning or irrigation
- Run washing machines only when full (saves 15-45 liters per load)
- Use a bucket instead of a hose for washing cars (saves up to 300 liters)
- Water gardens during early morning or evening to reduce evaporation

For agriculture:
- Implement drip irrigation systems (90-95% efficiency vs. 60-70% for traditional methods)
- Schedule irrigation based on crop water requirements and weather conditions
- Use soil moisture monitoring to optimize irrigation timing
- Apply mulch around plants to retain moisture (reduces water needs by 25%)
- Consider drought-resistant crop varieties suitable for Wasit's climate
- Maintain irrigation systems to prevent leaks and water waste

Current water distribution schedules by district are available in the Water Resources tab. For water emergencies, contact the Water Authority at the emergency hotline.
            """,
            
            "heat safety": """
With temperatures in Wasit regularly exceeding 45°C in summer, heat safety is essential:

Personal protection:
- Drink 2-4 liters of water daily, even when not thirsty
- Avoid outdoor activities between 11:00 AM and 4:00 PM
- Wear lightweight, light-colored, loose-fitting clothing
- Use cooling techniques: damp cloths on neck/wrists, cool showers
- Know the signs of heat illness: dizziness, nausea, headache, rapid heartbeat
- Move to air-conditioned spaces during peak heat hours when possible

Home cooling without air conditioning:
- Close windows and blinds during day, open at night for ventilation
- Use wet sheets hung in doorways for evaporative cooling
- Place bowls of water around the house to increase humidity
- Create cross-ventilation with strategically placed fans
- Sleep on the lowest level of your home as heat rises
- Dampen sheets before sleeping for cooling effect

For vulnerable populations (elderly, children, pregnant women, those with chronic conditions):
- Check on vulnerable family members and neighbors twice daily
- Ensure proper medication storage (most medications should stay below 25°C)
- Never leave children in vehicles, even for a minute
- Schedule outdoor activities for early morning or evening hours

Cooling centers are available throughout Wasit during extreme heat. Locations and hours are listed in the Heat Safety tab.
            """,
            
            "agricultural adaptation": """
Wasit farmers can adapt to water scarcity and high temperatures with these strategies:

Water-efficient farming:
- Convert to drip irrigation systems (government subsidies available)
- Implement deficit irrigation strategies for water-stressed periods
- Use laser land leveling to improve water distribution efficiency
- Install soil moisture sensors to optimize irrigation timing
- Collect and store rainwater during rainy season

Heat-resistant agriculture:
- Plant heat-tolerant crop varieties (contact Agricultural Directorate for recommendations)
- Adjust planting calendar to avoid crop development during peak heat
- Use shade cloth for sensitive crops during extreme heat periods
- Apply white kaolin clay spray to reduce leaf temperature
- Increase plant spacing to reduce competition for water
- Create windbreaks to reduce evapotranspiration

Soil management:
- Increase organic matter in soil to improve water retention
- Use mulching to reduce soil water evaporation by up to 25%
- Implement minimum tillage to preserve soil moisture
- Practice contour farming to reduce water runoff
- Add compost to improve soil structure and water holding capacity

The Agricultural Support Line (07XX-XXX-XXX) provides technical assistance for implementing these adaptations. Some measures qualify for government subsidies through the Agricultural Directorate.
            """,
            
            "emergency resources": """
Wasit has several emergency resources for environmental challenges:

Emergency contacts:
- Water Emergency Hotline: 07XX-XXX-XXX (24/7 for water outages, contamination)
- Heat Health Hotline: 07XX-XXX-XXX (for heat-related health emergencies)
- Agricultural Support Line: 07XX-XXX-XXX (for urgent agricultural assistance)
- General Emergency: 104 (Police), 122 (Ambulance), 115 (Fire)

Water emergency resources:
- Emergency water distribution points are activated during severe shortages
- Water tanker services are available for critical needs (request through Water Authority)
- Water quality testing is available for suspected contamination
- Emergency repair teams respond to major infrastructure failures

Heat emergency resources:
- Cooling centers are open during extreme heat events (see Heat Safety tab)
- Medical response teams are trained for heat-related illnesses
- Emergency power is prioritized for critical cooling infrastructure
- Vulnerable population registries for wellness checks during heat waves

Agricultural emergency support:
- Drought response team provides technical assistance
- Emergency irrigation allocation for critical crop stages
- Pest and disease rapid response for outbreaks
- Livestock support during extreme conditions

Sign up for emergency alerts via SMS by registering your mobile number in the Emergency Resources tab.
            """,
            
            "climate information": """
Wasit's climate is characterized by extremely hot summers and mild winters:

Temperature patterns:
- Summer (June-September): Daytime highs regularly exceed 45°C, nighttime lows around 30°C
- Winter (December-February): Daytime highs 15-20°C, nighttime lows can drop to 5°C or below
- Spring/Fall: Rapid temperature transitions with daily fluctuations of 15-20°C

Precipitation:
- Annual rainfall: Approximately 100-150mm, primarily between November and April
- Rainfall has decreased by approximately 15-20% in the past decade
- Precipitation events have become more intense but less frequent

Climate trends:
- Average temperatures have increased by 1.5°C since 1980
- Heat waves have increased in frequency, intensity, and duration
- Drought periods have become more frequent and prolonged
- Growing season has shifted by approximately 2-3 weeks

Climate projections:
- Continued temperature increases of 2-4°C by 2050
- Further reduction in precipitation by 10-30% by 2050
- Increased frequency of extreme weather events
- Water availability from rivers projected to decrease by up to 60% by 2025

The Environmental Monitoring Station in Al-Kut provides daily updates on temperature, humidity, and air quality. This information is used to issue heat warnings and agricultural advisories.
            """
        }
    
    def get_response(self, user_input):
        # Convert input to lowercase for easier matching
        user_input_lower = user_input.lower()
        
        # Check for environmental queries first
        for topic, response in self.environmental_knowledge.items():
            if topic in user_input_lower:
                return response
        
        # Check for water-related queries
        if any(term in user_input_lower for term in ["water", "drought", "irrigation", "drinking"]):
            return self.environmental_knowledge["water conservation"]
        
        # Check for heat-related queries
        if any(term in user_input_lower for term in ["heat", "temperature", "hot", "cool", "cooling"]):
            return self.environmental_knowledge["heat safety"]
        
        # Check for agriculture-related environmental queries
        if any(term in user_input_lower for term in ["farm", "crop", "agriculture"]) and any(term in user_input_lower for term in ["heat", "water", "drought", "temperature"]):
            return self.environmental_knowledge["agricultural adaptation"]
        
        # Check for emergency-related environmental queries
        if any(term in user_input_lower for term in ["emergency", "crisis", "urgent"]) and any(term in user_input_lower for term in ["water", "heat", "temperature"]):
            return self.environmental_knowledge["emergency resources"]
        
        # Check for climate-related queries
        if any(term in user_input_lower for term in ["climate", "weather", "temperature pattern", "rainfall"]):
            return self.environmental_knowledge["climate information"]
        
        # Check for standard government service queries
        for keyword, response in self.knowledge_base.items():
            if keyword in user_input_lower:
                return response
        
        # Generate response for greetings
        if any(greeting in user_input_lower for greeting in ["hello", "hi", "greetings", "salam", "good morning", "good afternoon", "good evening"]):
            return "Hello! I'm the Wasit AI Citizen Assistant. I can help you with government services, water conservation information, heat safety guidance, and more. How can I assist you today?"
        
        # Generate response for thanks
        if any(thanks in user_input_lower for thanks in ["thank", "thanks", "appreciate", "grateful"]):
            return "You're welcome! I'm here to help with any information about Wasit government services and environmental challenges. Is there anything else you'd like to know?"
        
        # Default response if no match is found
        return "I don't have specific information about that topic yet. I can help with government services, water conservation, heat safety, agricultural adaptation, and emergency resources in Wasit. Please try asking about one of these topics or rephrase your question."
