from flask import Flask, render_template
from mcstatus import MinecraftServer

app = Flask(__name__)


@app.route("/")



def status():
    server = MinecraftServer.lookup("mc.redditmc.com")
    status = server.status()
    name = "The server has {0} players and replied in {1} ms".format(status.players.online, status.latency)


    return render_template('index.html', name=name)





if __name__ == "__main__":
    app.run(debug=True)
