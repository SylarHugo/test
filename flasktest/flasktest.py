#导入Flask类
from flask import Flask#func1,func2
#用于自定义路由转换func3
from werkzeug.routing import BaseConverter 
#Werkzeug是一个WSGI工具包 对先引入index.html,同时根据后面传入的参数,对html进行修改渲染#func4
from flask import render_template
#接收包含前端发送过来的所有请求数据func4
from flask import request
#redirect重定向到其它网站302
from flask import redirect#func4
#重定向到自身的其它函数中#func4
from flask import url_for
#前后端之间传输数据的函数#func5,make_dir  
from flask import make_response
#传输数据的格式为json#func5
from flask import json
#格式转换成json
from flask import jsonify
#在网页中主动抛出异常，类似raise#func5
from flask import abort
#jinja2模板，在原html中添加返回内容func6,func7
#后端使用表单，等他与前端的form，func8
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
#验证数据是否为空，是否相同,验证返回值需要使用wsgi
from wtforms.validators import DataRequired, EqualTo
#add wsgi server改用局域网ip
from gevent import pywsgi
#flask_sqlalchemy



 
#flask对象实例化
app = Flask(__name__)
#关闭ascii格式，正常显示中文
#app.config['JSON_AS_ASCII'] = False
#后端控制前端form等表单时，出发CSRF保护，回避保护
app.config['SECRET_KEY'] = 'some string'



'''              '/'为根目录127.0.0.1:5000，
app.route为路由，形成服务器与py代码的映射关系，
每个网页都需要一个@app.route建立ip和def func的关系
显示内容为@app.route紧跟着的def func()，同名是忽略后面的
 @app.route('/hello')为127.0.0.1:5000/hello  
 @app.route('/hi')为127.0.0.1:5000/hi 
func同名可修改端点，进行修正。endpoint=''   '''
@app.route('/', methods = ['get'], endpoint = 'hello')
def func1():
	return 'Hello world!'

'''       <>表示使用正则表达式，用于提取参数，
将/后的内容赋值给id，用int：规定id的数据类型
<id>时，id为str型，需要int(id)或str(2)转换。
int正数，string字符（不包含/），float正浮点数，path包含/的文本路径
'''
@app.route('/func2/<int:id>')
def func2(id):
	if id == 1:
		return 'python'
	if id == 2:
		return 'flask'
	if id == 3:
		return 'django'

class RegexConverter(BaseConverter):#继承类,

 	def __init__(self,url_map, regex1):
 		'''执行程序，建立映射时执行,访问调用该类的url时不再重新执行
 		重写类时，改写了父类的方法，用super调用父类方法。setattr添加属性'''
 		super(RegexConverter,self).__init__(url_map)
 		self.regex2 = regex1
 		self.uuu = url_map
 		#print(url_map)#此时只有func1,func2
 		#print(regex1)#regex1标识re()内的正则规则1\d{3}
 	def to_python(self, value):
 		'''访问调用该类的url时执行,self.uuu中添加url，func3'''
 		#print(self.regex2)
 		#print(self.uuu)#不在一个方法内,不能行print(url_map)
 		return value#value返回到func3
 		

'''将自定义的转换器RegexConverter添加到flask对象中。
['re1']表示字典型，{'re':RegexConverter}
'''
app.url_map.converters['re1'] = RegexConverter
#/<re1("123"):value>报错程序错误，1\d{m}标识1开始的数字,m标识d代表的数字位数
@app.route('/func3/<re1("1\d{3}"):value>')
def func3(value):
	return 'func3 : re1("regular expression")'


@app.route('/func4', methods = ['GET', 'POST'])
def func4():
	'''render_template在.py同级的templates文件夹中找indexhtml
	或设置jinja2模板'''
	#get mostbe capital letter
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		name = request.form.get('name1')#只能get到1个值或1个字典等
		password = request.form.get('password')
		return 'type(name) is str'
	if request.method == 'redirect':#重定向
		return redirect('https://www.baidu.com')
	if request.method == 'url_for':#重定向
		return redirect(url_for('func1')) 

@app.route('/func5', methods = ['GET', 'POST'])
def func5():
	data = {
	'name' : 'li'
	}
	#把data以json格式返回给前端
	#return make_response(data)

	'''
	把data以text/html格式返回给前端,json默认为asllc,不能显示中文
	ensure_ascii=False正常显示中文'''
	#return make_response(json.dumps(data,ensure_ascii=False))
	'''把text/html改成json回传
	mimetype = Multipurpose Internet Mail Extensions type
	'''
	# response = make_response(json.dumps(data,ensure_ascii=False))
	# response.mimetype = 'application/json'
	# return response
	'''jsonify函数把data套加json格式'''
	#return jsonify(data)
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		#abort(404)
		name = request.form.get('name1')
		if name == 'sylar':
			return "hello sylar"
		else:
			abort(404)

#自定义错误方法404
@app.errorhandler(404)
def handle_404_error(err):
	return 'this error is 404'
	#return render_template('index.html')

#jinja2
@app.route('/func6')
def func6():
	data2 = {'name' : 'syalr','age' : 18}
	#只能使用func6的data,不能使用其它函数的值
	return render_template('index.html',data = data2)

#自定义过滤器
def func7(val):#def a filter function
	pass
#注册过滤器filter，才能在html中使用过滤器
app.add_template_filter(func7, 'func7nameinhtml')
#html中用|使用过滤器


#后端使用前端表单，先定义类
class MyForm(FlaskForm):
	uname = StringField(label = 'name', validators=[DataRequired()])
	# upw = PasswordField(label = 'u_pw', validators = [DataRequired()])
	# upw2 = PasswordField(label = 'u_pw2', validators = [DataRequired(), EqualTo(upw)])
	# usubmit = SubmitField(label = 'u_submit')

#与其它fun1-7不能用在同一html中,需要部署wsgi
@app.route('/func8', methods = ['GET', 'POST'])
def func8register():
	form = MyForm()
	'''部署玩wsgi后，先近func8,提交后优先跳转到func8指定html的form
	的action指定的app.route中，默认为'/'，eg.action='/func4'，优先进入func4.
	再进行get,post判断
		'''
	if request.method == 'GET':
		return render_template('register.html', form = form)
		#部署玩wsgi后
	if request.method == 'POST':
		if form.validate_on_submit():
			return render_template('index.html', form = form)
		else:
			print('authentication failed,https://flask-wtf.readthedocs.io/')
		#return render_template('register.html', form = form)

if __name__ == '__main__':
	#部署线上web，使用wsgi
	server = pywsgi.WSGIServer(('0.0.0.0', 12345), app)
	server.serve_forever()
	app.run()


