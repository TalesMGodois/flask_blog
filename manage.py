import os, sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_blog import app

manager = Manager(app)

manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'),
    port = int(os.getenv('PORT', 3000)))
)

@manager.command
def run_server():
    return Server(
        use_debugger = True,
        use_reloader = True,
        host = os.getenv('IP', '0.0.0.0'),
        port = int(os.getenv('PORT', 3000))
    )

if __name__ == '__main__':
        manager.run()
