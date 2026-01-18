# Deployment Guide

## Table of Contents
1. [Local Deployment](#local-deployment)
2. [Docker Deployment](#docker-deployment)
3. [Cloud Deployment](#cloud-deployment)
4. [Environment Variables](#environment-variables)

---

## Local Deployment

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Steps

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd "ML Project"
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
Open your browser and navigate to: `http://localhost:5000`

---

## Docker Deployment

### Using Docker

1. **Build the Docker image**
```bash
docker build -t student-performance-app .
```

2. **Run the container**
```bash
docker run -p 5000:5000 student-performance-app
```

3. **Access the application**
Navigate to: `http://localhost:5000`

### Using Docker Compose

1. **Build and run**
```bash
docker-compose up -d
```

2. **Stop the application**
```bash
docker-compose down
```

---

## Cloud Deployment

### AWS Elastic Beanstalk

1. **Install EB CLI**
```bash
pip install awsebcli
```

2. **Initialize EB**
```bash
eb init -p python-3.9 student-performance-app
```

3. **Create environment and deploy**
```bash
eb create student-performance-env
eb deploy
```

### Heroku

1. **Create Procfile**
```
web: python app.py
```

2. **Deploy to Heroku**
```bash
heroku create your-app-name
git push heroku main
heroku open
```

### Azure Web App

1. **Create requirements.txt** (already done)

2. **Deploy using Azure CLI**
```bash
az webapp up --name your-app-name --resource-group your-resource-group
```

### Google Cloud Platform (App Engine)

1. **Create app.yaml**
```yaml
runtime: python39
entrypoint: python app.py
```

2. **Deploy**
```bash
gcloud app deploy
```

---

## Environment Variables

For production deployment, consider setting:

```bash
# Flask environment
FLASK_ENV=production

# Security
SECRET_KEY=your-secret-key-here

# Logging
LOG_LEVEL=INFO
```

### Setting Environment Variables

**Linux/Mac:**
```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
```

**Windows:**
```powershell
$env:FLASK_ENV="production"
$env:SECRET_KEY="your-secret-key"
```

**Docker:**
```dockerfile
ENV FLASK_ENV=production
ENV SECRET_KEY=your-secret-key
```

---

## Production Considerations

1. **Use a production server** (e.g., Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Set up SSL/HTTPS**

3. **Configure logging**

4. **Set up monitoring**

5. **Regular backups of artifacts folder**

---

## Troubleshooting

### Port already in use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Module not found errors
```bash
pip install -r requirements.txt --force-reinstall
```

### Permission errors
```bash
chmod +x app.py  # Linux/Mac
```

---

For more help, please open an issue on GitHub.
