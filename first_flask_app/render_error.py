from flask import Flask, render_template


app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, world',
        'content': 'This is my first blog post!'
    }
}


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/post/<int:post_id>')
def post(post_id):
    """
    This function renders a template from the `templates` folder in the directory of app.py.
    It will find the `post.html` template and render it with the data passed in.
    Look at `post.html` for information on how the variable `post` gets used there.
    """
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} was NOT found!')

    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)