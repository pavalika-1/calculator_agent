def success_condition(state):
    # Example success condition
    return state["stage"] == "act"


def agent_loop(max_iters=10):

    state = {
        "done": False,
        "stage": "start"
    }

    for i in range(max_iters):

        # Observe
        state["stage"] = "observe"
        print("Observe")

        # Decide
        state["stage"] = "decide"
        print("Decide")

        # Act
        state["stage"] = "act"
        print("Act")

        # Success -> terminate
        if success_condition(state):
            state["done"] = True
            state["stage"] = "success"
            return "success", state

    # Max iterations -> terminate with failure
    state["done"] = True
    state["stage"] = "failure"
    return "failure", state


result, state = agent_loop()

print("Result:", result)
print("State:", state)