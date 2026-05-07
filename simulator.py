class DeadlockSimulator:
    def __init__(self):
        self.processes = ["P1", "P2"]
        self.resources = ["R1", "R2"]

        self.reset()

    def reset(self):
        self.allocation = {"P1": [], "P2": []}
        self.request = {"P1": [], "P2": []}
        self.mode = "NONE"

    # ---------------- BASIC OPS ----------------
    def request_resource(self, p, r):
        self.request[p].append(r)

    def allocate_resource(self, p, r):
        if r not in self.allocation[p]:
            self.allocation[p].append(r)
            if r in self.request[p]:
                self.request[p].remove(r)

    # ---------------- DEADLOCK CHECK ----------------
    def detect_deadlock(self):
        if ("R2" in self.request["P1"] and
            "R1" in self.request["P2"]):
            return True
        return False

    # ---------------- PREVENTION TECHNIQUES ----------------

    def break_mutual_exclusion(self):
        self.mode = "Mutual Exclusion Broken"
        self.allocation["P1"] = ["R1", "R2"]
        self.allocation["P2"] = ["R1", "R2"]
        self.request = {"P1": [], "P2": []}

    def break_hold_and_wait(self):
        self.mode = "Hold & Wait Broken"
        self.allocation = {"P1": [], "P2": []}

    def break_no_preemption(self):
        self.mode = "No Preemption Broken"
        self.allocation["P2"] = []

    def break_circular_wait(self):
        self.mode = "Circular Wait Broken"
        self.request["P2"] = []

    # ---------------- STATUS ----------------
    def get_status(self):
        if self.detect_deadlock():
            return f"❌ DEADLOCK DETECTED | Mode: {self.mode}"
        else:
            return f"✅ NO DEADLOCK | Mode: {self.mode}"