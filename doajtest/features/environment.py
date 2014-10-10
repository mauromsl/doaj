from selenium import webdriver

from doajtest import helpers

# See more granular and higher-level possibilities for init/finalisation code at
# http://pythonhosted.org/behave/tutorial.html#environmental-controls


def before_all(context):
    context.live_server = helpers.LiveServer(port=helpers.get_first_free_port())
    context.live_server.spawn_live_server()
    context.app_url = context.live_server.get_server_url()
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.quit()


# Reset the index between whole files full of scenarios (== features)
def before_feature(context, feature):
    helpers.setup_index()


def after_feature(context, feature):
    context.live_server.terminate_live_server()
    helpers.teardown_index()