from flask import Flask, render_template
from simulator import DeadlockSimulator
from graph import draw_graph

app = Flask(__name__)
sim = DeadlockSimulator()

running = False

@app.route('/')
def index():
    return render_template('index.html')

# ---------------- CONTROL ----------------
@app.route('/start')
def start():
    global running
    running = True
    return "Simulation Started"

@app.route('/stop')
def stop():
    global running
    running = False
    return "Simulation Stopped"

@app.route('/reset')
def reset():
    sim.reset()
    return "Simulation Reset"

# ---------------- STEPS ----------------
@app.route('/step1')
def step1():
    sim.allocate_resource("P1", "R1")
    return "P1 allocated R1"

@app.route('/step2')
def step2():
    sim.allocate_resource("P2", "R2")
    return "P2 allocated R2"

@app.route('/step3')
def step3():
    sim.request_resource("P1", "R2")
    return "P1 requested R2"

@app.route('/step4')
def step4():
    sim.request_resource("P2", "R1")
    return "P2 requested R1"

# ---------------- GRAPH ----------------
@app.route('/graph')
def graph():
    draw_graph(sim.allocation, sim.request)
    return "Graph Displayed"

# ---------------- STATUS ----------------
@app.route('/status')
def status():
    return sim.get_status()

# ---------------- PREVENTION ----------------
@app.route('/prevent/mutual')
def prevent_mutual():
    sim.break_mutual_exclusion()
    return sim.get_status()

@app.route('/prevent/holdwait')
def prevent_holdwait():
    sim.break_hold_and_wait()
    return sim.get_status()

@app.route('/prevent/preemption')
def prevent_preemption():
    sim.break_no_preemption()
    return sim.get_status()

@app.route('/prevent/circular')
def prevent_circular():
    sim.break_circular_wait()
    return sim.get_status()

if __name__ == '__main__':
    app.run(debug=True)