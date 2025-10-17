

# ☁️ Cloud Resume Project 2025 

A personal resume website hosted on **AWS** — built as part of my cloud learning journey.  
This project demonstrates deploying a **serverless web application** using AWS services such as **S3, Lambda, API Gateway, and DynamoDB**.

---

## 🌐 Live Demo
[Visit my live site here](https://davidgillick.co.uk)  
*(Hosted on AWS S3 with a live visitor counter powered by AWS Lambda and DynamoDB.)*

---

## 🏗️ Project Overview
This project follows the structure of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/), combining front-end development with AWS cloud services.

**Architecture Flow:**
```

User → CloudFront (optional) → S3 (Static Site)
↓
API Gateway → Lambda → DynamoDB

````

---

## 💡 Features
- **Static Website** hosted on S3  
- **Serverless Visitor Counter** using Lambda + DynamoDB  
- **API Gateway** for communication between front-end and backend  
- **CI/CD ready** for easy updates via GitHub  

---

## 🧩 Tech Stack
| Layer | Service / Technology |
|--------|-----------------------|
| Frontend | HTML, CSS, JavaScript |
| Hosting | AWS S3 (Static Website Hosting) |
| Backend | AWS Lambda (Python) |
| Database | AWS DynamoDB |
| API | AWS API Gateway |
| Infrastructure | CloudFormation / Terraform / CDK |

---

## ⚙️ Setup Instructions
To deploy your own version of this site:

1. **Clone this repository**
   ```bash
   git clone https://github.com/Gillickd/html_css_js_resume.git
   cd cloud-resume-project-public
````

2. **Deploy the backend (Lambda, API Gateway, DynamoDB)**

   * Use the templates in `/infrastructure/`
   * Replace placeholders (e.g., table name, bucket name)

3. **Update environment variables**

   * In Lambda configuration, set:

     ```
     TABLE_NAME = your-dynamodb-table-name
     ```
   * In the website config.json file, replace the API_BASE & API_STAGE placeholder:
   * Note: if API stage is configured to default, then remove API_STAGE from config.json file

     {
  "API_BASE": "https://your-api-gateway-url.com", 
  "API_STAGE": "dev"
}

4. **Deploy the frontend**

   * Upload website/contents to your S3 bucket.
   * Enable **Static Website Hosting** in S3 properties.

5. **Test it**

   * Open your S3 website endpoint in a browser.
   * Confirm that the visitor counter updates correctly.

---

## 📁 Repository Structure

```
cloud-resume-project-public/
├── website/           # HTML, CSS, JS files
├── lambda/            # Lambda function(s)
├── infrastructure/    # CloudFormation / Terraform / CDK templates
├── website/assets/    # Diagrams, screenshots, icon and images 
└── README.md
```

---

## 🧠 Learnings

Through this project, I learned how to:

* Connect **Lambda** functions to **DynamoDB** via **API Gateway**
* Use **AWS IAM roles** securely
* Deploy and host a static site on **AWS S3**
* Understand the fundamentals of **serverless architectures**
* Manage Infrastructure as Code (IaC) 

---

## 🖼️ Architecture Diagram

![Architecture Diagram](assets/architecture.png)

---

## ✍️ Author

**David Gillick**
[LinkedIn](https://linkedin.com/in/davidgillickaws) • [Blog](https://medium.com/@david.gillick/cloud-resume-project-08981aefbca1)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).




