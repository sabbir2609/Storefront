# Storefront-1.1

A flexible and scalable e-commerce headless app with Django RESTapi

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://storefrontx.azurewebsites.net/)

### Features :
1. Category
2. Products
3. Cart
4. User , User Group
5. Image Upload ( not configured )

• Authentication : JWT
• Parallel Tasking -> Celery
• Cache -> Redis
• Database -> PostgreSQL

when you start locally : 
```
sudo service postgresql start
docker run -p 6379:6379 redis
python manage.py runserver
```

Docker File coming soon ! 
