from microbit import *
import servo

# 서보 모터 핀 설정
servo_pin_tilt = pin0
servo_pin_up_down = pin1
servo_pin_left_right = pin2

# 서보 모터 객체 생성
servo_tilt = servo.Servo(servo_pin_tilt)
servo_up_down = servo.Servo(servo_pin_up_down)
servo_left_right = servo.Servo(servo_pin_left_right)

# 각도 및 위치 조절 범위 설정 (0~180도 사이)
min_tilt = 0
max_tilt = 90
min_position = 0
max_position = 180

# 경사도를 조절하는 함수 정의
def adjust_tilt(target_tilt):
    if target_tilt < min_tilt:
        target_tilt = min_tilt
    elif target_tilt > max_tilt:
        target_tilt = max_tilt
    servo_tilt.write_angle(target_tilt)

# 상하 이동을 조절하는 함수 정의
def adjust_height(target_height):
    if target_height < min_position:
        target_height = min_position
    elif target_height > max_position:
        target_height = max_position
    servo_up_down.write_angle(target_height)

# 좌우 이동을 조절하는 함수 정의
def adjust_position(target_position):
    if target_position < min_position:
        target_position = min_position
    elif target_position > max_position:
        target_position = max_position
    servo_left_right.write_angle(target_position)

# 사용자가 원하는 경사도, 높이 및 위치 설정
target_tilt = 45  # 예시로 45도로 설정
target_height = 90  # 예시로 중간 높이로 설정
target_position = 90  # 예시로 중간 위치로 설정

# 책상의 경사도, 높이 및 위치 조절
adjust_tilt(target_tilt)
adjust_height(target_height)
adjust_position(target_position)

# 경사도, 높이 및 위치를 주기적으로 변경하여 조절
while True:
    if button_a.is_pressed():
        target_tilt += 5
        if target_tilt > max_tilt:
            target_tilt = max_tilt
        adjust_tilt(target_tilt)
        display.scroll("Tilt: " + str(target_tilt))
        
    if button_b.is_pressed():
        target_tilt -= 5
        if target_tilt < min_tilt:
            target_tilt = min_tilt
        adjust_tilt(target_tilt)
        display.scroll("Tilt: " + str(target_tilt))
    
    # 상하 이동 및 좌우 이동은 버튼을 추가로 구현하여 제어 가능
    sleep(200)
    