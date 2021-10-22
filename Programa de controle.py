# Python Script
# Controle do Robo-Camera


#import das bibliotecas GPIO,time e pygame
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from time import sleep
import pygame

#inicializa pygame
pygame.init()

#Define tamanho da janela do pygame em 100x100
win = pygame.display.set_mode((100,100))


#Import da biblioteca do PCA9685
from adafruit_servokit import ServoKit    
nbPCAServo=16 
pca = ServoKit(channels=16)

#habilita canal 1(0) para servo 1
pca.servo[0].set_pulse_width_range(500 , 2500) #SERVO 1

#habilita canal 1(1) para servo 2
pca.servo[3].set_pulse_width_range(500 , 2500) #SERVO 2


#função para controle de posição do motor servo 1 - RECEBE VALOR INTEIRO (ANGULO 0 A 180)
def look(pos): # control servo 1
    pca.servo[0].angle = pos
    sleep(0.01)
    



#MOTOR A ==========================
#MOTOR Direito
#Pinos no l298n - raspberri pi
in1 = 24 
in2 = 23
en = 25

#pinos definidos como OUTPUT
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
pA=GPIO.PWM(en,1000) 
pA.start(30) #potência na ativação
#MOTOR A ==========================



#MOTOR B ==========================
#MOTOR Esquerdo
#Pinos no l298n - raspberri pi
inE1 = 5
inE2 = 6
en2 = 26
#GPIOs como OUTPUT
GPIO.setup(inE1,GPIO.OUT)
GPIO.setup(inE2,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(inE1,GPIO.LOW)
GPIO.output(inE2,GPIO.LOW)
pB=GPIO.PWM(en2,1000)
#potência na ativação
pB.start(30)



        
        
def FRENTE():
        #Motor Esquerdo
    pB.ChangeDutyCycle(30)
    GPIO.output(inE1,GPIO.HIGH)
    GPIO.output(inE2,GPIO.LOW)
        
        
        #Motor Direito
    pA.ChangeDutyCycle(30)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
    
    sleep(0.3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.LOW)
    

def FRENTETURBO():
        #ME
    pB.ChangeDutyCycle(90)
    GPIO.output(inE1,GPIO.HIGH)
    GPIO.output(inE2,GPIO.LOW)
        
        
        #MD
    pA.ChangeDutyCycle(90)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
        
    sleep(0.3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.LOW)
    
    
        
def GOBACK():
        #ME
    pB.ChangeDutyCycle(35)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.HIGH)
        
        
        #MD
    pA.ChangeDutyCycle(35)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    
        
    sleep(0.3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.LOW)
    
    
    
def TLEFT():
        #ME
    pB.ChangeDutyCycle(35)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.HIGH)
        
        
        #MD
    pA.ChangeDutyCycle(35)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    
        
    sleep(0.3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.LOW)
    



def TRIGHT():
        #ME
    pB.ChangeDutyCycle(35)
    GPIO.output(inE1,GPIO.HIGH)
    GPIO.output(inE2,GPIO.LOW)
        
        
        #MD
    pA.ChangeDutyCycle(35)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    
        
    sleep(0.3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.LOW)
#=======================================RE=
    


def TRIGHTHYPER():
        #ME
    pB.ChangeDutyCycle(70)
    GPIO.output(inE1,GPIO.HIGH)
    GPIO.output(inE2,GPIO.LOW)
        
        
        #MD
    pA.ChangeDutyCycle(70)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    
        
    sleep(0.3)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(inE1,GPIO.LOW)
    GPIO.output(inE2,GPIO.LOW)
#=======================================RE=










while True:
    for eve in pygame.event.get():pass
    keyInput = pygame.key.get_pressed()
    
    if keyInput [pygame.K_w]:
        print('UP')
        FRENTE()
        pygame.display.update()
    
    elif keyInput [pygame.K_h]:
        print('UPHYPER')
        FRENTETURBO()
        pygame.display.update()
    
    elif keyInput [pygame.K_z]:
        print('DOWN')
        GOBACK()
        pygame.display.update()
    
    elif keyInput [pygame.K_a]:
        print('LEFT')
        TLEFT()
        pygame.display.update()
    
    elif keyInput [pygame.K_d]:
        print('RIGHT')
        TRIGHT()
        pygame.display.update()
        
        
    elif keyInput [pygame.K_e]:
        print('LOOK_UP')
        look(40)
        pygame.display.update()
        
        
    elif keyInput [pygame.K_r]:
         print('LOOK_CENTER')
         look(80)
         pygame.display.update()
         
         
    elif keyInput [pygame.K_t]:
        print('LOOK_DOWN')
        look(120)
        pygame.display.update()
        
        
    elif keyInput [pygame.K_0]:
        print('TRIGH_HYPER')
        TRIGHTHYPER()
        pygame.display.update()

    
     







