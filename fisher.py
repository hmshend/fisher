from app import create_app


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
