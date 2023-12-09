import pigpio
import threading

class LedController:   
      
    def __init__(self, red, green, blue):
        self.controller = pigpio.pi()
        
        self._red_pin = red
        self._green_pin = green
        self._blue_pin = blue
            
    def turnoff(self):
        for pin in [self._red_pin, self._green_pin, self._blue_pin]:
            self.controller.set_PWM_dutycycle(pin, 0)
            
    def set_val(self, pin, value):
        self.controller.set_PWM_dutycycle(pin, value)
        
    def get_val(self, pin):
        return self.controller.get_PWM_dutycycle(pin)
    
    def get_rgb(self):
        r = self.controller.get_PWM_dutycycle(self._red_pin)
        g = self.controller.get_PWM_dutycycle(self._green_pin)
        b = self.controller.get_PWM_dutycycle(self._blue_pin)
        return r, g, b
    
    def switch(self, pin):
        self.set_val(pin, 255 - self.get_val(pin))
    