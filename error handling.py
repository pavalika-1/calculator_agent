#handle invalid action:return error dict
def agent(action):
    if action == "observe":
        return {"status": "success", "message": "Observation completed"}

    elif action == "act":
        return {"status": "success", "message": "Action completed"}

    else:
        return {
            "status": "error",
            "message": "Invalid action"
        }


print(agent("observe"))
print(agent("jump"))
