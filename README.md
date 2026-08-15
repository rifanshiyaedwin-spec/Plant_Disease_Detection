# 🌿 PLANTASANITUS – SMART AGRICULTURE PLATFORM

### AI-Powered Agricultural Decision Support and Agro-Medicine E-Commerce Ecosystem

---

## 1. PROJECT OVERVIEW

**PlantaSanitus** is an AI-enabled Smart Agriculture Platform developed to provide farmers with a centralized digital solution for plant disease identification, disease severity assessment, soil health analysis, weather monitoring, treatment recommendations, farm management, and agro-medicine purchasing.

The platform combines Artificial Intelligence, Computer Vision, Explainable AI, soil analytics, weather intelligence, multilingual assistance, e-commerce, farm management, community interaction, educational resources, and security mechanisms into a single web-based application.

The system is primarily developed using **Python and Flask**, with **TensorFlow and Keras** used for machine learning, **OpenCV** for computer vision, **Pillow and NumPy** for image processing, and **SQLite** for database management.

PlantaSanitus is designed as a **Final Year Computer Science and Engineering Capstone Project** that demonstrates the application of modern software engineering, artificial intelligence, machine learning, database management, web development, and cybersecurity concepts in the agricultural domain.

---

## 2. MAIN OBJECTIVE

The primary objective of PlantaSanitus is to provide farmers with an integrated agricultural assistant that combines multiple agricultural services within a single platform.

Traditional agricultural applications often focus on one particular function, such as disease detection, weather monitoring, soil testing, or product purchasing. PlantaSanitus attempts to combine these activities into one unified system.

The platform allows a farmer to provide agricultural information, such as plant images or soil parameters, and receive analytical results and recommendations. Based on the diagnosis, the farmer can access treatment information and related agro-medicine products through the marketplace.

The system therefore supports the complete agricultural decision-making process, beginning with identifying a problem and continuing through treatment selection, product purchasing, order tracking, and historical record management.

---

## 3. MULTI-ROLE AUTHENTICATION SYSTEM

PlantaSanitus implements a role-based authentication system that supports three major categories of users: **Farmers, Agro-Medicine Sellers, and Administrators**.

Each user category receives access to functionality appropriate to its responsibilities. Authentication is implemented using password hashing and session-based authentication mechanisms.

### 3.1 Farmer

Farmers represent the primary users of the platform. They can perform plant disease scans by uploading leaf images, analyze soil health, view weather information, manage farms and fields, review previous disease scans, purchase agro-medicines, track orders, interact with AgriBot, and participate in the community forum.

The farmer dashboard is designed to provide access to the major agricultural services of the platform from a centralized interface.

### 3.2 Agro-Medicine Seller

Agro-Medicine Sellers are responsible for managing products available through the marketplace.

Sellers can add new agricultural products, specify product categories and target diseases, define product prices, manage available stock, provide product descriptions, upload product images, and enter usage instructions.

The seller functionality allows the marketplace to maintain product information and inventory while providing farmers with access to relevant treatment products.

### 3.3 Administrator

Administrators provide centralized management and supervision of the platform.

Administrative functionality includes managing users, reviewing disease scan information, managing marketplace products, monitoring security-related information, and supporting system-level auditing and administration.

The role-based architecture ensures that users cannot access functionality that does not belong to their assigned role.

---

## 4. AI PLANT DISEASE DETECTION

AI-based plant disease detection is one of the primary features of PlantaSanitus.

The platform allows farmers to upload up to three images of an affected plant leaf for analysis. The uploaded images are processed by the application and passed to the disease prediction component.

The diagnostic system is designed to provide more information than simply identifying a disease name.

The results can include the crop name, detected disease, scientific name, confidence score, disease severity, treatment urgency, estimated recovery period, symptoms, possible causes, organic treatment recommendations, chemical treatment recommendations, preventive measures, and highlighted regions associated with visible symptoms.

The diagnostic information is also stored in the database so that farmers can review their previous scans and use the information for future reference.

This makes the disease detection component useful not only as a classification system but also as an agricultural decision-support feature.

---

## 5. MACHINE LEARNING ARCHITECTURE

The project contains a dedicated training module named `train.py` for developing the plant disease classification model.

The machine learning pipeline uses the **PlantVillage dataset** and applies transfer learning using **MobileNetV2** with ImageNet pretrained weights.

The MobileNetV2 architecture is used as the base feature extractor. Additional layers, including Global Average Pooling, Dropout, and a Softmax classification layer, are used to produce the final disease classification.

The model uses images with a resolution of **224 × 224 pixels**. A 20% validation split is used during training.

Data augmentation techniques include horizontal and vertical flipping, rotation, zoom, and contrast adjustment. These techniques are intended to improve model generalization by exposing the model to variations in the training images.

The model is trained using the **Adam optimizer** and **Sparse Categorical Cross-Entropy loss**, with accuracy used as the primary evaluation metric.

The training process also includes model checkpointing, early stopping, and learning-rate reduction. The trained model is saved as `plant_disease_model.h5`.

### 5.1 Important Implementation Observation

There is an important distinction between the machine learning training architecture and the current integrated inference implementation.

The `train.py` module genuinely defines and trains a MobileNetV2-based disease classification model. However, the current `predict.py` implementation does not directly load `plant_disease_model.h5` and perform TensorFlow-based inference.

Instead, the current prediction implementation contains demonstration-oriented logic for determining disease labels and generating prediction-related values.

Therefore, the technically accurate statement for a project presentation is:

> **“PlantaSanitus incorporates a MobileNetV2 transfer-learning pipeline for plant disease classification, while the currently integrated inference module contains a demonstration-oriented prediction implementation.”**

This distinction should be clearly explained if the project is evaluated by an examiner.

---

## 6. EXPLAINABLE AI

PlantaSanitus incorporates Explainable AI concepts to make disease predictions more understandable to users.

Instead of displaying only the predicted disease, the system attempts to identify regions of the leaf where visible symptoms may be present.

The XAI component uses OpenCV-based image processing to identify potential symptom regions, including areas associated with necrosis and other visible abnormalities. These regions can be represented using bounding-box coordinates.

The system can also provide human-readable descriptions of observed visual characteristics, such as leaf chlorosis and yellowing, concentric brown necrotic spots, edge scorching, and cuticle decay.

This approach improves the interpretability of the system because users can understand which portions of the image contributed to the visual explanation.

The XAI functionality is particularly useful in an agricultural application because farmers may be more confident in a recommendation when the system provides visual evidence rather than only presenting a classification result.

---

## 7. PLANT DISEASE KNOWLEDGE BASE

The `disease_info.py` module contains a structured plant disease knowledge base covering 38 PlantVillage crop and disease classes according to the project documentation.

The knowledge base provides additional information associated with each disease classification.

Depending on the disease, the information can include the crop name, disease name, scientific name, disease status, severity, symptoms, possible cause, organic treatment, chemical treatment, and preventive measures.

For example, an Apple Scab entry can contain information about its symptoms, fungal cause, organic treatment options, chemical treatment recommendations, and preventive practices.

The knowledge base allows the disease prediction module to transform a predicted disease class into useful agricultural information that can be understood by farmers.

---

## 8. DISEASE SEVERITY AND TREATMENT PRIORITY

PlantaSanitus provides an additional severity assessment after identifying a disease.

The system categorizes disease conditions into three major levels: **Mild, Moderate, and Severe**.

A mild condition represents a comparatively limited disease presence, while a moderate condition indicates a more noticeable infection requiring timely treatment. A severe condition represents a serious infection requiring immediate attention.

The system also generates a severity percentage, treatment urgency, and estimated recovery period.

This feature transforms the system from a basic disease classification application into a more practical decision-support platform.

Farmers can therefore understand not only what disease may be affecting their crop but also how serious the condition may be and how urgently action should be taken.

---

## 9. AGRO-CHEMICAL DOSAGE CALCULATOR

PlantaSanitus includes a dosage calculation feature designed to assist farmers in estimating treatment requirements according to field size.

The farmer can enter the field area in acres, after which the system calculates the required chemical or fungicide quantity and the corresponding amount of water.

The system can also provide a spraying schedule, such as applications on Day 1, Day 7, and Day 14, depending on the treatment information available within the application.

The purpose of this feature is to help farmers translate general treatment recommendations into field-level application requirements.

Actual chemical usage should always be verified against the product label and appropriate agricultural guidance before application.

---

## 10. SOIL HEALTH ANALYSIS

PlantaSanitus includes a dedicated soil health analysis module implemented through `soil_service.py`.

The system evaluates soil parameters including **pH, Nitrogen, Phosphorus, Potassium, and field area**.

Based on the entered pH value, the system determines whether the soil is acidic, within an optimal range, or alkaline.

The system also evaluates nutrient levels and identifies possible deficiencies in Nitrogen, Phosphorus, and Potassium.

Based on the analysis, PlantaSanitus generates fertilizer or organic amendment recommendations.

This functionality provides farmers with a basic digital soil assessment mechanism and connects soil information with agricultural decision-making.

---

## 11. WEATHER INTELLIGENCE

PlantaSanitus includes weather intelligence to help farmers understand environmental conditions affecting agriculture.

The weather component provides information such as temperature, humidity, wind speed, rainfall outlook, and potential disease-risk conditions.

Weather conditions can have a significant effect on crop health. High humidity, rainfall, and certain temperature conditions can increase the risk of particular plant diseases, especially fungal infections.

By integrating weather information with other agricultural features, PlantaSanitus attempts to provide farmers with more context when making crop-management decisions.

---

## 12. AGRO-MEDICINE E-COMMERCE MARKETPLACE

A distinctive feature of PlantaSanitus is its integrated agro-medicine marketplace.

The marketplace connects disease diagnosis and treatment recommendations with the purchasing of agricultural products.

The marketplace supports organic and chemical agricultural products. Each product can contain information such as its name, category, target disease, price, available stock, description, usage instructions, and product image.

Farmers can browse products, add required quantities to their shopping cart, proceed through checkout, make a simulated payment, and monitor the progress of their orders.

This creates an integrated connection between disease identification and treatment procurement.

The marketplace therefore extends the platform beyond diagnosis and provides farmers with a complete digital treatment-support environment.

---

## 13. QR-BASED PRODUCT GUIDANCE

PlantaSanitus includes a QR-based product guidance feature for agro-medicines.

Each product can be associated with a QR code that directs the user to the corresponding product or instruction page.

The QR-based system can provide access to product information and usage instructions.

This feature can be particularly useful when QR codes are printed on physical agricultural product packaging.

A farmer can scan the code using a mobile device and access relevant product information without manually searching for the product within the platform.

---

## 14. SHOPPING AND ORDER MANAGEMENT

PlantaSanitus supports a complete shopping and order-management process.

An order contains information including the associated user, total amount, payment method, payment status, order status, delivery date, and shipping address.

The marketplace supports multiple stages of order processing, including order placement, processing, transportation, and delivery.

Order cancellation functionality is also supported.

The database updates product inventory when orders are created, allowing available stock to be maintained within the marketplace.

This provides sellers with inventory control while allowing farmers to monitor the status of their purchases.

---

## 15. SECURED PAYMENT GATEWAY

The project contains a dedicated `payment_service.py` module that provides a simulated payment gateway for academic purposes.

The payment system supports three major payment methods: **UPI, Card, and Cash on Delivery**.

UPI payments use Virtual Payment Address format validation.

Card payments use the **Luhn checksum algorithm** to validate card-number structure.

Cash on Delivery provides an alternative payment method without requiring digital payment validation.

The payment service generates a transaction identifier and cryptographic transaction signature. Sensitive account information is masked rather than returned in complete form.

It is important to clarify that this is a **simulated payment gateway** intended for academic demonstration and is not a real connection to a bank, UPI provider, or commercial payment gateway.

---

## 16. AGRIBOT AI ASSISTANT

PlantaSanitus includes **AgriBot AI**, a multilingual agricultural assistant designed to provide farmers with quick access to agricultural information.

The assistant can answer questions related to plant diseases, treatments, dosage guidance, organic remedies, and preventive measures.

The current implementation contains knowledge related to diseases and agricultural products such as Early Blight, Late Blight, Apple Scab, Common Rust, Neem Oil, and Copper Fungicide.

The implementation supports multiple languages, including English, Tamil, Hindi, Telugu, and Kannada.

The chatbot receives the user's question and selected language through an API and generates an appropriate response.

This multilingual capability is particularly useful for agricultural users who may prefer receiving information in regional languages.

---

## 17. MULTI-FARM AND FIELD MANAGEMENT

PlantaSanitus includes dedicated database entities for managing farms and individual fields.

A farm can contain information such as the farm name, area in acres, crop type, location, and owner.

Individual fields can contain information including the field name, current status, and notes.

Field status can represent conditions such as healthy, diseased, or harvested.

This feature enables the platform to organize agricultural information at the farm and field levels instead of treating every disease scan as an isolated event.

Farm management therefore provides a foundation for future expansion into more advanced precision-agriculture and farm-monitoring capabilities.

---

## 18. FARMER COMMUNITY FORUM

PlantaSanitus includes a community forum designed to encourage interaction and knowledge sharing among agricultural users.

The forum supports posts, replies, user associations, images, and expert verification.

The `is_expert_verified` field allows the system to identify content that has been verified by an expert.

The community feature can provide farmers with an opportunity to share agricultural experiences, discuss crop problems, ask questions, and learn from other users.

This complements the AI-based assistance provided by the platform with a human-oriented knowledge-sharing environment.

---

## 19. GOVERNMENT SCHEMES AND EDUCATIONAL RESOURCES

PlantaSanitus provides dedicated sections for agricultural government schemes and educational resources.

The government-scheme section can provide information about areas such as crop insurance, agricultural subsidies, and organic certification.

The educational section provides agricultural videos, disease guides, and other learning resources.

The Flask application exposes dedicated routes for schemes, videos, and guides.

These features aim to make the platform useful not only for disease diagnosis and product purchasing but also for improving farmers' access to agricultural knowledge and support information.

---

## 20. DISEASE HISTORY AND REPORTS

PlantaSanitus stores disease scan information in the database so that users can review their previous diagnostic activities.

Each scan can contain information including the user, uploaded image, crop, disease, confidence score, severity, treatment urgency, recovery time, scientific name, XAI highlights, and timestamp.

The stored information can be accessed through the history functionality.

The application also provides report-generation functionality for individual scans.

Historical information can help farmers identify recurring disease problems and maintain a record of crop-health observations over time.

---

## 21. DATABASE ARCHITECTURE

PlantaSanitus uses **SQLite** as its primary database system.

The database is designed to manage multiple categories of information required by the platform.

The major database entities include users, farms, fields, disease scans, soil tests, products, orders, order items, reviews, forum posts, forum replies, notifications, and audit information.

The Users entity forms an important part of the system because user information is associated with activities such as disease scans, farms, soil tests, reviews, forum participation, and orders.

Farm and Field entities support agricultural organization, while Product, Order, and Order Item entities support the marketplace.

Forum Post and Forum Reply entities support community interaction.

Notifications can be used to provide users with important system or order-related information.

The database module acts as a central database manager responsible for storing and retrieving information required throughout the application.

---

## 22. SECURITY ARCHITECTURE

Security is an important component of PlantaSanitus.

The project follows concepts associated with the **CIA Triad: Confidentiality, Integrity, and Availability**.

### 22.1 Confidentiality

Confidentiality is supported through password hashing, HTTP-only session cookies, role-based authorization, and masking of sensitive payment information.

Password hashing prevents passwords from being stored directly in plain text.

Session security mechanisms help protect authenticated user sessions.

Role-based authorization restricts users from accessing functionality outside their assigned permissions.

### 22.2 Integrity

Integrity mechanisms include HTML escaping, XSS protection, secure file-upload handling, path-traversal protection, database transaction management, Luhn validation, and HMAC-based transaction signatures.

These mechanisms are intended to prevent unauthorized modification, malicious input, and manipulation of important application information.

### 22.3 Availability

Availability-related mechanisms include file-upload size restrictions, OpenCV fallback processing, and application-level operational checks.

These features help the application continue functioning reliably while preventing unnecessarily large or problematic uploads from affecting system operation.

---

## 23. OVERALL SYSTEM ARCHITECTURE

The overall architecture of PlantaSanitus consists of a Flask-based web application layer, user-specific interfaces, AI and analytics services, database services, marketplace services, and security components.

The Flask web server acts as the primary application layer and connects the frontend interfaces with backend services.

The Farmer interface provides access to disease detection, soil analysis, weather information, marketplace services, AgriBot, farm management, community features, and historical records.

The Seller interface provides product and inventory management functionality.

The Administrator interface provides centralized management and monitoring capabilities.

The AI and analytics layer contains the machine learning pipeline, computer vision processing, disease knowledge base, soil analysis engine, weather intelligence, and AgriBot functionality.

SQLite provides persistent storage for users, farms, fields, scans, soil tests, marketplace products, orders, reviews, forum information, notifications, and audit information.

Together, these components form an integrated agricultural decision-support ecosystem.

---

## 24. TECHNOLOGY STACK

### Programming Language

**Python** is used as the primary programming language for backend development, machine learning, image processing, database interaction, and application logic.

### Web Framework

**Flask** is used to develop the web application and manage routes, sessions, user interactions, and backend services.

### Machine Learning

**TensorFlow and Keras** are used for developing and training the plant disease classification model.

### Deep Learning Model

**MobileNetV2** is used as the transfer-learning architecture for plant disease classification.

### Dataset

The **PlantVillage dataset** is used as the primary dataset for plant disease model development.

### Computer Vision

**OpenCV** is used for image processing and XAI-related visual region detection.

### Image Processing

**Pillow and NumPy** are used for image manipulation, preprocessing, and numerical operations.

### Database

**SQLite** is used as the persistent relational database for the application.

### Authentication

**Werkzeug password hashing and Flask sessions** are used for authentication and session management.

### Security

Security mechanisms include HTML escaping, XSS protection, file-upload validation, path protection, Luhn validation, and HMAC-based transaction verification.

### Payment

A simulated payment service supports UPI, Card, and Cash on Delivery.

### QR Generation

A QR generation service is used to provide product-specific guidance links.

### Frontend

The user interface is developed using HTML, CSS, JavaScript, and Flask templates.

### Data Visualization

Matplotlib is available for data visualization and analytical representation.

---

## 25. WHAT MAKES PLANTASANITUS DIFFERENT?

The major strength of PlantaSanitus is that it is not limited to being a plant disease detection application.

A conventional plant disease detection project may simply identify a disease from a leaf image and display the result.

PlantaSanitus attempts to extend the process by providing disease identification, severity analysis, treatment urgency, treatment recommendations, dosage guidance, agro-medicine products, payment processing, order management, and follow-up history.

The platform additionally integrates soil analysis, weather intelligence, farm and field management, multilingual AI assistance, community interaction, government scheme information, and agricultural educational resources.

Therefore, PlantaSanitus can be positioned as an **integrated AI-powered agricultural decision-support and e-commerce ecosystem** rather than simply a disease classification system.

Its major innovation lies in bringing multiple agricultural services together within a single platform.

---

## 26. PROJECT INNOVATION

The project combines several technologies and agricultural services that are commonly implemented as separate systems.

The integration of **AI-based plant disease analysis with treatment recommendations and agro-medicine e-commerce** is one of the project's major distinguishing features.

The inclusion of **Explainable AI** provides additional transparency by identifying visible symptom regions.

The **soil health module** provides additional context for crop management.

The **weather intelligence module** provides environmental information that can influence disease risk.

The **AgriBot multilingual assistant** improves accessibility for farmers who prefer regional languages.

The **farm and field management system** provides a foundation for maintaining agricultural records over time.

The **community forum and educational resources** further expand the platform beyond automated diagnosis.

Together, these features make PlantaSanitus a broader agricultural technology ecosystem.

---

## 27. PROJECT LIMITATIONS

Although PlantaSanitus provides a wide range of features, certain limitations should be clearly acknowledged.

The current integrated disease-prediction implementation is demonstration-oriented and does not directly perform TensorFlow inference using the trained `plant_disease_model.h5`.

The payment gateway is simulated and is not connected to a real financial institution or payment provider.

Weather intelligence depends on the availability and implementation of the underlying weather service.

The soil analysis system uses predefined thresholds and should not be considered a replacement for professional laboratory soil testing.

Disease identification based on images may also be affected by image quality, lighting conditions, leaf orientation, disease similarity, and differences between controlled datasets and real-world agricultural environments.

These limitations provide opportunities for future development.

---

## 28. FUTURE ENHANCEMENTS

Several improvements can be implemented in future versions of PlantaSanitus.

The trained MobileNetV2 model can be directly integrated into the production inference pipeline so that uploaded images are processed using the actual trained neural network.

The disease classification model can be further improved using larger and more diverse real-world agricultural datasets.

Advanced XAI techniques such as Grad-CAM can be integrated to provide more reliable visual explanations of model predictions.

The platform can be extended with IoT sensors for real-time soil moisture, temperature, humidity, and environmental monitoring.

Satellite imagery and drone-based crop monitoring can be incorporated for large-scale agricultural analysis.

Real payment gateways such as commercial UPI and card-payment providers can replace the current simulated payment service in a production environment.

The multilingual assistant can be expanded to support additional Indian and international languages.

The system can also be enhanced with personalized recommendations based on crop type, location, weather, soil condition, historical disease records, and farm characteristics.

---

## 29. CONCLUSION

PlantaSanitus is an integrated Smart Agriculture Platform that combines artificial intelligence, computer vision, explainable AI, soil analysis, weather intelligence, farm management, agricultural assistance, and agro-medicine e-commerce.

The platform enables farmers to analyze plant diseases, understand disease severity, obtain treatment recommendations, evaluate soil conditions, access weather information, manage agricultural fields, communicate through a community platform, and purchase relevant agro-medicines.

The use of role-based authentication provides separate functionality for farmers, sellers, and administrators. SQLite provides persistent storage, while Flask serves as the primary web application framework.

The inclusion of security mechanisms, multilingual assistance, QR-based product guidance, order management, disease history, and educational resources further expands the capabilities of the platform.

The major strength of PlantaSanitus is its integrated approach. Instead of treating disease detection, soil analysis, agricultural guidance, and product purchasing as independent functions, the platform attempts to bring them together into one unified agricultural ecosystem.

Therefore, PlantaSanitus can be defined as an **AI-driven agricultural decision-support platform designed to connect crop health analysis, treatment guidance, farm management, farmer assistance, and agro-medicine commerce within a single digital environment.**

---

## 30. ONE-LINE PROJECT DEFINITION

**PlantaSanitus is an integrated AI-driven Smart Agriculture Platform that connects plant disease diagnosis, agricultural decision support, treatment guidance, soil and weather analytics, farm management, farmer assistance, and agro-medicine e-commerce in one unified ecosystem.**
