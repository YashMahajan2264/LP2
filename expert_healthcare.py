problem_dict = { "Patient not responding": "1. Check vital signs and assess patient's condition.\n2. Administer emergenc\n3. Notify attending physician and escalate as appropriate.",
    "Equipment malfunction": "1. Perform basic troubleshooting on the equipment.\n2. Notify biomedical engineering department for repair.\n3. Have backup equipment ready if available.",
    "Medication error": "1. Assess patient for any adverse effects.\n2. Notify pharmacy and attending physician immediately.\n3. Document the error and follow hospital protocol for reporting.",
    "Patient fall": "1. Assess patient for any injuries.\n2. Notify nursing staff and attending physician.\n3. Implement fall prevention measures for the patient.",
    "Code blue (Cardiac arrest)": "1. Initiate cardiopulmonary resuscitation (CPR).\n2. Call for a code blue team.\n3. Follow ACLS (Advanced Cardiac Life Support) protocol.",
    "Infection control breach": "1. Isolate affected area and patients if necessary.\n2. Notify infection control team.\n3. Implement enhanced cleaning and disinfection protocols.",
    "Emergency evacuation": "1. Remain calm and follow hospital evacuation procedures.\n2. Assist patients and staff with mobility as needed.\n3. Ensure communication with emergency services and hospital leadership.",
    "Power outage": "1. Activate backup power sources if available.\n2. Prioritize critical patient care areas.\n3. Communicate with hospital administration and utility providers.",
    "Medical supply shortage": "1. Prioritize essential supplies for patient care.\n2. Notify supply chain management for restocking.\n3. Implement conservation strategies.",
    "IT system failure": "1. Notify IT department immediately.\n2. Implement manual documentation processes if necessary.\n3. Provide alternative communication channels for critical updates.",
}
def handle_request(user_input):
    if user_input.lower() == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry, I don't know how to help with that problem."
while True:
    user_input = input("What's the problem? Type 'exit' to quit. ")
    response = handle_request(str(user_input)) 
    print(response)
