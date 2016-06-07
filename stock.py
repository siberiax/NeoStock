import mechanize
import parsetext

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [('User-agent', 'Chrome')]

url = "http://www.neopets.com/stockmarket.phtml?type=portfolio"

user = '***REMOVED***'
passwd = '***REMOVED***'

response = br.open(url)

br.select_form(name="login")
br.form["username"] = user
br.form["password"] = passwd
success = br.submit()

data = success.read()

parsetext.parseData(data)
