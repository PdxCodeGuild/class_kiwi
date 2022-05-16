                                                ELECTRONIC MEDICAL RECORD BILLING PROPOSAL
                OVERVIEW
One of the many causes for delayed or rejected reimbursements in healthcare is the ‘Unspecified’ billing codes. This codes were designed for diagnosis, procedures or encounters that are considered unknown. For a billing organization like Medicare, ‘I didn’t know what it was isn’t the same as ‘Unknown.’ The U.S. Healthcare system is a complex revenue focused generating system. Its users include doctors and billing specialists. Correcting billing concerns should involve the understanding that billing specialists aren’t doctors nor doctors billing specialists. A solution might involve hiring an individual with experience of breaching knowledge gap between the two specialties. The proposed project assumes the role of such an individual by providing an application that directly links an Electronic Medical Record (EMR) to an Evidence Based  Medicine website approved by the organization.

        Libraries
The project will utilize Django, JavaScript, HTML, CSS, Bootstrap or Tailwind(not sure whether I want to include bootstrap/tailwind for this project)

                FUNCTIONALITY
For users, an EMR billing system might look simple and easy to use based on the design however the complexity of the healthcare system makes designing one a complex process. Due to time constraints, this project will be as simple as possible and closer to the desired end project. The assumption is the doctor has completed all necessary documentation and only needs billing codes based on diagnosis.

        Users
Admin - will have permissions to assign access as doctors or billing specialist
Patients --- user specific
Doctors ---user specific
Billing specialists – user specific 

        User View
-It will be login required access 

    Doctors
-Site will be a simple blank input with a button. The input provides user avenue for specific search terms while the button is linked to the approved API. Once the button is clicked, results based on potential codes will be displayed. The user will then choose a desired diagnosis. (API--ICD10 Site)
    Billing
-Same thing as doctors only that the API will be linked to a diagnosis API. Design is the same, only that user will be confirming doctors’ input  by typing the code selected by the doctor and confirming that the diagnosis is accurate. (API—DIAGNOSIS)

                DATA MODEL
Stored Data --- the ICD-10 codes and retrieved diagnosis

                SCHEDULE
    Day 1-Day 4:
Create User Specific Accounts --- Admin, Patient, Doctor, Billing
    Day 5-Day 9: 
Link Accounts to respectable sites(API---Only 2)--- if possible, provide a front-end option that only admin can access (this ensures uniformity and adhering to strict organization utilization)
    Day 10-15:
Prettify the Site
    Day 16-20:
Testing and retesting site for functionality
    Day 21-23:
Hash out bugs
    Day 25:
Deploy
