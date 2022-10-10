# Storefront-1.1
This is the step by step code from The Ultimate Django Course by Code With Mosh

Preview Demo : [Storefront](https://storefront2609.herokuapp.com/)

### Features :
1. Category
2. Products
3. Cart
4. User , User Group
5. Image Upload

Authentication : JWT
Parallel Tasking -> Celery
Cache -> Redis
Database -> PostgreSQL

when you start : 
```
sudo service postgresql start
docker run -p 6379:6379 redis
python manage.py runserver
```

Docker File coming soon ! 