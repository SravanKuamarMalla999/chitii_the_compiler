from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.json.get('code')
    if not code:
        return jsonify({'error': 'No code provided'}), 400

    # Save input code to a file your compiler expects
    with open('program.txt', 'w') as f:
        f.write(code)

    # Run your compiler (adjust if needed)
    result = subprocess.run(['python', '-m', 'build.main'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        return jsonify({'error': result.stderr})

    # Compile LLVM IR to executable
    clang_result = subprocess.run(['clang', 'program.ll', '-o', 'program.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if clang_result.returncode != 0:
        return jsonify({'error': clang_result.stderr})

    # Run executable and collect output
    exec_result = subprocess.run(['./program.exe'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    return jsonify({'output': exec_result.stdout, 'error': exec_result.stderr})

if __name__ == "__main__":
    app.run(debug=True)
