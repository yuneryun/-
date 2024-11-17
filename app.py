from flask import Flask, render_template, request, jsonify
from analog_converter import analog_convert
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        input_value = float(data['input_value'])
        input_min = float(data['input_min'])
        input_max = float(data['input_max'])
        output_min = float(data['output_min'])
        output_max = float(data['output_max'])
        
        result = analog_convert(input_value, input_min, input_max, output_min, output_max)
        return jsonify({'result': round(result, 3)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/random', methods=['POST'])
def random_convert():
    try:
        data = request.get_json()
        output_type = data['output_type']  # 'current' 或 'voltage'
        
        # 生成随机范围和值
        min_val = round(random.uniform(-100, 100), 2)
        max_val = round(min_val + random.uniform(10, 200), 2)
        current_val = round(random.uniform(min_val, max_val), 2)
        
        # 根据输出类型设置输出范围
        output_min = 4 if output_type == 'current' else 0
        output_max = 20 if output_type == 'current' else 10
        
        result = analog_convert(current_val, min_val, max_val, output_min, output_max)
        
        return jsonify({
            'input_min': min_val,
            'input_max': max_val,
            'input_value': current_val,
            'result': round(result, 3)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 