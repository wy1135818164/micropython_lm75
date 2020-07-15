# micropython_lm75
读取lm75温度传感器、设置过热关断阈值和滞后阈值，支持读取温度和设置温度小于0℃

# 方法
- 获取温度：lm75.get_temp()
- 设置过热关断阈值和滞后阈值：lm75.set_os(25.5)/lm75.set_os(25.5,23)

# 例程
```python
if __name__=='__main__':
    from machine import Pin, I2C
    i2c = I2C(scl=Pin(23), sda=Pin(22))
    lm75=LM75(i2c)
    #获取lm75温度
    print(lm75.get_temp())
    #设置过热关断阈值为25.5℃
    lm75.set_os(25.5)
```
