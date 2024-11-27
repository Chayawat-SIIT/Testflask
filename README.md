# Concert Ticketing System

Welcome to the **G-10 Cloud-Based Application Project** repository! This repository contains the source code for a scalable cloud-based application, featuring **frontend** and **backend** components. The project is designed for deployment both locally and on the cloud.

---

## Repository Structure

```plaintext
.
├── frontend/          # Frontend source code
│   ├── Dockerfile     # Dockerfile for frontend container
│   ├── Static         # Components file
│   └── Template       # Other HTML file
├── backend/           # Backend source code
│   ├── Dockerfile     # Dockerfile for backend container
│   ├── app.py         # Main Python application file
│   ├── requirements.txt # Python dependencies
│   └── ...            # Other backend scripts and modules
└── README.md          # Project documentation
```
---

## Features

- **Frontend**: Built with HTML, CSS, and JavaScript for user interactions.
- **Backend**: Python (Flask) API for business logic and data processing.
- **Scalability**: Deployed on AWS with ECS and an Application Load Balancer.

---

## Getting Started

You can run the application locally or access the deployed cloud version.

### Access the Cloud Deployment

The application is deployed on AWS. You can access it using the following URL:  
**[Cloud Application URL](http://backend-alb-83162907.us-east-1.elb.amazonaws.com)**

---

### Running Locally

You can run the application locally using one of two methods:

#### Method 1: Virtual Environment (venv)

1. **Backend Setup**:
   - Navigate to the `backend/` folder:
     ```bash
     cd backend
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the backend application:
     ```bash
     python app.py
     ```

2. **Frontend Setup**:
   - Open the `frontend/` folder in your code editor.
   - Use a live server plugin (such as the Live Server extension in VS Code) to simulate the frontend locally.

#### Method 2: Using Docker Desktop

1. Ensure Docker Desktop is installed and running on your system.
2. Build and run the frontend and backend containers:
   - For the backend:
     ```bash
     cd backend
     docker build -t backend-app .
     docker run -p 5000:5000 backend-app
     ```
   - For the frontend:
     ```bash
     cd frontend
     docker build -t frontend-app .
     docker run -p 8080:80 frontend-app
     ```
3. Access the application:
   - Frontend: `http://localhost:8080`
   - Backend: `http://localhost:5000`

---

## Technical Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Cloud Infrastructure**: AWS ECS, Application Load Balancer (ALB)

---

## Contributing

We welcome contributions to improve this project! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please feel free to reach out!
```
