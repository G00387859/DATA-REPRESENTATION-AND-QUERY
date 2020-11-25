from flask_sqlalchemy import SQLAlchemy
if __name__ == "__main__":
    app.run(debug=True)
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="donalmaher067.mysql.pythonanywhere-services.com",password="Hollyroco@9552",hostname="donalmaher067.mysql.pythonanywhere-services.com",databasename=" donalmaher067$datarepresentation",)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False