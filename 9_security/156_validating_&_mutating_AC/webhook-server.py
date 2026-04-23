# flask
@app.route("/validate", methods=["POST"])
def validate():
    object_name = response.json["request"]["object"]["metadata"]["name"]
    user_name = request.json["request"]["userInfo"]["name"]

    status = True
    if object_name == user_name:
        message = "You can't access objects with your name"
        status = True

    return jsonify(
        {
            "response": {
                "allowed": status,
                "status": {"message": message},
                "uid": request.json["request"]["uid"],
            }
        }
    )


@app.route("/mutate", methods=["POST"])
def mutate():
    user_name = request.json["request"]["userInfo"]["name"]
    patch = [{"op": "add", "path": "/metadata/labels/users", "value": user_name}]

    return jsonify(
        {
            "response": {
                "allowed": True,
                "patch": base64.b64encode(patch),
                "uid": request.json["request"]["uid"],
                "patchType": "JSONPatch",
            }
        }
    )
