from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from random import choice, randint
import logging
from django.utils import lorem_ipsum




logger = logging.getLogger(__name__)

def my_logger(func):
    def wrapper(*args, **kwargs):
        coin = func(*args, **kwargs)
        logger.info(f"Была вызвана функция {func.__name__}")
        return coin
    return wrapper

@my_logger
def main_form(request):
    html = f"""
        <h1>Main</h1>
        <h2>It`s all</h2>
        <p>{" ".join(lorem_ipsum.paragraphs(100, common=False))}</p>
    """
    return HttpResponse(html)

@my_logger
def about(request):
    html = f"""
        <h1>Hello!</h1>
        <h2>My name is Alex</h2>
        <h3>About me:</h3>
        <p>{" ".join(lorem_ipsum.paragraphs(5, common=False))}</p>
    """
    return HttpResponse(html)

