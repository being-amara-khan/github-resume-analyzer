# GitHub Resume Analyzer

A Flask-based web application that analyzes GitHub profiles and displays key metrics about a user's repositories and coding activity.

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
git clone https://github.com/yourusername/github-resume-analyzer.git
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

## CI/CD Pipeline

This project includes a CI/CD pipeline that:
- Runs tests on every push
- Builds and deploys the Docker container
- Ensures code quality and consistency

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 