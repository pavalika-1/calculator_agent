state = {
    "done": False,
    "stage": 0
}

max_iters = 10

for i in range(max_iters):
    print(f"Iteration: {i + 1}")

    # Observe
    print("Observe")

    # Decide
    print("Decide")

    # Act
    print("Act")

    state["stage"] += 1

    # Example stopping condition
    if state["stage"] == 3:
        state["done"] = True

    if state["done"]:
        print("Success")
        break
else:
    print("Failure: Maximum iterations exceeded")

print(state)