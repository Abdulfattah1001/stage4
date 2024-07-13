broker_url = 'pyamqp://guest@localhost//'
result_url ='rpc://'

task_routes = {
    'tasks.add': {'queue': 'add'}
}