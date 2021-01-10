from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/sorting_algorithms')
def sorting_algo():
	return render_template('sorting.html')


@app.route('/path_finding')
def path_finding():
	return render_template('path_finding.html')


@app.route('/sudoku')
def sudoku_solver():
	return render_template('sudoku.html')


if __name__ == '__main__':
	app.run(debug=True)