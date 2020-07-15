from machine import Pin, I2C

class LM75:
    def __init__(self,i2c,add=0x48):
        self.i2c=i2c
        self.i2c_add=add
    #获取温度
    def get_temp(self):
        buf=self.i2c.readfrom_mem(self.i2c_add, 0x00,2)
        data='%02x'%abs(buf[0])+'%02x'%abs(buf[1])
        if (int(data,16)>>5)<1024:
            temp=(int(data,16)>>5)*0.125
        else:
            temp=((int(data,16)>>5)-2048)*0.125
        return temp
    #设置过热关断阈值(data_H)和滞后(data_L)
    def set_os(self,data_H,*data_L):
        if(len(data_L)==0):
            data_L=data_H
        else:
            data_L=data_L[0]
        print(data_H,data_L)
        if(data_H>0):
            self.i2c.writeto_mem(self.i2c_add,3,(int(data_H*2)<<7).to_bytes(2,'little'))
        else:
            self.i2c.writeto_mem(self.i2c_add,3,(int(data_H*2)+512<<7).to_bytes(2,'little'))
        if(data_L>0):
            self.i2c.writeto_mem(self.i2c_add,2,(int(data_L*2)<<7).to_bytes(2,'little'))
        else:
            self.i2c.writeto_mem(self.i2c_add,2,(int(data_L*2)+512<<7).to_bytes(2,'little'))

if __name__=='__main__':
    i2c = I2C(scl=Pin(23), sda=Pin(22))
    lm75=LM75(i2c)
    #获取lm75温度
    print(lm75.get_temp())
    #设置过热关断阈值为25.5℃
    lm75.set_os(25.5)