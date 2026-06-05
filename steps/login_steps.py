from behave import *

@given('User opens login page')
def step_impl(context):
    print("Application Opened")

@when('User enters valid username and password')
def step_impl(context):
    print("Credentials Entered")

@then('User should see dashboard')
def step_impl(context):
    print("Dashboard Displayed")
    
