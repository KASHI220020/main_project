from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/admin_view')
def admin_view():
    data={}
    q="select * from agent"
    res=select(q)
    data['res']=res
    return render_template('admin_view.html',data=data)


@admin.route('/ad_add_policy',methods=['get','post'])
def ad_add_policy():
    data={}
    q="select * from policy"
    res=select(q)
    data['res']=res
    if 'submit' in request.form:
        polic_T=request.form['p_type']
        p_amount=request.form['p_amount']
        p_nod=request.form['p_num']
        q="insert into policy value(null,'%s','%s','%s')"%(polic_T,p_amount,p_nod)
        res=insert(q)
        return redirect(url_for('admin.ad_add_policy'))
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['pid']
    
    else:
        action=None

    if action=="delete":
        q="delete from policy where policy_id='%s'"%(id)
        delete(q)
        return redirect(url_for('admin.ad_add_policy'))

    if action=="update":
        q="select * from policy where policy_id='%s'"%(id)
        res=select(q)
        data['ressss']=res



    if "Update" in request.form:
        polic_T=request.form['p_type']
        p_amount=request.form['p_amount']
        p_nod=request.form['p_num']
        q="update policy set policy='%s',amount='%s',noofdays='%s' where policy_id='%s'"%(polic_T,p_amount,p_nod,id)
        update(q)
        return redirect(url_for('admin.ad_add_policy'))

    return render_template('admin_addp.html',data=data)

@admin.route('/ad_dmgreq')
def ad_dmgreq():
    data={}
    q="select * from damagerequest"
    res=select(q)
    data['res']=res
    return render_template('admin_dmgreq.html',data=data)