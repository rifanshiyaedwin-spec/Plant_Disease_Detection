🌿 PlantaSanitus – Smart Agriculture Platform
AI-Powered Agricultural Decision Support & Agro-Medicine E-Commerce Ecosystem

📌 1. Project Overview

PlantaSanitus is an AI-enabled Smart Agriculture Platform designed to help farmers identify plant diseases, determine disease severity, analyze soil health, monitor weather conditions, obtain treatment recommendations, and purchase agro-medicines through an integrated marketplace.

The platform combines:

Artificial Intelligence + Computer Vision + Explainable AI + Soil Analytics + Weather Intelligence + E-Commerce + Farm Management + Multilingual Assistance + Security

It is developed as a Final Year Computer Science and Engineering Capstone Project.

🛠️ Core Technologies
Category	Technology
Programming Language	Python
Web Framework	Flask
Machine Learning	TensorFlow / Keras
Deep Learning	MobileNetV2
Computer Vision	OpenCV
Image Processing	Pillow, NumPy
Database	SQLite
Authentication	Flask Sessions + Werkzeug
Frontend	HTML, CSS, JavaScript
Visualization	Matplotlib
🎯 2. Main Objective

The primary objective of PlantaSanitus is to provide farmers with a single centralized agricultural assistant instead of requiring multiple applications for different agricultural activities.

🔄 Overall Workflow
Farmer
   ↓
Agricultural Information
   ↓
AI / Analytics
   ↓
Diagnosis & Recommendations
   ↓
Treatment Selection
   ↓
Agro-Medicine Marketplace
   ↓
Payment
   ↓
Order Tracking
   ↓
Follow-up / History
🌱 Example: Disease Diagnosis

A farmer can upload photographs of an affected plant leaf and receive:

Crop
Detected Disease
Scientific Name
Confidence Score
Disease Severity
Treatment Urgency
Estimated Recovery Time
Symptoms
Possible Cause
Organic Treatment
Chemical Treatment
Preventive Measures
XAI Highlighted Regions
👥 3. Multi-Role Authentication System

PlantaSanitus provides three major user roles:

Role	Primary Responsibility
👨‍🌾 Farmer	Agricultural analysis and purchasing
🏪 Agro-Medicine Seller	Product and inventory management
🛡️ Administrator	System administration and auditing
👨‍🌾 Farmer

The farmer can:

Perform plant disease scans
Analyze soil health
View weather information
Manage farms and fields
View previous disease scans
Purchase agro-medicines
Track orders
Use AgriBot
Participate in the community forum
🏪 Agro-Medicine Seller

The seller can:

Add agro-medicine products
Specify product type
Define target diseases
Set price and stock
Add descriptions
Add usage instructions
Manage marketplace inventory
🛡️ Administrator

The administrator manages:

Users
Disease scans
Marketplace products
System security information
Auditing activities
🤖 4. AI Plant Disease Detection

Disease detection is one of the core modules of PlantaSanitus.

The platform supports uploading up to three leaf images for multi-image analysis.

🔬 Diagnostic Output
Leaf Image(s)
      ↓
Image Processing
      ↓
Disease Classification
      ↓
Disease Information
      ↓
Severity Analysis
      ↓
Treatment Recommendation
      ↓
Preventive Guidance

The system is designed to provide:

Disease identification
Confidence score
Disease severity
Treatment urgency
Recovery time
Scientific name
Symptoms
Cause
Organic treatment
Chemical treatment
Prevention
XAI visual regions
🧠 5. Machine Learning Architecture

The training pipeline follows:

PlantVillage Dataset
        ↓
Data Augmentation
        ↓
MobileNetV2
        ↓
Global Average Pooling
        ↓
Dropout
        ↓
Softmax Classification
⚙️ Training Configuration
Parameter	Configuration
Dataset	PlantVillage
Base Model	MobileNetV2
Pretrained Weights	ImageNet
Input Size	224 × 224
Validation Split	20%
Optimizer	Adam
Loss Function	Sparse Categorical Cross-Entropy
Metric	Accuracy
Output Model	plant_disease_model.h5
🔄 Data Augmentation

The training process uses:

Horizontal / vertical flipping
Rotation
Zoom
Contrast adjustment

Additional training techniques include:

Model checkpointing
Early stopping
Learning-rate reduction
⚠️ Important Implementation Note

There is an important difference between the training architecture and the current integrated prediction implementation.

train.py genuinely defines and trains the MobileNetV2 model. However, the current predict.py inference implementation does not load plant_disease_model.h5 for TensorFlow inference. Instead, the current implementation contains demonstration-oriented prediction logic.

🎓 Recommended Viva Explanation

“PlantaSanitus incorporates a MobileNetV2 transfer-learning pipeline for plant disease classification, while the currently integrated inference module contains a demonstration-oriented prediction implementation.”

This is the most technically accurate way to present the system.

🔍 6. Explainable AI – XAI

PlantaSanitus attempts to explain where the visible symptoms are located on the plant leaf, rather than simply displaying a disease name.

🖼️ XAI Processing
Leaf Image
    ↓
OpenCV Processing
    ↓
Symptom Region Detection
    ↓
Bounding Boxes
    ↓
Highlighted Leaf Regions
    ↓
Human-Readable Explanation

Possible explanations include:

Leaf chlorosis and yellowing
Concentric brown necrotic spots
Edge scorching
Cuticle decay

This improves the interpretability and transparency of the diagnosis.

📚 7. Plant Disease Knowledge Base

The disease_info.py module contains a structured knowledge base covering 38 PlantVillage crop/disease classes according to the project documentation.

Each disease entry may contain:

Information	Description
🌱 Crop	Affected crop
🦠 Disease	Disease name
🔬 Scientific Name	Scientific classification
📊 Severity	Severity information
🩺 Symptoms	Observable symptoms
🧬 Cause	Possible cause
🌿 Organic Treatment	Organic treatment
🧪 Chemical Treatment	Chemical treatment
🛡️ Prevention	Preventive measures

This knowledge base converts a predicted disease class into practical agricultural guidance.

🚦 8. Disease Severity & Treatment Priority

The platform categorizes disease severity into:

🟢 Mild

Early-stage infection requiring monitoring and basic treatment.

🟡 Moderate

Visible infection requiring timely treatment.

🔴 Severe

Advanced infection requiring immediate attention.

The system also generates:

Severity percentage
Treatment urgency
Estimated recovery period

Therefore:

Disease Detection
       ↓
Severity Assessment
       ↓
Treatment Priority
       ↓
Recommended Action
🧪 9. Agro-Chemical Dosage Calculator

The dosage calculator helps farmers estimate treatment requirements based on field size in acres.

📐 Inputs
Field area
Recommended chemical/fungicide
📊 Outputs
Required chemical quantity
Required water quantity
Spraying schedule

Example schedule:

Day 1  → Initial Application
   ↓
Day 7  → Follow-up Application
   ↓
Day 14 → Final / Preventive Application

Note: Actual chemical application should always follow the product label and applicable agricultural guidance.

🌱 10. Soil Health Analysis

The soil_service.py module analyzes:

pH
Nitrogen
Phosphorus
Potassium
Field area
🧪 Soil Classification
             Soil Input
                 ↓
        ┌────────┼────────┐
        ↓        ↓        ↓
     Acidic    Optimal   Alkaline

The system also checks nutrient deficiencies and generates fertilizer or organic amendment recommendations.

🌦️ 11. Weather Intelligence

PlantaSanitus integrates weather intelligence to support agricultural decision-making.

🌤️ Weather Parameters
Temperature
Humidity
Wind speed
Rain outlook
Disease-risk forecasting
🌧️ Agricultural Use

Weather information can help farmers understand environmental conditions that may increase the risk of diseases, particularly fungal infections.

Weather Conditions
       ↓
Environmental Analysis
       ↓
Disease Risk
       ↓
Farmer Advisory
🛒 12. Agro-Medicine E-Commerce Marketplace

One of the strongest features of PlantaSanitus is the connection between AI diagnosis and agro-medicine purchasing.

🛍️ Marketplace Features
Organic products
Chemical products
Product descriptions
Target diseases
Pricing
Stock management
Usage instructions
Product images
Shopping cart
Checkout
Order tracking
🔗 Complete Treatment Ecosystem
Disease Detection
       ↓
Treatment Recommendation
       ↓
Recommended Product
       ↓
Shopping Cart
       ↓
Payment
       ↓
Order Processing
       ↓
Delivery
📱 13. QR-Based Product Guidance

Each agro-medicine product can have an associated QR code.

📲 QR Workflow
Physical Product
      ↓
Scan QR Code
      ↓
Product Information
      ↓
Usage Instructions
      ↓
Treatment Guidance

This feature can be particularly useful when QR codes are printed on physical product packaging.

📦 14. Shopping & Order Management

The platform supports a complete order lifecycle.

🧾 Order Information
User
Total amount
Payment method
Payment status
Order status
Delivery date
Shipping address
🚚 Order Lifecycle
🛍️ Order Placed
        ↓
⚙️ Processing
        ↓
🚚 In Transit
        ↓
📦 Delivered

Order cancellation is also supported.

💳 15. Secured Payment Gateway

The project contains a dedicated payment_service.py.

💰 Supported Methods
Payment Method	Validation
UPI	VPA format validation
Card	Luhn checksum
COD	Cash on Delivery

The payment service generates:

Transaction ID
Cryptographic transaction signature
Masked payment information
⚠️ Important

The payment gateway is a simulated academic payment system and is not a real integration with a bank or payment provider.

🤖 16. AgriBot AI Assistant

AgriBot AI acts as a multilingual agricultural assistant.

💬 Capabilities

It can assist with:

Plant disease questions
Treatment information
Dosage guidance
Organic remedies
Preventive measures
🌐 Supported Languages
English
Tamil
Hindi
Telugu
Kannada
🧠 Example Knowledge

The implementation contains knowledge related to:

Early Blight
Late Blight
Apple Scab
Common Rust
Neem Oil
Copper Fungicide
🚜 17. Multi-Farm & Field Management

PlantaSanitus supports farm-level organization through dedicated Farm and Field entities.

🌾 Farm Information
Farm name
Area in acres
Crop type
Location
Owner
🌱 Field Information
Field name
Status
Notes
📊 Field Status
🟢 Healthy
🟠 Diseased
🟤 Harvested

This allows PlantaSanitus to evolve from a simple disease detector into a farm management platform.

👨‍🌾 18. Farmer Community Forum

The community module allows farmers to interact and share agricultural knowledge.

It supports:

Forum posts
Replies
User association
Images
Expert verification

The is_expert_verified field allows posts to be identified as expert-verified content.

🏛️ 19. Government Schemes & Educational Resources

The platform provides dedicated resources for:

🏛️ Government Schemes
Crop insurance
Agricultural subsidies
Organic certification
Other agricultural support programs
🎓 Educational Resources
Agricultural videos
Disease guides
Educational materials

The Flask application exposes:

/schemes
/videos
/guide
📊 20. Disease History & Reports

Each diagnostic scan can be stored for future reference.

🗂️ Scan Information
User
Image
Crop
Disease
Confidence
Severity
Urgency
Recovery time
Scientific name
XAI highlights
Timestamp
📈 History Workflow
Disease Scan
     ↓
Database Storage
     ↓
Historical Records
     ↓
Statistics
     ↓
Reports

This allows farmers to track previous disease incidents.

🗄️ 21. Database Architecture

PlantaSanitus uses SQLite as its primary database.

🧩 Core Database Relationships
                         USERS
                           │
          ┌────────────────┼─────────────────┐
          ↓                ↓                 ↓
        Farms          Disease Scans      Soil Tests
          │
        Fields




       SELLERS
          │
       Products
          │
        Orders
          │
      Order Items




        USERS
          │
    ┌─────┼──────────────┐
    ↓     ↓              ↓
 Reviews Forum Posts  Notifications
              │
         Forum Replies

The database manager handles:

Users
Roles
Farms
Fields
Disease scans
Soil tests
Products
Orders
Reviews
Forum posts
Notifications
Audits
🔐 22. Security Architecture

Security is designed around the CIA Triad.

🔒 Confidentiality
Password hashing
HTTP-only session cookies
Role-based authorization
Payment credential masking
🛡️ Integrity
HTML escaping
XSS protection
File-upload security
Path-traversal protection
SQLite transaction integrity
Luhn verification
HMAC transaction signatures
⚡ Availability
File-upload size restrictions
OpenCV fallback processing
Application-level operational checks
🔐 Security Model
                 SECURITY
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
 Confidentiality  Integrity  Availability
        │           │           │
 Passwords       XSS         Upload Limits
 Sessions        HMAC        Operational
 Authorization   Validation  Protection
🏗️ 23. Overall System Architecture
                         🌿 PLANTASANITUS
                               │
                               ▼
                     ┌──────────────────┐
                     │   FLASK SERVER   │
                     └────────┬─────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
      👨‍🌾 FARMER          🏪 SELLER          🛡️ ADMIN
          │                   │                   │
    ┌─────┼─────┐             │            ┌─────┼─────┐
    │     │     │             │            │     │     │
 Disease Soil Weather      Products       Users Scans Products
    │     │     │             │
    └─────┼─────┘             │
          │                   │
          ▼                   ▼
    ┌────────────────────────────────────────┐
    │          AI / ANALYTICS LAYER          │
    │                                        │
    │  • MobileNetV2                         │
    │  • Computer Vision                     │
    │  • Explainable AI                      │
    │  • Disease Knowledge Base              │
    │  • Soil Analytics                      │
    │  • Weather Intelligence                │
    │  • AgriBot AI                          │
    └────────────────────┬───────────────────┘
                         │
                         ▼
                ┌───────────────────┐
                │   SQLite DATABASE │
                ├───────────────────┤
                │ Users             │
                │ Farms / Fields    │
                │ Disease Scans     │
                │ Soil Tests        │
                │ Products          │
                │ Orders            │
                │ Reviews           │
                │ Forum             │
                │ Notifications     │
                └─────────┬─────────┘
                          │
                          ▼
                 🌾 AGRICULTURAL
                  DECISION SUPPORT
💻 24. Technology Stack
Layer	Technology
Language	Python
Web Framework	Flask
Machine Learning	TensorFlow / Keras
Deep Learning Model	MobileNetV2
Dataset	PlantVillage
Computer Vision	OpenCV
Image Processing	Pillow, NumPy
Database	SQLite
Authentication	Werkzeug + Flask Sessions
Security	XSS Protection, Path Protection, Luhn, HMAC
Payment	Simulated UPI / Card / COD
QR	QR Generation Service
Frontend	HTML / CSS / JavaScript
Visualization	Matplotlib
⭐ 25. What Makes PlantaSanitus Different?

A conventional plant disease detection project generally follows:

📷 Leaf Image
      ↓
🦠 Disease Name

PlantaSanitus extends this concept into a complete agricultural ecosystem:

📷 Leaf Image
      ↓
🦠 Disease Detection
      ↓
📊 Severity Analysis
      ↓
🚨 Treatment Urgency
      ↓
💊 Treatment Recommendation
      ↓
🧪 Dosage Guidance
      ↓
🛒 Agro-Medicine Product
      ↓
💳 Payment
      ↓
📦 Delivery
      ↓
📈 Follow-up & History

Alongside this, the platform integrates:

🌱 Soil Analytics
        +
🌦️ Weather Intelligence
        +
🚜 Farm Management
        +
🤖 AgriBot
        +
👨‍🌾 Farmer Community
        +
📚 Educational Resources
🏆 Core Innovation

PlantaSanitus transforms plant disease detection into an end-to-end agricultural decision-support ecosystem.

🎤 26. Short Project Description for Viva

PlantaSanitus is an AI-powered Smart Agriculture Platform developed to provide farmers with an integrated solution for plant disease diagnosis and agricultural decision support. The system combines computer vision, explainable AI, soil health analysis, weather intelligence, agro-medicine recommendations, farm management, and an e-commerce marketplace into a single web application. Farmers can upload leaf images for disease analysis, obtain information about symptoms, severity, treatment and prevention, analyze soil NPK and pH values, and receive agricultural guidance through the multilingual AgriBot assistant. The platform also allows farmers to purchase recommended agro-medicines through a marketplace with QR-based product guidance, simulated digital payments and order tracking. Separate Farmer, Seller and Admin roles provide role-based access and management capabilities. SQLite is used for persistent storage, while Flask provides the web application layer. Security mechanisms based on confidentiality, integrity and availability are incorporated throughout the system.

🌿 27. One-Line Definition

PlantaSanitus is an integrated AI-driven Smart Agriculture Platform that connects plant disease diagnosis, agricultural decision support, treatment guidance, soil and weather analytics, farmer assistance, farm management, and agro-medicine e-commerce in one unified ecosystem.

✨ Recommended Visual Style for Your Final Report

For the actual document, I recommend this hierarchy:

┌─────────────────────────────────────────────┐
│          🌿 PLANTASANITUS                   │
│     Smart Agriculture Platform              │
└─────────────────────────────────────────────┘


1. PROJECT OVERVIEW
   └── 1.1 Introduction
   └── 1.2 Objective
   └── 1.3 Key Features


2. SYSTEM MODULES
   └── 2.1 Authentication
   └── 2.2 Disease Detection
   └── 2.3 XAI
   └── 2.4 Soil Analysis
   └── 2.5 Weather Intelligence
   └── 2.6 Marketplace


3. AI & MACHINE LEARNING
   └── 3.1 Dataset
   └── 3.2 Model Architecture
   └── 3.3 Training
   └── 3.4 Prediction
   └── 3.5 Explainable AI


4. E-COMMERCE
   └── 4.1 Products
   └── 4.2 Cart
   └── 4.3 Payment
   └── 4.4 Orders
   └── 4.5 QR Guidance


5. FARM MANAGEMENT
   └── 5.1 Farms
   └── 5.2 Fields
   └── 5.3 Soil
   └── 5.4 Weather


6. SUPPORT SYSTEMS
   └── 6.1 AgriBot
   └── 6.2 Community
   └── 6.3 Schemes
   └── 6.4 Educational Resources


7. DATABASE & SECURITY
   └── 7.1 Database Architecture
   └── 7.2 Security Architecture


8. SYSTEM ARCHITECTURE


9. TECHNOLOGY STACK


10. INNOVATION & UNIQUENESS


11. CONCLUSION
