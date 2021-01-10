# CachyPooh
Website to build understanding of databases and web development!
CacheDatabase holds top trending news/entertainment tidbits so that users can find trendy info from all major entertainment/media sources
# Setting up the database
- Start up wsl
- Create a virtual environment
- Run `pip3 install -r requirements.txt`
- Then `pip freeze > requirements.txt`
- Run `sudo su - postgres`
- `createdb mydb` replace mydb with ur db name
- `createuser -P` Will give u prompts to answer
- `psql`
- `GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;` Replace mydb with your db name and myuser with your username
- You now have a postgres database set up :)
# Starting database
- `sudo su - postgres`
- `psql`
- `pg_ctlcluster 12 main start`
- OR
- `sudo /etc/init.d/postgresql start`
# Starting server
- CD to your directory
- `python3 manage.py runserver`
