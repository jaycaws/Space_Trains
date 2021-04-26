import MySQLdb
from flask import Flask, render_template, request, json

app = Flask(__name__)

db = MySQLdb.connect(host="database-1.csp9hzaw6xyx.us-east-2.rds.amazonaws.com", port=3306, user="root",
                     passwd="password", db="")
cursor = db.cursor()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/query/')
def about():
    return render_template('about.html')


@app.route('/select', methods=['POST', 'GET'])
def query():
    try:
        __query = request.args.get("query")
        print('one')

        if __query:
            db.query(__query)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("about.html", query=__query, data=data)
            else:
                print('four')

                return render_template("about.html", query=__query, data=data)

        else:
            print('five')
            return render_template("about.html", query=__query)

    except Exception as e:
        print('error')
        return render_template("about.html", query=__query, data=data)
    finally:
        print("were done~")


@app.route('/expeditions/')
def exp():
    cursor.execute("SELECT * FROM spacetrains.EXPO_INSTANCE")
    data = cursor.fetchall()
    return render_template('expeditions.html', value=data)


@app.route('/addExp', methods=['POST', 'GET'])
def addExp():
    try:
        __addExp = request.args.get("addExp")

        cursor.execute(__addExp)
        print('one')

        if __addExp:
            db.query(__addExp)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("port.html", query=__addExp)
            else:
                print('four')

                return render_template("port.html", query=__addExp)

        else:
            print('five')

            return render_template("port.html")

    except Exception as e:
        print('error')
        return render_template("port.html", query=__addExp)
    finally:
        print("were done~")


@app.route('/deleteExpedition', methods=['POST', 'GET'])
def delExp():
    try:
        __delExp = request.args.get("delExp")
        print('one')

        if __delExp:
            db.query(__delExp)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("port.html", query=__delExp)
            else:
                print('four')

                return render_template("port.html", query=__delExp)

        else:
            print('five')
            return render_template("port.html", query=__delExp)

    except Exception as e:
        print('error')
        return render_template("port.html", query=__delExp)
    finally:
        print("were done~")


@app.route('/port/')
def port():
    cursor.execute("SELECT * FROM spacetrains.SPACEPORT")
    data = cursor.fetchall()
    return render_template('port.html', value=data)


@app.route('/addPort', methods=['POST', 'GET'])
def addPort():
    try:
        __addPort = request.args.get("addPort")
        cursor.execute(__addPort)
        print('one')

        if __addPort:
            db.query(__addPort)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("port.html", query=__addPort)
            else:
                print('four')

                return render_template("port.html", query=__addPort)

        else:
            print('five')

            return render_template("port.html")

    except Exception as e:
        print('error')
        return render_template("port.html", query=__addPort)
    finally:
        print("were done~")


@app.route('/deletePort', methods=['POST', 'GET'])
def delPort():
    try:
        __delPort = request.args.get("delPort")
        print('one')

        if __delPort:
            db.query(__delPort)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("port.html", query=__delPort)
            else:
                print('four')

                return render_template("port.html", query=__delPort)

        else:
            print('five')
            return render_template("port.html", query=__delPort)

    except Exception as e:
        print('error')
        return render_template("port.html", query=__delPort)
    finally:
        print("were done~")


@app.route('/trains/')
def trains():
    cursor.execute("SELECT * FROM spacetrains.TRAIN_TYPE")
    data = cursor.fetchall()
    return render_template('trains.html', value=data)


@app.route('/addTrain', methods=['POST', 'GET'])
def addTrain():
    try:
        __addTrain = request.args.get("addTrain")
        cursor.execute(__addTrain)
        print('one')

        if __addTrain:
            db.query(__addTrain)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("port.html", query=__addTrain)
            else:
                print('four')

                return render_template("port.html", query=__addTrain)

        else:
            print('five')

            return render_template("port.html")

    except Exception as e:
        print('error')
        return render_template("port.html", query=__addTrain)
    finally:
        print("were done~")


@app.route('/deleteTrain', methods=['POST', 'GET'])
def delTrain():
    try:
        __delTrain = request.args.get("delTrain")
        print('one')

        if __delTrain:
            db.query(__delTrain)
            print("one a")
            results = db.store_result()
            print("one b")
            data = results.fetch_row(maxrows=0)
            print("two")

            if len(data) is 0:
                print('three')
                return render_template("port.html", query=__delTrain)
            else:
                print('four')

                return render_template("port.html", query=__delTrain)

        else:
            print('five')
            return render_template("port.html", query=__delTrain)

    except Exception as e:
        print('error')
        return render_template("port.html", query=__delTrain)
    finally:
        print("were done~")


if __name__ == '__main__':
    app.run(debug=True)
