# Storefront-1.1
A flexible and scalable e-commerce headless app with Django RESTapi

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://storefrontx.azurewebsites.net/)

### Features :
1. Category
2. Products
3. Cart
4. User , User Group
5. Image Upload

• Authentication : JWT  [See setupguide.md](./resources/setupguide.md)  
• Parallel Tasking -> Celery  
• Cache -> Redis  
• Database -> PostgreSQL  

when you start : 
```
sudo service postgresql start
docker run -p 6379:6379 redis
python manage.py runserver
```

Update: I've successfully run this into Termux Android.

Technologies :   
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) 
