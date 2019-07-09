from django.shortcuts import render

# Create your views here.
def goods_index(request):
    """
    :param request:
    :return: 首页
    """
    return render(request, 'goods/goods.html')