from . import post
from .form import PostForm
from flask import request, flash, redirect, url_for,render_template
from flask_login import current_user
from app.models import Post
from app import db

@post.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form=PostForm()
    if request.method == 'POST' and form.validate_on_submit():
    #    this is coming from the post form
        post_data = {
                'img_url':form.img_url.data,
                'title':form.title.data,
                'caption':form.caption.data,
                'user_id': current_user.id

        }

        # Create a Post Instance
        new_post = Post()

        # Set post_data to our post attributes
        new_post.from_dict(post_data)

        db.session.add(new_post)
        db.commit()

        flash('Successfully created post', 'success')
        return redirect(url_for('main.home'))
    else:
        return render_template('create_post.html', form=form)