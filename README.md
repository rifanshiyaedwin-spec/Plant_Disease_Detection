PlantaSanitus 🌿 – Smart Agriculture Platform

1. Project Overview

PlantaSanitus is an AI-enabled Smart Agriculture Platform designed to assist farmers in identifying plant diseases, understanding disease severity, analyzing soil health, monitoring agricultural conditions, obtaining treatment recommendations, and purchasing agro-medicines through an integrated marketplace.

The project combines Artificial Intelligence, Computer Vision, Explainable AI (XAI), soil analytics, weather intelligence, e-commerce, multilingual assistance, farm management, and security mechanisms into a single web-based platform. The README identifies it as a Final Year Computer Science and Engineering Capstone Project.

The system is implemented primarily using Python, Flask, TensorFlow, OpenCV, NumPy, Pillow, and SQLite. The dependency file confirms Flask, TensorFlow, OpenCV, Pillow, NumPy, Werkzeug and Matplotlib as core technologies.

2. Main Objective

The primary objective of PlantaSanitus is to provide farmers with a centralized digital agricultural assistant rather than requiring them to use separate applications for disease detection, soil analysis, weather information, treatment guidance, and agricultural product purchasing.

The platform follows a basic workflow:

Farmer → Upload/Enter Agricultural Information → AI/Analytics → Diagnosis & Recommendations → Treatment/Product Selection → Purchase → Order Tracking

For example, a farmer can upload photographs of an affected plant leaf. The system processes the images and produces information such as:

Crop
Detected disease
Scientific name
Confidence
Disease severity
Treatment urgency
Estimated recovery time
Symptoms
Possible cause
Organic treatment
Chemical treatment
Preventive measures
XAI-highlighted regions

The prediction result is also stored in the database for future history and reporting.

3. Major Modules of PlantaSanitus
3.1 Multi-Role Authentication System

PlantaSanitus provides three major user roles:

Farmer
Agro-Medicine Seller
Administrator

Users can register and log in, and their role determines which dashboard and functionality they can access. The application uses password hashing and session-based authentication.

Farmer

The farmer can:

Perform plant disease scans
Analyze soil
View weather information
Manage farms and fields
View previous disease scans
Purchase agro-medicines
Track orders
Use AgriBot
Participate in the community forum
Seller

The seller can:

Add agro-medicine products
Specify product type
Specify target disease
Set price and stock
Add descriptions
Add usage instructions
Manage marketplace inventory
Administrator

The administrator provides centralized management and auditing of:

Users
Disease scans
Marketplace products
System security information

The role structure is also reflected in the database schema, where users are explicitly associated with farmer, seller, or admin roles.

4. AI Plant Disease Detection

This is one of the most important components of PlantaSanitus.

The platform supports uploading up to three leaf images for a multi-image diagnostic process. The application saves the uploaded images and sends them to the disease prediction engine.

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

The database stores these diagnostic results, including confidence, severity percentage, urgency, recovery time, scientific name, and XAI coordinates.

5. Machine Learning Architecture

The project contains a dedicated train.py module for developing the plant-disease classification model.

The training pipeline uses:

PlantVillage Dataset → Data Augmentation → MobileNetV2 → Global Average Pooling → Dropout → Softmax Classification

The training process uses a 20% validation split, 224×224 image input, and data augmentation including:

Horizontal/vertical flipping
Rotation
Zoom
Contrast adjustment

The project uses MobileNetV2 transfer learning with ImageNet weights as its base feature extractor.

The model is compiled using:

Adam optimizer
Sparse categorical cross-entropy loss
Accuracy metric

It also uses:

Model checkpointing
Early stopping
Learning-rate reduction

and saves the trained model as plant_disease_model.h5.

Important implementation observation

There is an important distinction between the intended ML architecture and the current prediction implementation.

train.py genuinely defines and trains a MobileNetV2 model. However, the current predict.py inference function does not load plant_disease_model.h5 and perform TensorFlow inference. Instead, its current demonstration logic determines the label partly from the uploaded filename and generates confidence/severity values programmatically.

So, for a project presentation, it would be accurate to say:

“PlantaSanitus incorporates a MobileNetV2 transfer-learning pipeline for plant disease classification, while the current integrated inference module contains a demonstration-oriented prediction implementation.”

This distinction is important if you are presenting the project to an examiner.

6. Explainable AI (XAI)

PlantaSanitus does not simply return a disease name. It attempts to explain where the visible symptoms are located on the leaf.

The XAI module uses OpenCV image processing to identify regions corresponding to potential necrotic areas and generates bounding-box coordinates.

It also produces human-readable explanations such as:

Leaf chlorosis and yellowing
Concentric brown necrotic spots
Edge scorching
Cuticle decay

These regions can subsequently be displayed as highlighted areas in the interface.

This makes the system more interpretable than a simple black-box disease classifier.

7. Plant Disease Knowledge Base

The disease_info.py file contains a structured plant disease knowledge base covering 38 PlantVillage crop/disease classes according to its documentation.

For each disease, the knowledge base can contain:

Crop
Disease name
Scientific name
Status
Severity
Symptoms
Cause
Organic treatment
Chemical treatment
Prevention

For example, the Apple Scab entry contains symptoms, fungal cause, organic treatment, chemical treatment, and preventive measures.

This knowledge base allows the AI diagnosis module to convert a predicted disease class into meaningful agricultural guidance.

8. Disease Severity and Treatment Priority

After determining the disease information, PlantaSanitus generates a severity assessment.

The system categorizes disease conditions into levels such as:

🟢 Mild
🟡 Moderate
🔴 Severe

It additionally generates:

Severity percentage
Treatment urgency
Estimated recovery period

For example, the prediction module associates different severity ranges with different urgency levels and recovery periods.

This helps transform disease detection into a more practical decision-support system.

9. Agro-Chemical Dosage Calculator

The platform also includes a dosage calculation feature.

According to the project documentation, the farmer can enter the field size in acres, after which the system calculates:

Required chemical/fungicide quantity
Required water quantity
Spraying schedule

The documented example includes a 2-acre calculation and a Day 1 → Day 7 → Day 14 spraying schedule.

This is intended to help farmers translate treatment recommendations into field-level application quantities.

10. Soil Health Analysis

The soil_service.py module provides a soil-health recommendation engine based on:

pH
Nitrogen
Phosphorus
Potassium
Field area

The system determines whether the soil is:

Acidic
Optimal
Alkaline

and checks nutrient deficiencies.

For example, the implementation evaluates nitrogen, phosphorus and potassium against threshold values and generates fertilizer or organic amendment recommendations.

The application exposes this through a dedicated /soil interface where the user enters soil parameters and field area.

11. Weather Intelligence

PlantaSanitus also integrates a weather intelligence component.

The project documentation describes weather information including:

Temperature
Humidity
Wind speed
Rain outlook
Disease-risk forecasting

It is designed to help farmers understand environmental conditions that may increase the probability of fungal diseases.

The main Flask application imports the weather service and uses weather information on the platform's main and farmer dashboard views.

12. Agro-Medicine E-Commerce Marketplace

One of the distinctive aspects of PlantaSanitus is that it connects disease diagnosis with agricultural product purchasing.

The marketplace supports:

Organic products
Chemical products
Product descriptions
Target diseases
Prices
Stock management
Usage instructions
Product images
Shopping cart
Checkout
Order tracking

The database has dedicated product, order and order-item tables.

This creates a complete flow:

Disease Detection → Treatment Recommendation → Product Selection → Purchase

13. QR-Based Product Guidance

The project includes a QR service for agro-medicines.

Each product can have a QR code that directs the user to its product/instruction page. The product detail route generates QR information and displays it with the product's usage guide.

This can be useful on physical product packaging because a farmer could scan the QR code and access:

Product information
Usage instructions
Related guidance
14. Shopping and Order Management

The system supports a complete order workflow.

Orders contain:

User
Total amount
Payment method
Payment status
Order status
Delivery date
Shipping address

Order statuses include:

Order Placed → Processing → In Transit → Delivered

with cancellation also supported.

The database also deducts product stock when an order is created.

15. Secured Payment Gateway

The project contains a dedicated payment_service.py.

It supports:

UPI

The system validates the UPI Virtual Payment Address format.

Card

The system validates card numbers using the Luhn checksum algorithm.

Cash on Delivery

COD is also supported.

The payment service generates a transaction ID and cryptographic transaction signature and masks account information rather than returning complete payment credentials.

The application integrates this service into its checkout process.

Important: based on the source code, this is a simulated/academic payment gateway, not an integration with a real bank or payment provider.

16. AgriBot AI Assistant

PlantaSanitus includes AgriBot AI, a multilingual agricultural assistant.

It is designed to help farmers with:

Plant disease questions
Treatment information
Dosage guidance
Organic remedies
Preventive measures

The current implementation contains knowledge for diseases/products such as:

Early Blight
Late Blight
Apple Scab
Common Rust
Neem Oil
Copper Fungicide

and provides multilingual responses.

The supported languages in the implementation include:

English
Tamil
Hindi
Telugu
Kannada

The chatbot API receives the user's question and language and returns the generated response along with audio-synthesis availability metadata.

17. Multi-Farm and Field Management

The database architecture includes dedicated entities for farms and fields.

A farm stores:

Farm name
Area in acres
Crop type
Location
Owner

Individual fields can contain:

Field name
Status
Notes

Field status can represent conditions such as:

Healthy
Diseased
Harvested

This allows the platform to move beyond individual disease scans toward farm-level management.

18. Farmer Community Forum

PlantaSanitus also provides a community-oriented component.

The database supports:

Forum posts
Replies
User association
Images
Expert verification

The is_expert_verified field allows posts to be identified as expert verified.

The application also exposes a dedicated forum interface.

19. Government Schemes and Educational Resources

The application contains dedicated sections for:

Government agricultural schemes
Agricultural videos
Disease guides
Educational resources

The Flask application exposes /schemes, /videos, and /guide routes.

The README specifically describes agricultural scheme resources such as crop insurance, subsidies and organic certification guidance.

20. Disease History and Reports

Every diagnostic scan can be stored in the database.

The scan table records:

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

This enables users to view their previous scans and statistics.

The application also provides a history page and a report-generation route for individual scans.

21. Database Architecture

The project uses SQLite as its database.

The database contains tables for:

Users
   ↓
Farms
   ↓
Fields


Users
   ↓
Disease Scans


Users
   ↓
Soil Tests


Sellers
   ↓
Products
   ↓
Orders
   ↓
Order Items


Users
   ↓
Reviews


Users
   ↓
Forum Posts
   ↓
Forum Replies


Users
   ↓
Notifications

The database module describes itself as the master database manager for users, roles, scans, farms, fields, soil tests, marketplace products, orders, reviews, forum posts, notifications and audits.

22. Security Architecture

Security is explicitly incorporated into the project through a CIA Triad approach:

Confidentiality

The implementation documents:

Password hashing
HTTP-only session cookies
Role/user-based authorization
Payment credential masking/tokenization
Integrity

It includes:

HTML escaping
XSS protection
File upload security
Path traversal protection
SQLite transaction integrity
Luhn payment verification
HMAC transaction signatures
Availability

The project includes:

File upload size restrictions
OpenCV fallback processing
Application-level operational checks

These security mechanisms are implemented in security_service.py.

23. Overall System Architecture

A simplified architecture of your project can be represented as:

                         PLANTASANITUS 🌿
                               │
                    ┌──────────┴──────────┐
                    │   Flask Web Server  │
                    └──────────┬──────────┘
                               │
       ┌───────────────────────┼────────────────────────┐
       │                       │                        │
       ▼                       ▼                        ▼
   FARMER                  SELLER                    ADMIN
       │                       │                        │
       ├── Disease Scan       ├── Products             ├── Users
       ├── Soil Analysis      ├── Inventory             ├── Scans
       ├── Weather            └── Orders                ├── Products
       ├── Marketplace                                  └── Security
       ├── AgriBot
       └── Farm Management
       │
       ▼
 ┌──────────────────────────────────────────────┐
 │              AI / ANALYTICS LAYER            │
 │                                              │
 │ MobileNetV2 Training                         │
 │ Computer Vision                              │
 │ XAI Region Detection                         │
 │ Disease Knowledge Base                       │
 │ Soil NPK Analyzer                            │
 │ Weather Intelligence                         │
 │ AgriBot                                     │
 └──────────────────────┬───────────────────────┘
                        │
                        ▼
              ┌───────────────────┐
              │   SQLite Database │
              ├───────────────────┤
              │ Users             │
              │ Farms / Fields    │
              │ Scans             │
              │ Soil Tests        │
              │ Products          │
              │ Orders            │
              │ Reviews           │
              │ Forum             │
              │ Notifications     │
              └───────────────────┘
                        │
                        ▼
               Agricultural Decision
                    Support
24. Technology Stack
Layer	Technology
Programming Language	Python
Web Framework	Flask
Machine Learning	TensorFlow / Keras
Deep Learning Model	MobileNetV2
Dataset	PlantVillage
Computer Vision	OpenCV
Image Processing	Pillow, NumPy
Database	SQLite
Authentication	Werkzeug password hashing + Flask sessions
Security	HTML escaping, path protection, Luhn, HMAC
Payment	Simulated UPI/Card/COD gateway
QR	QR generation service
Frontend	HTML/CSS/JavaScript templates
Data Visualization	Matplotlib

The README and requirements files confirm the principal technology choices.

25. What Makes PlantaSanitus Different?

The strongest aspect of your project is that it is not just a plant disease detection system.

A conventional project might follow:

Leaf Image → Disease Name

PlantaSanitus attempts to provide:

Leaf Image → Disease → Severity → Urgency → Treatment → Dosage → Product → Payment → Delivery → Follow-up

while also incorporating:

Soil + Weather + Farm Management + AI Assistant + Community + Educational Resources

Therefore, PlantaSanitus can be presented as an integrated AI-powered agricultural decision-support and e-commerce ecosystem.

26. Short Project Description for Presentation

If you need to explain your project in a viva or presentation, you can use this:

PlantaSanitus is an AI-powered Smart Agriculture Platform developed to provide farmers with an integrated solution for plant disease diagnosis and agricultural decision support. The system combines computer vision, explainable AI, soil health analysis, weather intelligence, agro-medicine recommendations, farm management, and an e-commerce marketplace into a single web application. Farmers can upload leaf images for disease analysis, obtain information about symptoms, severity, treatment and prevention, analyze soil NPK and pH values, and receive agricultural guidance through the multilingual AgriBot assistant. The platform also allows farmers to purchase recommended agro-medicines through a marketplace with QR-based product guidance, simulated digital payments and order tracking. Separate Farmer, Seller and Admin roles provide role-based access and management capabilities. SQLite is used for persistent storage, while Flask provides the web application layer. Security mechanisms based on confidentiality, integrity and availability are incorporated throughout the system.

27. One-Line Definition

PlantaSanitus is an integrated AI-driven smart agriculture platform that connects plant disease diagnosis, agricultural decision support, treatment guidance, soil and weather analytics, farmer assistance, and agro-medicine e-commerce in one system.








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
