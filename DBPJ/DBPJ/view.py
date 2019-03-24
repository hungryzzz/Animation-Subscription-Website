# users login and register
# managers login

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from Enjoy.models import Users, Managers, Animation, Subscribe_Comment, Not_sub
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

user_id = 0
user_name = ""
manager_id = 0
manager_name = ""

# 首页
def home(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    if user_id == 0 and manager_id == 0:
        return render_to_response('home.html')
    else:
        if user_id != 0:
            return render(request, 'user_page.html', {'user_id': user_id, 'user_name': user_name})
        else:
            return render(request, 'manager_page.html', {'manager_id': manager_id, 'manager_name': manager_name})

# 用户注册
def reg_form(request):
    global user_id, user_name
    request.encoding = 'utf-8'
    if user_id == 0:
        return render_to_response('register.html')
    else:
        return render(request, 'user_page.html', {'user_id': user_id, 'user_name': user_name})

def reg(request):
    request.encoding = 'utf-8'
    name = request.GET['user_name']
    if name != "":
        namefilter = Users.objects.filter(name=name)
        if len(namefilter) > 0:
            return render(request, 'register.html', {'error': '该用户名已存在'})
        else:
            pw1 = request.GET['user_pw1']
            pw2 = request.GET['user_pw2']
            if pw1 != "" and pw2 != "":
                if pw1 != pw2:
                    return render(request, 'register.html', {'error': '两次输入密码不同'})
                else:
                    email = request.GET['user_email']
                    if email != "":
                        user = Users.objects.create(name=name, pw=pw1, email=email, legal=True)
                        user.save()
                        finish_not_sub(name)
                        return render(request, 'login.html')
                    else:
                        return render(request, 'register.html', {'error': '请输入电子邮箱'})
            else:
                if pw1 == "":
                    return render(request, 'register.html', {'error': '请输入密码'})
                else:
                    return render(request, 'register.html', {'error': '请再次确认密码'})
    else:
        return render(request, 'register.html', {'error': '请输入用户名'})


def finish_not_sub(name):
    list = Animation.objects.all()
    for var in list:
        not_sub = Not_sub.objects.create(user_name=name, ani_name=var.name)
        not_sub.save()
    return


# 用户登录
def login_form(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    if user_id == 0:
        return render_to_response('login.html')
    else:
        return render(request, 'user_page.html', {'user_id': user_id, 'user_name': user_name})

def get_login_name(request):
    request.encoding = 'utf-8'
    global user_name, user_id
    user_name = request.GET['name']
    if user_name == "":
        return render(request, 'login.html', {'error': '请输入用户名'})
    else:
        namefilter = Users.objects.filter(name=user_name)
        legalfilter = Users.objects.filter(name=user_name, legal=True)
        if len(namefilter) > 0:
            if len(legalfilter) > 0:
                for var in namefilter:
                    user_id += var.id
                return login(request)
            else:
                user_name = ""
                return render(request, 'login.html', {'error': '该帐号已被禁用'})
        else:
            user_name = ""
            return render(request, 'login.html', {'error': '该用户名不存在'})

def login(request):
    request.encoding = 'utf-8'
    global user_name, user_id
    pw = request.GET['pw']
    legalfilter = Users.objects.filter(name=user_name, pw=pw, legal=True)
    if len(legalfilter) > 0:
        return render(request, 'user_page.html', {'user_id': user_id, 'user_name': user_name})
    else:
        return render(request, 'login.html', {'error': '密码错误'})

# 用户退出登录
def logout(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    user_id = 0
    user_name = ""
    return render_to_response('home.html')


# 管理员页面
def magager_page(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('home.html')
    else:
        return render(request, 'manager_page.html', {'manager_id': manager_id, 'manager_name': manager_name})

# 管理员登录
def get_manager_name(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    manager_name = request.GET['name']
    if manager_name == "":
        return render(request, 'mlogin.html', {'error': '请输入用户名'})
    else:
        namefilter = Managers.objects.filter(name=manager_name)
        if len(namefilter) > 0:
            for var in namefilter:
                manager_id += var.id
            return mlogin(request)
        else:
            manager_name = ""
            return render(request, 'mlogin.html', {'error': '您无访问权限'})

def mlogin_form(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('mlogin.html')
    else:
        return render(request, 'manager_page.html', {'manager_id': manager_id, 'manager_name': manager_name})


def mlogin(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    num = request.GET['id_num']
    pw = request.GET['pw']
    numfilter = Managers.objects.filter(name=manager_name, id_num=num)
    pwfilter = Managers.objects.filter(name=manager_name, id_num=num, pw=pw)
    if len(pwfilter) > 0:
        return render(request, 'manager_page.html', {'manager_id': manager_id, 'manager_name': manager_name})
    else:
        if len(numfilter) > 0:
            return render(request, 'mlogin.html', {'error': '密码错误'})
        else:
            return render(request, 'mlogin.html', {'error': '工作号错误'})


# 管理员退出登录
def mlogout(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    manager_id = 0
    manager_name = ""
    return render_to_response('home.html')


# 管理员番剧相关
def m_all_animation(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('mlogin.html')
    else:
        Animation.objects.order_by("-pub_time")
        list = Animation.objects.all()
        if len(list) > 0:
            return render(request, 'manager_animation.html', {'list': list, 'message': '所有番剧', 'manager_name': manager_name})
        else:
            return render(request, 'manager_animation.html', {'error': '尚无番剧', 'message': '所有番剧', 'manager_name': manager_name})


def modify_animation_state(request, id):
    request.encoding = 'utf-8'
    Animation.objects.filter(id=id).update(state='已完结')
    return m_all_animation(request)


def manager_add_form(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('mlogin.html')
    else:
        return render(request, 'manager_animation.html', {'message': '添加番剧', 'manager_name': manager_name})


@csrf_exempt
def manager_add_animation(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    img = request.FILES.get('img')
    name = request.POST['name']
    pub_time = request.POST['pub_time']
    update_time = request.POST['update_time']
    style = request.POST['style']
    tag1 = request.POST['tag1']
    tag2 = request.POST['tag2']
    va1 = request.POST['va1']
    va2 = request.POST['va2']
    va3 = request.POST['va3']
    va4 = request.POST['va4']
    state = "未完结"
    link = request.POST['link']
    if not img:
        return render(request, 'manager_animation.html', {'message': '添加番剧', 'mes': '请上传图片',
                                                          'manager_name': manager_name})
    if len(name) <= 0:
        return render(request, 'manager_animation.html', {'message': '添加番剧', 'mes': '请输入番剧名',
                                                          'manager_name': manager_name})
    else:
        namefilter = Animation.objects.filter(name=name)
        if len(namefilter) > 0:
            return render(request, 'manager_animation.html', {'message': '添加番剧', 'mes': '该番剧已存在',
                                                              'manager_name': manager_name})
    if len(pub_time) <= 0:
        return render(request, 'manager_animation.html', {'message': '添加番剧', 'mes': '请输入大陆上映时间',
                                                          'manager_name': manager_name})
    if len(update_time) <= 0:
        return render(request, 'manager_animation.html', {'message': '添加番剧', 'mes': '请输入大陆每周更新时间',
                                                          'manager_name': manager_name})
    animation = Animation.objects.create(img=img, name=name, pub_time=pub_time, update_time=update_time,
                                         style=style, tag1=tag1, tag2=tag2, va1=va1, va2=va2,
                                         va3=va3, va4=va4, state=state, link=link)
    animation.save()
    add_not_sub(name)
    return render(request, 'manager_animation.html', {'message': '添加番剧', 'mes': '添加成功', 'manager_name': manager_name})


def add_not_sub(name):
    list = Users.objects.all()
    for var in list:
        not_sub = Not_sub.objects.create(user_name=var.name, ani_name=name)
        not_sub.save()
    return


# 管理员用户相关
def m_all_users(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('mlogin.html')
    else:
        list = Users.objects.all()
        if len(list) > 0:
            return render(request, 'manager_users.html', {'list1': list, 'flag': '所有用户', 'manager_name': manager_name})
        else:
            return render(request, 'manager_users.html', {'error1': '尚无用户', 'flag': '所有用户', 'manager_name': manager_name})


def m_forbid1(request, id):
    request.encoding = 'utf-8'
    Users.objects.filter(id=id).update(legal=False)
    return m_all_users(request)


def m_allow1(request, id):
    request.encoding = 'utf-8'
    Users.objects.filter(id=id).update(legal=True)
    return m_all_users(request)

m_query_name = ""

def m_query_name_form(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('mlogin.html')
    else:
        return render(request, 'manager_users.html', {'flag': '查询用户', 'manager_name': manager_name})


def m_get_query_name(request):
    request.encoding = 'utf-8'
    global m_query_name
    m_query_name = request.GET['query_name']
    namefilter = Users.objects.filter(name=m_query_name)
    if len(namefilter) > 0:
        return m_query_user(request)
    else:
        m_query_name = ""
        return render(request, 'manager_users.html', {'flag': '查询用户', 'error': '该用户不存在', 'manager_name': manager_name})


def m_query_user(request):
    request.encoding = 'utf-8'
    global m_query_name
    namefilter = Users.objects.filter(name=m_query_name)
    filter = Subscribe_Comment.objects.filter(user_name=m_query_name)
    listfilter = Subscribe_Comment.objects.filter(user_name=m_query_name, comment__isnull=False)
    if len(filter) > 0:
        if len(listfilter) > 0:
            return render(request, 'manager_users.html', {'list': listfilter, 'row': namefilter, 'error': 1, 'message': 1,
                                                          'flag': '查询用户', 'manager_name': manager_name})
        else:
            return render(request, 'manager_users.html', {'row': namefilter, 'message': '该用户尚无评论', 'error': 1,
                                                          'flag': '查询用户', 'manager_name': manager_name})
    else:
        return render(request, 'manager_users.html', {'row': namefilter, 'message': '该用户尚未订阅番剧', 'error': 1,
                                                      'flag': '查询用户', 'manager_name': manager_name})


def m_forbid2(request, id):
    request.encoding = 'utf-8'
    Users.objects.filter(id=id).update(legal=False)
    return m_query_user(request)


def m_allow2(request, id):
    request.encoding = 'utf-8'
    Users.objects.filter(id=id).update(legal=True)
    return m_query_user(request)


def m_delete_comment1(request, id):
    request.encoding = 'utf-8'
    Subscribe_Comment.objects.filter(id=id).update(comment="")
    return m_query_user(request)


# 管理员评论相关
def m_all_comment(request):
    request.encoding = 'utf-8'
    global manager_id, manager_name
    if manager_id == 0:
        return render_to_response('mlogin.html')
    else:
        list1 = Subscribe_Comment.objects.filter(comment__isnull=False)
        if len(list1) > 0:
            return render(request, 'manager_comment.html', {'list': list1, 'manager_name': manager_name})
        else:
            return render(request, 'manager_comment.html', {'message': '尚无评论', 'manager_name': manager_name})


def m_delete_comment2(request, id):
    request.encoding = 'utf-8'
    Subscribe_Comment.objects.filter(id=id).update(comment=None)
    return m_all_comment(request)


user_comment_id = ""
user_comment = ""


# 用户新番订阅表
def mysub(request):
    request.encoding = 'uft-8'
    global user_id, user_name, user_comment_id, user_comment
    if user_id == 0:
        return render_to_response('login.html')
    else:
        list1 = Subscribe_Comment.objects.filter(user_name=user_name)
        if len(list1) > 0:
            list = Animation.objects.all()
            return render(request, 'user_mysub.html', {'list': list, 'list1': list1, 'flag': 0,
                                                       'user_name': user_name})
        else:
            return render(request, 'user_mysub.html', {'error': '您尚未订阅番剧', 'user_name': user_name})


def cancel_sub1(request, name):
    request.encoding = 'utf-8'
    global user_id, user_name
    Subscribe_Comment.objects.filter(user_name=user_name, ani_name=name).delete()
    not_sub = Not_sub.objects.create(user_name=user_name, ani_name=name)
    not_sub.save()
    return mysub(request)


def user_sub_comment(request, id):
    request.encoding = 'utf-8'
    global user_comment_id, user_comment, user_id, user_name
    user_comment_id = id
    ani_name = ""
    list1 = Subscribe_Comment.objects.filter(id=user_comment_id)
    if len(list1) > 0:
        for var in list1:
            if var.comment is not None:
                user_comment += var.comment
            ani_name += var.ani_name
        list = Animation.objects.filter(name=ani_name)
        return render(request, 'user_mysub.html', {'list': list, 'flag': 1, 'comment': user_comment,
                                                   'user_name': user_name})


def get_user_comment(request):
    request.encoding = 'utf-8'
    global user_name, user_id, user_comment_id, user_comment
    comment = request.GET['comment']
    Subscribe_Comment.objects.filter(id=user_comment_id).update(comment=comment)
    user_comment_id = ""
    user_comment = ""
    return mysub(request)


# 用户 番剧相关
def user_all_animation(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    if user_id == 0:
        return render_to_response('login.html')
    list1 = Animation.objects.all()
    if len(list1) > 0:
        list2 = Subscribe_Comment.objects.filter(user_name=user_name)
        list3 = Not_sub.objects.filter(user_name=user_name)
        return render(request, 'user_animation.html', {'list1': list1, 'list2': list2, 'list3': list3,
                                                       'message': '所有番剧', 'user_name': user_name})
    else:
        return render(request, 'user_animation.html', {'error': '尚无番剧', 'user_name': user_name})


def cancel_sub2(request, id):
    request.encoding = 'utf-8'
    global user_id, user_name
    sub = Subscribe_Comment.objects.filter(id=id)
    for var in sub:
        not_sub = Not_sub.objects.create(user_name=user_name, ani_name=var.ani_name)
        not_sub.save()
    Subscribe_Comment.objects.filter(id=id).delete()
    return user_all_animation(request)


def add_sub1(request, name):
    request.encoding = 'utf-8'
    global user_id, user_name
    sub = Subscribe_Comment.objects.create(user_name=user_name, ani_name=name)
    sub.save()
    Not_sub.objects.filter(user_name=user_name, ani_name=name).delete()
    return user_all_animation(request)


ani_year = ""
ani_month = ""


def user_get_time(request, year, month):
    request.encoding = 'utf-8'
    global ani_year, ani_month
    ani_year = year
    ani_month = month
    return user_time_animation(request)


def user_time_animation(request):
    request.encoding = 'utf-8'
    global user_id, user_name, ani_year, ani_month
    if user_id == 0:
        return render_to_response('login.html')
    list1 = Animation.objects.filter(pub_time__year=ani_year, pub_time__month=ani_month)
    if len(list1) > 0:
        list2 = Subscribe_Comment.objects.filter(user_name=user_name)
        list3 = Not_sub.objects.filter(user_name=user_name)
        string = ani_year + '-' + ani_month
        return render(request, 'user_animation.html', {'list1': list1, 'list2': list2, 'message': string,
                                                       'list3': list3, 'user_name': user_name})
    else:
        return render(request, 'user_animation.html', {'error': '尚无该时段番剧', 'user_name': user_name})


def cancel_sub3(request, id):
    request.encoding = 'utf-8'
    global user_id, user_name
    sub = Subscribe_Comment.objects.filter(id=id)
    for var in sub:
        not_sub = Not_sub.objects.create(user_name=user_name, ani_name=var.ani_name)
        not_sub.save()
    Subscribe_Comment.objects.filter(id=id).delete()
    return user_time_animation(request)


def add_sub2(request, name):
    request.encoding = 'utf-8'
    global user_id, user_name
    sub = Subscribe_Comment.objects.create(user_name=user_name, ani_name=name)
    sub.save()
    Not_sub.objects.filter(user_name=user_name, ani_name=name).delete()
    return user_time_animation(request)


query_ani_name = ""


# 用户查询番剧
def get_query_animation(request):
    request.encoding = 'utf-8'
    global query_ani_name, user_name
    query_ani_name = request.GET['query_ani_name']
    anifilter = Animation.objects.filter(name__contains=query_ani_name)
    if len(anifilter) > 0:
        return query_animation(request)
    else:
        query_ani_name = ""
        return render(request, 'user_animation.html', {'message': '查询番剧', 'error1': '无相关番剧',
                                                       'user_name': user_name})


def query_animation(request):
    request.encoding = 'utf-8'
    global user_id, user_name, query_ani_name
    list1 = Animation.objects.filter(name__contains=query_ani_name)
    list2 = Subscribe_Comment.objects.filter(ani_name__contains=query_ani_name, comment__isnull=False)
    list3 = Subscribe_Comment.objects.filter(user_name=user_name, ani_name__contains=query_ani_name)
    list4 = Not_sub.objects.filter(user_name=user_name, ani_name__contains=query_ani_name)
    return render(request, 'user_animation.html', {'message': '查询番剧', 'user_name': user_name,
                                                   'list1': list1, 'list2': list2, 'list3': list3, 'list4': list4})


def user_get_animation_comment(request, name):
    request.encoding = 'utf-8'
    global user_id, user_name
    list1 = Animation.objects.filter(name=name)
    list2 = Subscribe_Comment.objects.filter(ani_name=name, comment__isnull=False)
    list3 = Subscribe_Comment.objects.filter(user_name=user_name, ani_name=name)
    list4 = Not_sub.objects.filter(user_name=user_name, ani_name=name)
    return render(request, 'user_animation.html', {'message': '查询番剧', 'user_name': user_name,
                                                   'list1': list1, 'list2': list2, 'list3': list3, 'list4': list4})


def cancel_sub4(request, id):
    request.encoding = 'utf-8'
    global user_id, user_name
    sub = Subscribe_Comment.objects.filter(id=id)
    for var in sub:
        not_sub = Not_sub.objects.create(user_name=user_name, ani_name=var.ani_name)
        not_sub.save()
    Subscribe_Comment.objects.filter(id=id).delete()
    return query_animation(request)


def add_sub3(request, name):
    request.encoding = 'utf-8'
    global user_id, user_name
    sub = Subscribe_Comment.objects.create(user_name=user_name, ani_name=name)
    sub.save()
    Not_sub.objects.filter(user_name=user_name, ani_name=name).delete()
    return query_animation(request)


# 用户 评论
def user_all_comment(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    if user_id == 0:
        return render_to_response('login.html')
    list = Subscribe_Comment.objects.filter(comment__isnull=False)
    return render(request, 'user_comment.html', {'message': '所有评论', 'list': list, 'user_name': user_name})


def user_my_comment(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    if user_id == 0:
        return render_to_response('login.html')
    list = Subscribe_Comment.objects.filter(user_name=user_name, comment__isnull=False)
    return render(request, 'user_comment.html', {'message': '我的评论', 'list': list, 'user_name': user_name})


def user_animation_comment(request):
    request.encoding = 'utf-8'
    global user_id, user_name
    if user_id == 0:
        return render_to_response('login.html')
    list1 = Animation.objects.all()
    list2 = Subscribe_Comment.objects.filter(comment__isnull=False)
    return render(request, 'user_comment.html', {'list1': list1, 'list': list2, 'message': '各番评论',
                                                 'user_name': user_name})






