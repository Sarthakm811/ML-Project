# API Documentation

## Overview
This document describes the API endpoints available in the Student Performance Predictor application.

---

## Base URL
```
http://localhost:5000
```

---

## Endpoints

### 1. Home Page
**Endpoint:** `/`  
**Method:** `GET`  
**Description:** Returns the home page with project introduction

**Response:**
- **Content-Type:** `text/html`
- **Status Code:** 200

**Example:**
```bash
curl http://localhost:5000/
```

---

### 2. Prediction Form (GET)
**Endpoint:** `/predictdata`  
**Method:** `GET`  
**Description:** Returns the prediction form page

**Response:**
- **Content-Type:** `text/html`
- **Status Code:** 200

**Example:**
```bash
curl http://localhost:5000/predictdata
```

---

### 3. Make Prediction (POST)
**Endpoint:** `/predictdata`  
**Method:** `POST`  
**Description:** Submit student data and receive math score prediction

**Request Body (Form Data):**
| Parameter | Type | Required | Options |
|-----------|------|----------|---------|
| gender | string | Yes | "male", "female" |
| ethnicity | string | Yes | "group A", "group B", "group C", "group D", "group E" |
| parental_level_of_education | string | Yes | "some high school", "high school", "some college", "associate's degree", "bachelor's degree", "master's degree" |
| lunch | string | Yes | "standard", "free/reduced" |
| test_preparation_course | string | Yes | "none", "completed" |
| reading_score | integer | Yes | 0-100 |
| writing_score | integer | Yes | 0-100 |

**Response:**
- **Content-Type:** `text/html`
- **Status Code:** 200
- **Body:** HTML page with prediction result

**Example using curl:**
```bash
curl -X POST http://localhost:5000/predictdata \
  -d "gender=male" \
  -d "ethnicity=group B" \
  -d "parental_level_of_education=bachelor's degree" \
  -d "lunch=standard" \
  -d "test_preparation_course=completed" \
  -d "reading_score=75" \
  -d "writing_score=80"
```

**Example using Python:**
```python
import requests

url = "http://localhost:5000/predictdata"
data = {
    'gender': 'male',
    'ethnicity': 'group B',
    'parental_level_of_education': "bachelor's degree",
    'lunch': 'standard',
    'test_preparation_course': 'completed',
    'reading_score': 75,
    'writing_score': 80
}

response = requests.post(url, data=data)
print(response.text)
```

**Example using JavaScript (fetch):**
```javascript
const formData = new FormData();
formData.append('gender', 'male');
formData.append('ethnicity', 'group B');
formData.append('parental_level_of_education', "bachelor's degree");
formData.append('lunch', 'standard');
formData.append('test_preparation_course', 'completed');
formData.append('reading_score', '75');
formData.append('writing_score', '80');

fetch('http://localhost:5000/predictdata', {
    method: 'POST',
    body: formData
})
.then(response => response.text())
.then(html => console.log(html));
```

---

## Data Types & Validation

### Gender
- **Type:** String
- **Values:** "male", "female"

### Race/Ethnicity
- **Type:** String
- **Values:** "group A", "group B", "group C", "group D", "group E"

### Parental Level of Education
- **Type:** String
- **Values:** 
  - "some high school"
  - "high school"
  - "some college"
  - "associate's degree"
  - "bachelor's degree"
  - "master's degree"

### Lunch Type
- **Type:** String
- **Values:** "standard", "free/reduced"

### Test Preparation Course
- **Type:** String
- **Values:** "none", "completed"

### Reading Score
- **Type:** Integer
- **Range:** 0-100

### Writing Score
- **Type:** Integer
- **Range:** 0-100

---

## Error Handling

### Common Errors

**400 Bad Request**
- Missing required parameters
- Invalid parameter values

**500 Internal Server Error**
- Model prediction failure
- Server-side error

---

## Response Format

The POST response returns an HTML page with the prediction displayed as:
```html
<div class="result">
    <h2>📊 Predicted Math Score: [score]</h2>
</div>
```

---

## Rate Limiting
Currently, there is no rate limiting implemented. Consider implementing rate limiting for production use.

---

## Future Enhancements
- RESTful JSON API endpoint
- API authentication
- Batch predictions
- Model confidence scores
- Feature importance visualization

---

For questions or issues, please contact: sarthakm811@gmail.com
