rm -r migrations
rm app.db
flask db init
flask db migrate -m "Init"
flask db upgrade
