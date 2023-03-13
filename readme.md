## BLOG API -- FAST API (PYTHON)

### Steps

- Create Virtual Env  
  `python -m venv fastapi-env`

- Activate the env file  
  `fastapi-env\Scripts\activate.bat`

- Instal FAST API in the virtual env  
  `pip3 install fastapi`

- Install Server Imp for Python  
  ` pip3 install uvicorn`

---

### After creating main.py file

- Start the Server  
  `uvicorn main:app --reload`

---

### To Test API

- Swagger UI  
  ` localhost:8000/docs`

- Redoc  
  ` localhost:8000/redoc`
