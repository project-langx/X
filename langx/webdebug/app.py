from flask import Flask, request, render_template, jsonify, session

from .methods import get_tokens_and_source, get_ast_and_source, get_opcodes_and_source


# Instantiate flask app
app = Flask(__name__)

# Basic config for flask app
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "my-secret-key"
app.config["SESSION_TYPE"] = "filesystem"


@app.route("/", methods=["GET"])
def index():

    if request.method == "GET":
        return render_template("index.html")


@app.route("/generate-tokens", methods=["GET", "POST"])
def generate_tokens():

    if request.method == "GET":
        source_lines = []
        token_lines = []

        for source in session.get("source_tokens"):
            source_lines.append(source['source'])

        for tokens in session.get("source_tokens"):
            token_lines.append("<br>".join(tokens['tokens']))

        return render_template(
            "tokens.html", source_lines=source_lines, token_lines=token_lines
        )

    elif request.method == "POST":
        file_path = request.form["file_path"]

        source_tokens = get_tokens_and_source(file_path=file_path)

        session["source_tokens"] = source_tokens

        return jsonify({"status": "Success", "url": "/generate-tokens"})


@app.route("/get-tokens", methods=["POST"])
def get_tokens():

    if request.method == "POST":
        data = request.get_json()
        file_path = data["file_path"]

        source_tokens = get_tokens_and_source(file_path=file_path)

        return jsonify({"source_tokens": source_tokens})


@app.route("/generate-ast", methods=["GET", "POST"])
def generate_ast():

    if request.method == "GET":
        return render_template(
            "ast.html", source=session.get("source"), ast=session.get("ast")
        )
    elif request.method == "POST":
        file_path = request.form["file_path"]

        ast, source = get_ast_and_source(file_path=file_path)

        session["source"] = source
        session["ast"] = ast

        return jsonify({"status": "Success", "url": "/generate-ast"})


@app.route("/get-ast", methods=[ "POST"])
def get_ast():

    if request.method == "POST":
        data = request.get_json()
        file_path = data["file_path"]

        ast, source = get_ast_and_source(file_path=file_path)

        return jsonify({"ast": ast, "source": source})


@app.route("/generate-bytecode", methods=["GET", "POST"])
def generate_bytecode():

    if request.method == "GET":
        return render_template(
            "bytecode.html",
            source=session.get("source"),
            bytecode=session.get("bytecode"),
        )
    elif request.method == "POST":
        file_path = request.form["file_path"]

        opcodes, source = get_opcodes_and_source(file_path=file_path)

        session["source"] = source
        session["bytecode"] = "<br>".join([str(opcode) for opcode in opcodes])

        return jsonify({"status": "Success", "url": "/generate-bytecode"})


@app.route("/get-bytecode", methods=["POST"])
def get_bytecode():

    if request.method == "POST":
        data = request.get_json()
        file_path = data["file_path"]

        opcodes, source = get_opcodes_and_source(file_path=file_path)

        return jsonify({"bytecode": opcodes, "source": source})
