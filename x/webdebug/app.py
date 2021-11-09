from flask import Flask, request, render_template, jsonify, session

from ..tokenizer.tokenizer import Tokenizer
from ..parser.parser import Parser
from ..utils.tree_walker import TreeWalker
from ..compiler.compiler import Compiler


# Instantiate flask app
app = Flask(__name__)

# Basic config for flask app
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.secret_key = "my-secret-key"
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/", methods=['GET'])
def index():

    if request.method == "GET":
        return render_template("index.html")

@app.route("/generate-tokens", methods=['GET', 'POST'])
def generate_tokens():

    if request.method == "GET":
        source_lines = session.get("source").split("\n")
        token_lines = []
        token_line = ""
        current_line_number = 1
        for token in session.get("tokens"):
            if token[-1] == current_line_number:
                token_line += f"Token(type={token[0]}, dtype={token[1]}, value={token[2]}, line_num={token[3]})<br>"
            else:
                token_lines.append(token_line)
                token_line = ""
                current_line_number += 1
                token_line += f"Token(type={token[0]}, dtype={token[1]}, value={token[2]}, line_num={token[3]})<br>"


        return render_template("tokens.html", source_lines=source_lines, token_lines=token_lines)

    elif request.method == "POST":
        file_path = request.form['file_path']

        with open(file_path, "r") as f:
            source = f.read()

        tokens = Tokenizer(source).generate_tokens()
        session['source'] = source
        session['tokens'] = tokens

        return jsonify({"status": "Success", "url": "/generate-tokens"})

@app.route("/generate-ast", methods=['GET', 'POST'])
def generate_ast():

    if request.method == "GET":
        return render_template("ast.html", source=session.get('source'), ast=session.get("ast"))
    elif request.method == "POST":
        file_path = request.form['file_path']

        with open(file_path, "r") as f:
            source = f.read()

        tokens = Tokenizer(source).generate_tokens()
        ast_root = Parser(tokens).parse()
        ast = TreeWalker(ast_root).walk()
        session['source'] = source
        session['ast'] = ast

        return jsonify({"status": "Success", "url": "/generate-ast"})

@app.route("/generate-bytecode", methods=['GET', 'POST'])
def generate_bytecode():

    if request.method == "GET":
        return render_template("bytecode.html", source=session.get('source'), bytecode=session.get("bytecode"))
    elif request.method == "POST":
        file_path = request.form['file_path']

        with open(file_path, "r") as f:
            source = f.read()

        tokens = Tokenizer(source).generate_tokens()
        ast_root = Parser(tokens).parse()
        opcodes = Compiler(ast_root).compile()
        session['source'] = source
        session['bytecode'] = "<br>".join([str(opcode) for opcode in opcodes])

        return jsonify({"status": "Success", "url": "/generate-bytecode"})
