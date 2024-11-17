def analog_convert(input_value, input_min, input_max, output_min, output_max):
    """
    将输入的模拟量从一个范围映射到另一个范围
    
    参数:
        input_value: 输入的模拟量值
        input_min: 输入范围的最小值
        input_max: 输入范围的最大值
        output_min: 输出范围的最小值
        output_max: 输出范围的最大值
    
    返回:
        映射后的值
    """
    # 确保输入值在范围内
    input_value = max(min(input_value, input_max), input_min)
    
    # 计算输入范围和输出范围
    input_span = input_max - input_min
    output_span = output_max - output_min
    
    # 计算缩放因子
    scale_factor = float(output_span) / float(input_span)
    
    # 进行转换
    return output_min + (input_value - input_min) * scale_factor

# 使用示例
if __name__ == "__main__":
    # 示例1：将0-5V的信号转换为4-20mA
    voltage = 2.5  # 输入电压
    current = analog_convert(voltage, 0, 5, 4, 20)
    print(f"电压 {voltage}V 转换为电流: {current}mA")
    
    # 示例2：将0-1023的ADC值转换为0-5V
    adc_value = 512
    voltage = analog_convert(adc_value, 0, 1023, 0, 5)
    print(f"ADC值 {adc_value} 转换为电压: {voltage}V") 