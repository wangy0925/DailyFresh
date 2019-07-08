from django.shortcuts import render

# Create your views here.
def goods_index(request):
    """
    :param request:
    :return: 首页
    """
    if request.user.is_authenticated:
        username = request.user.username
        print('user---', username)
    else:
        username = ''
    return render(request, 'goods/goods.html', {'username': username, 'status': '1'})