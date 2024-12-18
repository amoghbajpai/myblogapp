from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

posts = []

@app.route('/')
def index():
	return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
	if request.method == 'POST':
		title = request.form['title']
		content = request.form['content']
		posts.append({'title': title, 'content': content})
		return redirect(url_for('index'))
	return render_template('add.html')

@app.route('/delete/<int:post_id>')

def delete(post_id):
	if 0 <= post_id < len(posts):
		posts.pop(post_id)
		return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)
