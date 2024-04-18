from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#edu_platform all request handlers


def _registrationView(request):
    """ _registration function for registration process in edu_platform
        The function receives request from edu_platform's registaration form with POST method
        The function handle logics for registration  """
    pass

def _loginView(request):
    """_loginView function for login users of edu_platform
        The function uses login and authenticate methods to login user
        render and redirect methods used to login user """
    pass

def _course_detailsView(request):
    """ _ displays detailed information about a specific course.
Shows course description, instructor details, lesson module"""
    pass
def _course_listView(request):
    """funct """
    pass
def _lesson_detailsView(request):
    """"""
    pass
def _exam_detailsView(request):
    pass

def _grade_exam_detailsView(request):
    pass

def _aboutView(request):
    """_aboutView function for rendering the contents about edu_platform"""
    pass


login_required(login_url='login')
def _logoutView(request):
    """_logoutView function for logging out user from edu_platform's system dashboard""" 
    pass