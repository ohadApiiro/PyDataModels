from Flask import Flask

app = Flask(__name__)


@app.route('/my_route')
def hello():
    return 'hello'

class ClassWithoutMethods:
    foo = 1


class UserData:
    def __init__(self):
        self.user_name = ""
        self.user_Id = ""
        self.user_credit = ""
        self.user_bank = ""
        self.user_money = 0