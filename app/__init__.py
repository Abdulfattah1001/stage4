from flask import Flask
from flask import request, jsonify
from tasks import add
from tasks import sendMail
from tasks import logMessage

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    if 'sendmail' in request.args:
        email = request.args.get('sendmail')
        #state = sendMail.delay()
        state = sendMail.apply_async(args=[email])
        return jsonify({
            "result":state.id,
            "status":"message queued"
            })
    elif 'talktome' in request.args:
        state = logMessage.delay()
        return "Message logged"
    else:
        return "Welcome to Flask App"
    

@app.route("/status/<task_id>")
def task_status(task_id):
    task = sendMail.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state':task.state,
            'status':
            'Pending...'
        }
        return response
    else:
        return "Not yet implemented"
    

app.run(debug=True)