# Portfolio Django Project / Projeto Portfólio Django

## Overview / Visão geral  
This is a personal portfolio website built with Django. It uses template inheritance, includes 3 models (Post, Categoria, Contato), and has forms for creating posts, contacts, and searching posts.  
Este é um site portfólio pessoal feito com Django. Usa herança de templates, inclui 3 modelos (Post, Categoria, Contato) e tem formulários para criar posts, contatos e buscar posts.

---

## Features / Funcionalidades  
- Display posts with categories  
- Create new posts through a form  
- Contact form with success confirmation page  
- Search posts by title (or other field)  
- Home page with personal info and skills  

---

## How to run / Como rodar  

1. Clone this repository / Clone este repositório  
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Create and activate your virtual environment / Crie e ative seu ambiente virtual
Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Linux/Mac:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies / Instale as dependências

bash
Copy
Edit
pip install -r requirements.txt
Run migrations / Rode as migrações

bash
Copy
Edit
python manage.py migrate
Start the server / Inicie o servidor

bash
Copy
Edit
python manage.py runserver
Open your browser and go to / Abra o navegador e acesse

cpp
Copy
Edit
http://127.0.0.1:8000/
Testing the functionalities / Testando as funcionalidades
Home Page: Personal info and skills — URL: /

Posts: View all posts — URL: /posts/

Create Post: Create a new blog post — URL: /posts/criar/

Contact Form: Fill and send contact — URL: /contato/

Search Posts: Use the search form (if implemented) on /posts/ or wherever you placed it

Notes / Observações
Static files (CSS, JS, images) served from portfolio/static/

Templates are in portfolio/templates/ using Django template inheritance

Ensure you run the server inside the virtual environment

Made with ❤️ by Gisele Pavellegini
