import catalogue

from flask import Flask, request, url_for, render_template
cost = 0
cart = {}
cart_str = ""
userName = None

app = Flask(__name__)


# url_for('static', filename='style.css')
@app.route("/")
def home(userName=None):
    return render_template('layout.html', name=userName)

@app.route("/<string:userName>/")
def getUserName(userName):
    cart[userName] = {}
    return (f"Welcome to NoN, {userName}")


@app.route('/<userName>/<path:item>')
def buyItem(userName, item):
    global cart, cart_str
    cart_str = ""
    # show the subpath after /path/
    if item not in cart[userName].keys() and item in catalogue.shopItems:
        cart[userName][item] = [1, catalogue.shopItems[item]]
    elif item not in catalogue.shopItems:
        return f"No stock for {item}"
    else:
        cart[userName][item][0]+=1
    for i,l in enumerate(cart[userName].items()):
        cart_str += f"<tr>\
        <td>{i+1}</td>\
        <td>{l[0]}</td>\
        <td>{l[1][0]}</td>\
        <td>{l[1][0]*l[1][1]}</td>\
        </tr>"

    list = "<br/>\
            <b>This is your shopping cart!</b><br/>\
            <table style='border: 1px solid black'> \
            <tr> \
                <th>S/N</th> \
                <th>Item</th> \
                <th>Qty</th> \
                <th>Cost<th> \
            </tr>" \
             + cart_str \
            + "</table>"
    print(cart)
    return (f" You've added {item} into your Shopping Cart!<br/><br/>" + list)


'''<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
'''
@app.route('/<userName>/checkOut')
def checkOut(userName):
    global cart, cost
    cost = 0
    print(cart)
    print(cart[userName].values())
    for c in cart[userName].values():
        cost += c[0]*c[1]
    return f"<br/>\
            <h1><b>Checkout details</b><br/></h1>\
            <table style='border: 1px solid black'> \
            <tr> \
                <th>S/N</th> \
                <th>Item</th> \
                <th>Qty</th> \
                <th>Cost<th> \
            </tr>" \
             + cart_str \
            + f"<tr> \
                    <th></th> \
                    <th></th> \
                    <th><b>Total cost:</b></th>\
                    <th>{cost}</th> \
                </tr> \
            </table>"

@app.route('/<userName>/checkOut/payment')
def payment(userName):
    global cart
    print(cart)
    cart[userName] = {}
    print(cart)
    return f"You have paid {cost}!</br></br>Thank you and have a nice day! :)"


if __name__ == "__main__":
    app.run(host='0.0.0.0')



'''@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()'''
