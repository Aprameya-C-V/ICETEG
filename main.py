import streamlit as st

st.set_page_config(layout="wide")

# CSS for custom styling
st.markdown("""
    <style>
        .hero-section {
            background-color: #f0f2f6;
            padding: 50px;
            text-align: center;
        }
        .hero-title {
            font-size: 50px;
            font-weight: bold;
            color: #0047bb;
        }
        .hero-subtitle {
            font-size: 20px;
            color: #333;
        }
        .nav-bar {
            background-color: #0047bb;
            padding: 10px;
            text-align: center;
        }
        .nav-bar a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #777;
        }
    </style>
""", unsafe_allow_html=True)

# Adding logos
# Adding logos
col1, col2 = st.columns(2)
with col1:
    st.image("IEEEBengaluru.png", width=300)
with col2:
    st.image("JSSSTU.jpg", width=300)

# Hero section
st.markdown("""
    <div class="hero-section">
        <div class="hero-title">IEEE JSS STU ICETEG - 2025</div>
        <div class="hero-subtitle">International Conference on Emerging Technologies in Electronics and Green Energy</div>
    </div>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
    <div class="nav-bar">
        <a href="#overview">Overview</a>
        <a href="#registration-fees">Registration Fees</a>
        <a href="#topics-of-interest">Topics of Interest</a>
        <a href="#contact-information">Contact Information</a>
    </div>
""", unsafe_allow_html=True)

# Function to create section anchors
def section_anchor(anchor):
    st.markdown(f'<a name="{anchor}"></a>', unsafe_allow_html=True)

# Overview section
section_anchor("overview")
st.header("Overview")
st.write("""
The IEEE JSS STU International Conference on “Emerging Technologies in Electronics and Green Energy 2025” (IEEE JSS STU ICETEG - 2025) is planned to be organized on 21st and 22nd February 2025 by JSS S&TU (SJCE), JSS Technical Institutions Campus, Mysuru, Karnataka, India. 

IEEE JSS STU ICETEG – 2025 is a premier international conference technically sponsored by IEEE Bangalore Section, organized by three circuit branch departments: Electronics and Communication, Electronics and Instrumentation, and Electronics and Electrical Engineering.

The theme for ICETEG – 2025 is to promote the most upcoming innovations and advancements in various fields of engineering and technology, bringing together academia and industry. This conference provides an excellent opportunity for faculty members, research scholars, students, and industry delegates to present, demonstrate, and discuss innovative research developments in the fields of electronics, communication, green energy, computing technology, and biomedical applications.
""")

section_anchor("registration-fees")
st.header("Registration Fees")
st.write("""
| Category                   | Early Bird Registration |                   | Regular Registration |                    | Late Registration  |                    |
|----------------------------|-------------------------|-------------------|----------------------|--------------------|--------------------|--------------------|
|                            | Indian Author in INR    | Foreign Author in USD | Indian Author in INR | Foreign Author in USD | Indian Author in INR | Foreign Author in USD |
| IEEE Member                | 7000                    | 160               | 8000                 | 200                | 9500               | 220                |
| Non-IEEE Member            | 8500                    | 200               | 10000                | 220                | 12000              | 240                |
| Co-author/listener/Attendee| 5500                    | 65                | 4000                 | 75                 | 4500               | 85                 |
| Extra Certificate          | 800                     | 15                | 1000                 | 25                 | 1500               | 30                 |

Above registration fee is excluding GST (18%).
""")

# Topics of Interest section
section_anchor("topics-of-interest")
st.header("Topics of Interest")
st.write("""
### Electronics and Communication:
- Nanotechnology
- Nanomaterials
- Nano Electronics
- Nano dielectric devices and Composites
- Microelectronics
- VLSI design
- FPGA Based Systems
- Smart Electronics Systems/ Smart sensors
- Low Power VLSI Circuits
- Mixed Mode VLSI
- VLSI Verification and Testing
- Electronic/electrical Applications
- Electronics System Design
- Mechatronics Aerospace Electronics/ Avionics
- MEMS/NEMS
- Computational Electromagnetics
- Photonic/Opto-Electronic Structures/Devices
- Nanophotonics
- Consumer Electronics
- Display Technologies 
- Power Electronics/Power Systems
- Ad hoc Mesh and Sensor Networks/ Multimedia Networks
- Cognitive Radio
- Delay Tolerance/Communication Networks/Home LAN Body and Personal Area Networks
- Internet of Things
- Medium Access Control
- Modulation and Coding
- Network Architectures and Middleware
- Network Coding Fault -Management Reliability
- QoS in Networks
- Network Pricing and Billing
- Network Security Monitoring and Protection
- Networking in Military and Space Applications
- 5G Technology Networks
- Optical and Photonic Networks
- Peer-to-Peer and Overlay Networking
- Error Control Coding
- Spread Spectrum Communication
- OFDM and MIMO
- Antenna Filters Waveguides
- Computational Electromagnetics
- Cluster Cloud and Grid Computing
- Content Distribution Networks
- Distributed Multimedia Systems
- Web and Gaming Applications
- Storage Area Networks
- Data Compression and Encryption
- Cryptography and Secured Systems
- Tools and Techniques for Network Simulation and Performance Measurement

### Green Energy, Computing Technology, and Biomedical Applications:
- Green Technologies
- Hybrid vehicles
- Automotive electronics
- Mechatronics
- Non-linear control systems
- Medical signal processing
- Signal processing/ Digital image processing
- Biomedical instrumentation/ Biomedical image processing
- Robotics
- Machine learning
- Artificial intelligence and expert systems
- Embedded systems
- Digital design, analog design, and embedded systems design
- Media technologies
- Microprocessor-based technologies
- DSP architecture
- Speech processors
- Home/office automation
- Performance modelling and computing system
- Computer architecture/ Interface architecture
- Parallel and distributed algorithms
- Smart grids, data centers
- Big data analytics
- Computational intelligence and applications
""")

# Contact Information section
section_anchor("contact-information")
st.header("Contact Information")
st.write("""
### Conveners
- Dr. U.B. Mahadevaswamy
- Dr. K. Umarani
- Dr. M.H. Sidram

### Conference Coordinators
- Dr. Sudarshan Patil Kulkarni
- Dr. M.G. Veena
- Dr. Anitha S. Prasad
- Prof. Supreetha M
- Prof. Yashwanth S.D
- Dr. Neethi M
- Dr. Mohan N
- Dr. Mallikarjunaswamy M.S
- Dr. Nanda S
""")

