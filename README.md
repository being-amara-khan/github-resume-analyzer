# GitHub Resume Analyzer

A Flask-based web application that analyzes GitHub profiles and displays key metrics about a user's repositories and coding activity, implemented with a complete CI/CD pipeline.

## Application Screenshots

### Main Interface
![GitHub Resume Analyzer Interface](Github%20Resume%20analyzer.jpeg)

### Results Page
![GitHub Resume Analyzer Results](Github%20resme%20analyser%202.jpeg)

### CI/CD Pipeline Configuration
![GitHub Webhook Configuration](webhook_.PNG)

### Pipeline Execution Logs
![GitHub Hook Log](Github_Hook_logs.jpeg)

## Project Overview

This project demonstrates a complete DevOps implementation, combining:
- Web Application Development (Flask)
- Containerization (Docker)
- Continuous Integration/Continuous Deployment (Jenkins)
- Version Control (GitHub)
- Automated Testing (Pytest)

## DevOps Implementation Steps

### 1. Application Development
- **Technology Stack**: Python, Flask, Bootstrap 5
- **Why**: Flask provides a lightweight, flexible framework for web applications, while Bootstrap ensures responsive design
- **Implementation**: Created a web application that fetches and displays GitHub user statistics

### 2. Containerization with Docker
- **Dockerfile Creation**:
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY . .
  EXPOSE 5000
  CMD ["python", "app.py"]
  ```
- **Why**: Containerization ensures consistent deployment across different environments
- **Benefits**: 
  - Isolated environment
  - Easy deployment
  - Consistent runtime
  - Scalability

### 3. Version Control with GitHub
- **Repository Structure**:
  ```
  github-resume-analyzer/
  ├── app.py
  ├── requirements.txt
  ├── Dockerfile
  ├── Jenkinsfile
  ├── test_app.py
  └── templates/
      ├── index.html
      └── result.html
  ```
- **Why**: Version control is essential for:
  - Code tracking
  - Collaboration
  - Rollback capabilities
  - Change history

### 4. Automated Testing
- **Testing Framework**: Pytest
- **Test Cases**:
  - Home page accessibility
  - API endpoint validation
  - Error handling
- **Why**: Automated testing ensures:
  - Code quality
  - Regression prevention
  - Continuous validation

### 5. CI/CD Pipeline with Jenkins
- **Pipeline Stages**:
  1. Checkout code
  2. Run tests
  3. Build Docker image
  4. Deploy container
- **Why**: CI/CD pipeline provides:
  - Automated builds
  - Continuous testing
  - Automated deployment
  - Quality assurance

### 6. GitHub Webhook Integration
- **Configuration**:
  - Webhook URL: Jenkins server endpoint
  - Events: Push and Pull Request
  - Content type: application/json
- **Why**: Webhooks enable:
  - Automatic pipeline triggers
  - Real-time updates
  - Event-driven deployments

## Features

- Analyze any GitHub user's profile
- View public repository count
- Calculate total stars across repositories
- Display programming languages used
- Show last activity date
- Modern, responsive UI with Bootstrap 5

## Tech Stack

- Python 3.9
- Flask
- Bootstrap 5
- Docker
- GitHub API

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/being-amara-khan/github-resume-analyzer.git
cd github-resume-analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Docker Deployment

Build and run using Docker:

```bash
docker build -t github-analyzer-app .
docker run -d --name github-analyzer-container -p 5000:5000 github-analyzer-app
```

The application will be available at `http://localhost:5000`

## CI/CD Pipeline Details

The pipeline is configured in the `Jenkinsfile` and includes:

1. **Checkout Stage**
   - Pulls the latest code from GitHub
   - Ensures clean workspace

2. **Test Stage**
   - Runs pytest suite
   - Validates application functionality
   - Ensures code quality

3. **Build Stage**
   - Creates Docker image
   - Tags with version
   - Pushes to registry (if configured)

4. **Deploy Stage**
   - Stops existing container
   - Deploys new container
   - Updates application

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 