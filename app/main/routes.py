from flask import Blueprint, render_template, request
from app.models import Post

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    #paginate to 5 posts per page
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')