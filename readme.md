# Digital Spark

**Digital Spark** is a smart web application built with Python and Streamlit that helps users plan and manage their monthly social media content using curated tools, customizable templates, and subscription packages. It's ideal for small business owners, content creators, or anyone looking to build a strong digital presence.

---

## Features

### ✅ User Authentication
- Secure Signup & Login system using session state.
- Simulated user database with password validation.

### ✅ Dashboard (Post-Login)
- Personalized welcome message for logged-in users.
- Clean, professional UI with custom CSS.

### ✅ Content Tools Section
- Access content calendar, templates, analytics, and more.
- Built using OOP (`ToolsSection` class) for modularity.

### ✅ Subscription Packages
- 3 Tiers: **Basic**, **Pro**, and **Premium**.
- Package cards with price and 4 benefits each.
- Users can choose a package — stored in session state.

### ✅ Payment Section (Simulated)
- Dynamic pricing display based on selected plan.
- Checkout button available (Stripe can be added later).

### ✅ Logout Function
- Sign out option on the dashboard.
- Instantly redirects to the homepage.

---

## Technologies Used

- **Python 3.10+**
- **Streamlit**
- **OOP (Object-Oriented Programming)**
- **HTML/CSS (custom styling)**
- **Session State (for login and plan selection)**

---

## Folder Structure

Digital_Spark/
│
├── app.py # Main entry point
├── styles.css # Custom styling
├── dashboard_main.py # Dashboard content (tools, packages, payment)
│
├── app_pages/
│ ├── home.py
│ ├── login.py
│ └── signup.py
│
├── content_tools.py # OOP: ToolsSection
├── packages.py # OOP: PackageSection
├── payment.py # OOP: PaymentSection
├── backend/
│ └── user_db.py # OOP: UserDatabase and auth
├── models/
│ └── user.py # OOP: User model class
└── utils/
└── load_css.py # Load CSS helper



---

## Future Vision & Expansion

In future versions, **Digital Spark** will become a complete SaaS platform for content creators and brands. Here's what we plan to add:

- **Real Payment Integration (Stripe/PayPal)**
- **Drag-and-drop content calendar with reminders**
- **AI-generated post ideas and captions**
- **User analytics dashboard (charts, engagement stats)**
- **Admin dashboard for managing subscriptions**
- **Email notifications & newsletters**
- **Mobile-responsive UI and deployment on Streamlit Cloud**

---

## How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/digital-spark.git
   cd digital-spark


---

## Future Vision & Expansion

In future versions, **Digital Spark** will become a complete SaaS platform for content creators and brands. Here's what we plan to add:

- **Real Payment Integration (Stripe/PayPal)**
- **Drag-and-drop content calendar with reminders**
- **AI-generated post ideas and captions**
- **User analytics dashboard (charts, engagement stats)**
- **Admin dashboard for managing subscriptions**
- **Email notifications & newsletters**
- **Mobile-responsive UI and deployment on Streamlit Cloud**

---

## How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/digital-spark.git
   cd digital-spark


---

## Future Vision & Expansion

In future versions, **Digital Spark** will become a complete SaaS platform for content creators and brands. Here's what we plan to add:

- **Real Payment Integration (Stripe/PayPal)**
- **Drag-and-drop content calendar with reminders**
- **AI-generated post ideas and captions**
- **User analytics dashboard (charts, engagement stats)**
- **Admin dashboard for managing subscriptions**
- **Email notifications & newsletters**
- **Mobile-responsive UI and deployment on Streamlit Cloud**

---

## How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/digital-spark.git
   cd digital-spark

2. **Install dependencies** 
pip install -r requirements.txt

3. **Run the app** 
streamlit run app.py


Credits
Made with love by Anam Anwer GIAIC Roll # 00355123 as part of the $10 Challenge (3rd Week) — an educational initiative by GIAIC, promoting creativity and entrepreneurship through coding.