import streamlit as st
import json
import os
import requests

# === LLM Configuration ===
LLM_API_KEY = os.getenv('LLM_API_KEY', 'sk-8c752e31ed8b401cbb8b84feea54e197').strip()
LLM_API_URL = os.getenv('LLM_API_URL', 'https://chat.ivislabs.in/v1/chat/completions').strip()

# === Embedded University Data ===
UNIVERSITY_DATA = {
    "university": {
        "basic_information": {
            "name": "University of Mysore",
            "established": "1916-07-27",
            "type": "Public State University",
            "location": {
                "city": "Mysuru",
                "state": "Karnataka",
                "country": "India",
                "coordinates": {
                    "latitude": "12°18'29.45\"N",
                    "longitude": "76°38'18.83\"E"
                },
                "distance_from_bengaluru": "140 km southwest"
            },
            "significance": [
                "Sixth oldest university in India",
                "First university in Karnataka",
                "First university outside British India",
                "First University accredited by NAAC in 2000 with Five Star Status"
            ]
        },
        "motto": {
            "sanskrit": "Na hi Jnanena Sadrisham",
            "english": "Nothing is equal to knowledge",
            "source": "Rigveda",
            "secondary_motto": {
                "sanskrit": "Satyamevoddaharamuaham",
                "english": "I always uphold the truth"
            }
        },
        "emblem": {
            "description": "Bird 'Gandabherunda' flanked on either side by lion-elephant Sharaba",
            "symbolism": "Mythical creature believed to be stronger than lion and elephant and upholder of righteousness"
        },
        "colors": {
            "primary": "Navy blue",
            "secondary": "White"
        },
        "founding_fathers": {
            "maharaja": {
                "name": "Shri Nalvadi Krishnaraja Wadiyar IV",
                "years": "1884-1940",
                "role": "First Chancellor"
            },
            "diwan": {
                "name": "Sir M. Visvesvaraya",
                "years": "1860-1962"
            },
            "first_vice_chancellor": {
                "name": "H. V. Nanjundaiah",
                "tenure": "1916-1920"
            }
        },
        "current_leadership": {
            "chancellor": "Governor of Karnataka",
            "vice_chancellor": {
                "name": "Lokanath N. K.",
                "start_year": 2024
            }
        },
        "vision": "To aspire to become a world-class University by tapping human resources from all sections of society by offering them opportunities to learn across disciplines, and to build human capital, men and women of character and competence capable of being leaders of tomorrow and solving problems arising out of fast changing realities – global and local.",
        "mission": "Built on a great legacy inherited from our founding fathers, our mission is to create an environment of stimulating intellectual dialogue across disciplines and harvest knowledge with a cutting-edge through high quality teaching, research, and extension activities leading to the generation of students who would provide leadership, vision and direction to society.",
        "goal": "To realize this vision by 2025",
        "campus": {
            "main_campus": {
                "name": "Manasagangotri",
                "meaning": "Eternal flow of the mind",
                "named_by": "Kuvempu (Poet-laureate and former Vice-Chancellor)",
                "area_acres": 739,
                "lake": {
                    "name": "Kukkarahalli lake",
                    "area_acres": 261
                }
            },
            "additional_campuses": [
                {
                    "name": "Sir M. Visvesvaraya Postgraduate Centre",
                    "location": "Tubinakere near Mandya",
                    "distance_from_mandya": "8 km",
                    "highway": "Mysore-Bangalore highway"
                },
                {
                    "name": "Postgraduate Centre",
                    "location": "Hemagangotri, Hassan",
                    "distance_from_hassan": "10 km",
                    "highway": "Mangalore-Bangalore highway",
                    "village": "Kenchattahalli"
                },
                {
                    "name": "Dr. B. R. Ambedkar Post-Graduate Centre",
                    "location": "Chamarajanagar",
                    "description": "Southern most district Headquarters of Karnataka State"
                }
            ],
            "administrative_building": {
                "name": "Crawford Hall",
                "location": "Adjacent to Kukkarahalli lake",
                "offices": [
                    "Vice-Chancellor",
                    "Registrar",
                    "Registrar (Evaluation)",
                    "Finance Officer",
                    "Public Grievance Cell"
                ]
            }
        },
        "statistics": {
            "academic_staff": 762,
            "total_students": 10946,
            "undergraduates": 5250,
            "postgraduates": 3623,
            "doctoral_students": 766,
            "total_enrolled": 120000,
            "pg_departments": 63,
            "pg_programmes": 76,
            "affiliated_colleges": 226,
            "recognized_research_centers": 66,
            "outreach_research_centers": 157,
            "training_centers": 8,
            "specialized_programmes": 47,
            "foreign_collaborations": 38,
            "national_collaborations": 27,
            "departments_with_national_research_facilities": 11,
            "chairs": 14,
            "dst_fist_departments": 13,
            "ugc_sap_funded_departments": 13,
            "supporting_units": 13,
            "overseas_students_countries": 63
        },
        "rankings": {
            "nirf_2020": {
                "india_rank": 27,
                "karnataka_rank": 1,
                "overall_rank": 47
            },
            "nirf_2021": {
                "india_rank": 19
            },
            "nirf_2024": {
                "universities_rank": 54,
                "overall_rank": 86
            }
        },
        "accreditation": {
            "naac": [
                {
                    "year": 2000,
                    "status": "Five Stars Status",
                    "significance": "First University in the State"
                },
                {
                    "cycle": 2,
                    "year": 2006,
                    "grade": "A+"
                },
                {
                    "cycle": 3,
                    "score": 3.47,
                    "max_score": 4,
                    "grade": "A+"
                },
                {
                    "year": 2013,
                    "grade": "A"
                }
            ],
            "other_affiliations": ["UGC", "AIU"]
        },
        "recognitions": {
            "institution_of_excellence": {
                "year": 2008,
                "grant_amount_crores": 100,
                "awarded_by": "Government of India"
            },
            "university_with_potential_for_excellence": {
                "year": 2009,
                "recognized_by": "UGC",
                "grant_amount_crores": 50,
                "year_awarded": 2012,
                "duration_years": 5,
                "extended": True
            },
            "cpepa": {
                "full_name": "Centre of Excellence in Potential for Excellence in a Particular Area",
                "grant_amount_crores": 9.5,
                "renewed_year": 2016
            },
            "purse_scheme": {
                "recognition": "Top 20 universities in Scientific publications",
                "phase_1_grant_crores": 9.0,
                "phase_2_year": 2016,
                "phase_2_grant_crores": 8.5
            },
            "innovation_university": {
                "year": 2009,
                "recognized_by": "Government of Karnataka"
            },
            "h_index": {
                "value": 42,
                "source": "Web of Science",
                "publications_count": 3609,
                "since_year": 1986
            },
            "autonomy": {
                "year": 1956,
                "date": "1956-03-03"
            }
        },
        "faculties": [
            "Arts, Humanities and Social Science",
            "Commerce and Management",
            "Education",
            "Law",
            "Science and Technology"
        ],
        "undergraduate_programs": [
            {"name": "Bachelor of Computer Applications", "abbreviation": "BCA"},
            {"name": "Bachelor of Commerce", "abbreviation": "B.Com"},
            {"name": "Bachelor of Business Administration", "abbreviation": "BBA"}
        ],
        "postgraduate_programs": [
            {"name": "Master of Computer Applications", "abbreviation": "MCA"},
            {"name": "Master of Commerce", "abbreviation": "M.Com"},
            {"name": "MBA General Management"},
            {"name": "MBA (Dual Specialization)"}
        ],
        "mba_specializations": [
            "HR Management",
            "Marketing Management",
            "Financial Management",
            "Supply Chain Management",
            "Operations Management",
            "Data Science & Business Analytics",
            "Information Technology Business Management",
            "Entrepreneurship",
            "Executive Leadership",
            "Digital Marketing",
            "Small & Medium Business Management",
            "Hospital Administration",
            "Strategy And Leadership"
        ],
        "territorial_jurisdiction": {
            "original_districts": 9,
            "current_districts": 4,
            "district_names": ["Chamarajanagara", "Hassan", "Mandya", "Mysuru"],
            "reduced_due_to": [
                {"university": "Bangalore University", "year": 1964},
                {"university": "Mangalore University", "year": 1980},
                {"university": "Kuvempu University", "year": 1987}
            ]
        },
        "special_centers": [
            {
                "name": "Centre for Information Science and Technology",
                "abbreviation": "CIST",
                "location": "Senate Hall complex at Manasagangotri",
                "certification": "ISO 9001-2000 Certified",
                "description": "Non-formal education in Information Technology"
            },
            {
                "name": "Educational Multi-Media Research Centre",
                "abbreviation": "EMMRC",
                "established": 1996,
                "original_name": "Audio-Visual Research Centre (AVRC)",
                "name_changed": "August 2004",
                "description": "Produces educational videos for 24-hour educational television channel and Doordarshan"
            },
            {
                "name": "School of Planning and Architecture",
                "established": 2002,
                "courses": ["B.Arch", "B.Tech (Planning)", "M.Arch"],
                "approved_by": "Council of Architecture (COA), New Delhi"
            },
            {
                "name": "International School of Information Management",
                "abbreviation": "ISiM",
                "established": 2005,
                "partners": ["Three US universities", "Dalhousie University (Canada)", "IIIT Bangalore"]
            },
            {
                "name": "Third Sector Research Resource Centre",
                "abbreviation": "TSRRS",
                "established": 2004,
                "focus": "Interdisciplinary studies and research in civil society domain",
                "programs": [
                    "Diploma in management of non-profit organisations",
                    "Masters in management of non-profit organisations"
                ]
            },
            {
                "name": "Mysore University School of Justice",
                "abbreviation": "MUSJ",
                "description": "Department of Law incorporated into MUSJ",
                "programs": ["Five-year integrated law degree"]
            },
            {
                "name": "Centre for Proficiency Development and Placement Service",
                "abbreviation": "CPDPS",
                "services": ["Skill development", "Proficiency enhancement", "Personality development", "Placement liaison"]
            },
            {
                "name": "Centre for Competitive Examinations",
                "location": "EMMRC building",
                "exams_covered": ["IAS", "KAS", "IPS", "IFS", "NET", "SET", "Banking Services"]
            },
            {
                "name": "K-SET Centre",
                "full_name": "Karnataka State Eligibility Test Centre",
                "location": "Moulya Bhavan, behind Crawford Hall",
                "website": "www.kset.uni-mysore.ac.in",
                "purpose": "Conduct SET for Lecturership"
            },
            {
                "name": "International Centre",
                "location": "University College of Fine Arts at Manasagangotri",
                "services": [
                    "Admission guidance for foreign students",
                    "Eligibility assistance",
                    "VISA assistance",
                    "Residential permits",
                    "Bonafide certificates"
                ]
            },
            {
                "name": "Special Cell for SC/ST",
                "services": [
                    "Welfare of SC/ST students",
                    "Research fellowships",
                    "Special coaching for competitive exams",
                    "Computer training",
                    "Bridge courses",
                    "Library facility",
                    "Financial assistance"
                ]
            },
            {
                "name": "Women's Facilities Centre",
                "location": "Next to Department of Studies in Computer Science at Manasagangotri",
                "purpose": "Resting facility for women students commuting from different places"
            },
            {
                "name": "Dr. S. Radhakrishnan Centre for Philosophy and Indian Culture",
                "established_in_honor_of": "Dr. Sarvepalli Radhakrishnan"
            }
        ],
        "library": {
            "location": "Manasagangotri campus",
            "bound_journal_volumes": 75000,
            "reference_and_textbooks": 600000,
            "e_books": 18000,
            "e_journals": 7500,
            "total_books": 800000,
            "journal_titles": 2400,
            "journal_volumes": 100000,
            "services": [
                "In-house reference, consultation and home-lending",
                "Inter-library loan facility",
                "Textbook reference",
                "Textbook loan service",
                "Digital Information Resource Centre",
                "Centre for Information Resources for Competitive Examinations",
                "UGC-Infonet Journals access",
                "Assistive technologies for visually challenged",
                "Inflibnet services",
                "In-house photocopying facility"
            ],
            "timings": "8 AM to 8 PM on all working days"
        },
        "facilities": {
            "auditoria": [
                {"location": "Maharaja's College Centenary Building"},
                {"location": "University College of Fine Arts for Women"},
                {"location": "Humanities Block at Manasagangotri"},
                {"location": "Bahadur Institute of Management Studies (BIMS)"},
                {"location": "EMMRC, Nalwadi Krishnaraja Wadiyar auditorium, MGM"}
            ],
            "open_air_theatre": {
                "location": "Manasagangotri",
                "seating_capacity": 10000
            },
            "sports": {
                "infrastructure": [
                    "Cricket stadium",
                    "Tennis courts",
                    "Gymnasium",
                    "Swimming pool",
                    "Nalwadi Krishnaraja Wadiyar stadium",
                    "Gangotri Glades",
                    "Three Indoor stadiums"
                ],
                "managed_by": "Directorate of Physical Education"
            },
            "health_centers": [
                {"location": "Maharaja's College campus"},
                {"location": "Manasagangotri campus"}
            ],
            "banking": {
                "bank": "State Bank of India",
                "branches": [
                    {
                        "location": "Manasagangotri Campus",
                        "services": ["Banking", "ATM"]
                    },
                    {
                        "location": "Crawford Hall",
                        "services": ["Banking", "ATM"]
                    }
                ]
            },
            "postal_services": {
                "offices": [
                    {
                        "location": "Manasagangotri campus",
                        "services": ["Savings deposits", "Recurring deposits", "Telephone", "Speed Post"]
                    },
                    {
                        "location": "Crawford Hall",
                        "services": ["Savings deposits", "Recurring deposits", "Telephone", "Speed Post"]
                    }
                ]
            },
            "cafeteria": {
                "location": "Centrally located at Manasagangotri campus",
                "serves": ["Students", "Faculty", "General public"]
            },
            "internet": {
                "availability": ["Manasagangotri campus", "All postgraduate departments", "Library"],
                "types": ["Wired", "Wireless"],
                "managed_by": "ICD (Information Communication Division), Department of Studies in Computer Science"
            },
            "green_initiatives": [
                "Solar power in all street lamps",
                "Solar water heaters in all hostels",
                "Flower gardens and lawns",
                "Noise-free environment"
            ]
        },
        "hostels": {
            "men": [
                {"name": "DoS in Physical Education and Sports Sciences hostel", "location": "Mysuru"},
                {"name": "Postgraduate hostel for Men (Main Block)", "location": "Manasagangotri, Mysuru"},
                {"name": "Postgraduate hostel for Men (New Block)", "location": "Manasagangotri, Mysuru"},
                {"name": "Student Village", "location": "Manasagangotri, Mysuru"},
                {"name": "Postgraduate University hostel - II", "location": "Saraswathipuram, Mysuru"},
                {"name": "Postgraduate hostel (Men)", "location": "Hassan"},
                {"name": "Postgraduate hostel (Men)", "location": "Mandya"}
            ],
            "women": [
                {"name": "Postgraduate Ladies' hostel (New Block)", "location": "Manasagangotri, Mysuru"},
                {"name": "Postgraduate Ladies' hostel (New Wing)", "location": "Manasagangotri, Mysuru"},
                {"name": "Postgraduate Ladies' hostel (Old Wing)", "location": "Manasagangotri, Mysuru"},
                {"name": "Postgraduate hostel (Women)", "location": "Dr. B. R. Ambedkar Post-Graduate centre, Chamarajanagara"}
            ],
            "total_mens_hostels": 7,
            "total_womens_hostels": 4
        },
        "scholarships": [
            "State Government scholarships",
            "Central Government scholarships",
            "Subject scholarships",
            "Endowment scholarships",
            "Special scholarships for children of political sufferers",
            "Special scholarships for children of defence personnel",
            "Special scholarships for physically challenged",
            "Free studentships for economically weaker sections"
        ],
        "departments_with_recognition": {
            "dst_fist": [
                "Botany", "Bio-Technology", "Microbiology", "Physics", "Sericulture", "Statistics"
            ],
            "ugc_sap": [
                "Bio-Chemistry", "Bio-Technology", "Chemistry", "Commerce", "Computer Science", "Earth Science",
                "Food Science and Nutrition", "Journalism and Mass Communication", "Library and Information Science",
                "Mathematics", "Physics", "Political Science", "Statistics", "Zoology", "Kuvempu Institute of Kannada Studies"
            ]
        },
        "academic_system": {
            "scheme": "Flexible Choice-Based Credit System with Continuous Assessment Grading Pattern",
            "abbreviation": "CBCS-CAGP",
            "implemented_from": "2017-18"
        },
        "publications": {
            "division": "Prasaranga",
            "books_published": "1500+",
            "types": ["Various subjects", "Dictionaries", "Encyclopedias", "Monographs"]
        },
        "transport": {
            "service": "KSRTC city buses",
            "frequency": "20 minutes",
            "distance_from_central_bus_station": "6 km",
            "distance_from_railway_station": "3 km"
        },
        "policies": {
            "anti_ragging": "Zero tolerance - punishable offence, declaration required from all students",
            "no_smoking": "All postgraduate campuses declared No Smoking Areas"
        },
        "major_events": {
            "centenary_celebrations": {
                "year": "2015-16",
                "inauguration": {
                    "date": "2015-07-27",
                    "inaugurated_by": "Hon'ble President of India Shri Pranab Mukherjee"
                },
                "valedictory": {
                    "date": "2016-07-22",
                    "delivered_by": "Hon'ble Vice President of India Shri Hamid Ansari"
                },
                "nobel_laureates": 8
            },
            "103rd_indian_science_congress": {
                "year": 2016,
                "dates": "January 3-7, 2016",
                "theme": "Science and Technology for Indigenous Development in India",
                "inaugurated_by": "Hon'ble Prime Minister Shri Narendra Modi",
                "date_inaugurated": "2016-01-03",
                "total_delegates": 18528,
                "foreign_delegates": 600,
                "foreign_countries": ["USA", "Canada", "UK", "Australia", "Japan", "Korea", "France"],
                "nobel_laureates": 6,
                "field_medalists": 1,
                "bharatha_rathna_awardees": 1,
                "plenary_sessions": 28,
                "symposia": 25,
                "technical_sessions": 18
            },
            "40th_indian_social_science_congress": {
                "year": 2016,
                "dates": "December 19-23, 2016",
                "theme": "People's Health and Quality of Life in India",
                "organized_by": "Indian Academy of Social Sciences (IASS)",
                "inaugurated_by": "Prof. B. M. Hegde (President of ISSA, Allahabad)",
                "research_committees": 28,
                "thematic_panels": 21,
                "participants": "5000+ social scientists and delegates"
            }
        },
        "institution_of_excellence_facilities": {
            "grant_amount_crores": 100,
            "focus_area": "Bio-diversity, Bio-prospecting and Sustainable Development",
            "building": "Vijnana Bhavan",
            "facilities": ["NMR", "NGS", "LCMS", "XRD", "Imaging", "Cell culture"]
        },
        "upe_facilities": {
            "grant_amount_crores": 50,
            "duration_years": 5,
            "extended": True,
            "focused_areas": [
                {"name": "Processing, Characterization & Applications of Advanced Functional Materials", "number": 1},
                {"name": "Media and Social Development – A Case study of Karnataka", "number": 2}
            ],
            "facilities_established": [
                "High Performance Computing Environment (HPC)",
                "Adoption of Green Technology in the University Campus",
                "Centre for Education of Visually Challenged – Drushtee",
                "Multimedia Learning Resource Creation Centre (MLRCC)",
                "Earn While You Learn Scheme",
                "Workshops, Conferences and Seminars",
                "Centre for Proficiency Development",
                "Upgradation of Printing and Publication Units",
                "Books and Journals",
                "Sports and Games",
                "Strengthening of Department Laboratories and Hostels",
                "E-governance"
            ]
        },
        "online_programs": {
            "launched_during": "COVID pandemic",
            "approval": {
                "approved_by": "University Grants Commission (India)",
                "year": 2020
            },
            "initiative_started": 2014,
            "platform_partner": "University18",
            "significance": "One of the first public universities for online degree programs"
        },
        "notable_personalities": [
            {
                "name": "Dr. Sarvepalli Radhakrishnan",
                "years": "1888-1975",
                "role": "Professor of Philosophy",
                "tenure": "1918-1921",
                "achievements": [
                    "First Vice President of India (1952-1962)",
                    "Second President of India (1962-1967)"
                ]
            },
            {
                "name": "K. V. Puttappa (Kuvempu)",
                "role": "Former Vice-Chancellor",
                "tenure": "1956-1960",
                "achievements": [
                    "National poet",
                    "Jnanpith Award winner",
                    "First Jnanapeetha awardee",
                    "Named campus 'Manasagangotri'"
                ]
            },
            {"name": "T. S. Krishnamurthy", "achievement": "Former Chief Election Commissioner of India"},
            {"name": "R. K. Laxman", "profession": "Cartoonist"},
            {"name": "Devanur Mahadeva", "profession": "Writer"},
            {"name": "N. R. Narayana Murthy", "profession": "Billionaire"},
            {"name": "Nima Poovaya-Smith", "profession": "Museum curator, art historian and writer"},
            {"name": "M. Yamunacharya", "profession": "Philosopher, Writer, Gandhian"},
            {"name": "S. Srikanta Sastri", "profession": "Indian historian, Indologist, and polyglot"},
            {"name": "G. S. Shivarudrappa", "profession": "Writer"},
            {"name": "M. N. Venkatachaliah", "achievement": "Former Chief Justice of India"},
            {"name": "Priyadarshini", "profession": "Playback singer", "achievement": "First playback singer to receive Ph.D"},
            {"name": "Mysore Manjunath", "profession": "Indian Violinist"},
            {"name": "Avinash", "profession": "Actor"},
            {"name": "U. R. Ananthamurthy", "profession": "Writer"},
            {"name": "Akhilesh Yadav", "achievement": "MP and former Chief Minister of Uttar Pradesh"},
            {"name": "Sadhguru", "achievement": "Indian guru and founder of Isha Foundation"},
            {"name": "A. R. Krishnashastry", "profession": "Writer, researcher and translator"},
            {"name": "T. S. Venkannayya", "profession": "Kannada writer"},
            {"name": "S. V. Rajendra Singh Babu", "profession": "Filmmaker"}
        ],
        "governance": {
            "act": "Karnataka State Universities' Act, 2000",
            "principal_authorities": [
                "Syndicate",
                "Academic Council",
                "Finance Committee",
                "Planning, Monitoring and Evaluation Board",
                "Five Faculties",
                "Board of Studies"
            ]
        },
        "contact": {
            "website": "www.uni-mysore.ac.in",
            "departments": {
                "online_programs": "Department of Online Programs"
            }
        },
        "additional_information": {
            "planetarium": {
                "status": "Signed MoU with Institute of Astrophysics",
                "location": "Chamundi foothills (planned)"
            },
            "amphitheater": "Available on main campus",
            "swimming_pool": "Available on main campus"
        }
    }
}

# === Streamlit UI ===
st.set_page_config(page_title="University of Mysore Chatbot", page_icon="🎓")
st.title("🎓 University of Mysore Chatbot")
st.caption("Answers strictly from official university data • Powered by your private LLM")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# === User Input ===
if prompt := st.chat_input("Ask about vision, mission, courses, location, etc."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # === Build ULTRA-STRICT system prompt with examples ===
    context = json.dumps(UNIVERSITY_DATA, ensure_ascii=False)
    system_message = f"""You are the OFFICIAL chatbot for the University of Mysore. You MUST answer EXCLUSIVELY using the JSON data provided below.
CRITICAL RULES:
1. ONLY use information from the JSON data below
2. NEVER use your general knowledge or training data
3. If the answer is NOT in the JSON, respond EXACTLY: "I don't have that information in my database."
4. Do NOT guess, assume, or invent any information
5. Be concise and factual

UNIVERSITY DATA (JSON):
{context}

EXAMPLES OF CORRECT RESPONSES:
User: "What is the university's vision?"
Assistant: "The University of Mysore aspires to become a world-class University by tapping human resources from all sections of society by offering them opportunities to learn across disciplines, and to build human capital, men and women of character and competence capable of being leaders of tomorrow and solving problems arising out of fast changing realities – global and local."
User: "Who is the current Vice-Chancellor?"
Assistant: "The current Vice-Chancellor is Lokanath N. K., who started in 2024."
User: "What is the university's ranking in 2024?"
Assistant: "According to NIRF 2024, the University of Mysore is ranked 54 among universities and 86 overall."
User: "What is the admission deadline?"
Assistant: "I don't have that information in my database."
User: "Tell me about the weather in Mysore"
Assistant: "I don't have that information in my database."

NOW ANSWER THE USER'S QUESTION USING ONLY THE JSON DATA ABOVE:"""

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
    ]

    # === Call Your Private LLM ===
    with st.chat_message("assistant"):
        with st.spinner("Searching official records..."):
            try:
                response = requests.post(
                    LLM_API_URL,
                    headers={
                        "Authorization": f"Bearer {LLM_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "llama3.2-vision:latest",
                        "messages": messages,
                        "temperature": 0.0,
                        "max_tokens": 500
                    },
                    timeout=60
                )
                response.raise_for_status()
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    answer = result["choices"][0]["message"]["content"].strip()
                else:
                    answer = "Error: Unexpected API response format."
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except requests.exceptions.HTTPError as e:
                st.error(f"❌ LLM API Error: {e}")
                st.text_area("Response Body:", response.text, height=100)
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Network Error: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected Error: {e}")

# === Sidebar Info ===
with st.sidebar:
    st.header("ℹ️ How It Works")
    st.info(
        "✅ Answers come ONLY from embedded university data\n"
        "🔒 No external knowledge used\n"
        "🧠 Model: `llama3.2-vision:latest`\n"
        "⚡ Endpoint: your private Open WebUI\n"
        "🎯 Temperature: 0.0 (zero hallucination)"
    )
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()