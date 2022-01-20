from flask import render_template,redirect,request,session,flash
from flask_app import app, bcrypt
from flask_app.models.show import Show
from flask_app.models.user import User


# @app.route('/')
# @app.route('/sightings')
# def all_recipes():
#     sightings = Sightings.get_all()
#     print(sightings)
#     return render_template('index.html', all_sightings = sightings)


@app.route('/new')
def new_show():

    context = {
        'user' : User.get_one({'id':session['user_id']})
    }

    return render_template('new.html', **context)



@app.route('/create_show', methods=['POST'])
def create_show():


    is_valid = Show.validate_show(request.form)

    if not is_valid:
        return redirect('/new')

    data = {
        **request.form,
        'user_id' : session['user_id']
        # "name": request.form["name"],
        # "description": request.form["description"],
        # "instructions" : request.form["instructions"],
        # "date_made_on" : request.form["date_made_on"],
    }
    # Call the save @classmethod on User
    Show.create(data)
    # store user id into session

    return redirect("/dashboard")

@app.route('/show/<int:id>/show')
def show_show(id):
    context = {
        'user': User.get_one({'id': session['user_id']}),
        'show': Show.get_one({'id': id})

    }
    return render_template("show.html", **context)


@app.route('/edit/<int:id>')
def edit_show(id):

    show = Show.get_one({'id': id})

    if show.user_id != session['user_id']:
        return redirect('/')

    context = {
        'user': User.get_one({'id': session['user_id']}),
        'show' : show
    }
    return render_template('edit.html', **context)



@app.route('/show/<int:id>/update', methods=["POST"])
def update_show(id):

    show = Show.get_one({'id': id})

    if show.user_id != session['user_id']:
        return redirect('/')

    is_valid = Show.validate_show(request.form)

    if not is_valid:
        return redirect(f'/edit/{id}')

    data = {
        **request.form,
        'id':id
        # 'recipe' : recipe
    }
    show = Show.update(data)
    return redirect('/dashboard')


@app.route('/show/<int:id>/delete', methods=['POST'])
def delete_Show(id):

    show = Show.get_one({'id': id})

    if show.user_id != session['user_id']:
        return redirect('/')

    Show.delete_show({'id': id})
    return redirect('/dashboard')