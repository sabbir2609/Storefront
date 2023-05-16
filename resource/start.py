import subprocess

# Start PostgreSQL
postgre_process = subprocess.Popen(["sudo", "service", "postgresql", "start"])
postgre_process.communicate()

# Start Redis
redis_process = subprocess.Popen(["sudo", "service", "redis-server", "start"])
redis_process.communicate()
