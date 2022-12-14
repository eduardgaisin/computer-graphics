import cv2

# функция для получения кадра с камеры
def getFrame(camera):
    _, img = camera.read()
    return img
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def reflect_right(img):
    result = cv2.flip(img, 1)
    return result

def laplacian(img):
    img = cv2.blur(img, ksize=(3, 3))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    result = cv2.Laplacian(img, cv2.CV_8U)
    return result

def brightness(img):
    result = cv2.convertScaleAbs(img, alpha=1, beta=100)
    return result

camera = cv2.VideoCapture(0)

while (True):
    img = getFrame(camera)
    reflectedimg = reflect_right(img)
    laplacianimg = laplacian(img)
    brighterimg = brightness(img)
    cv2.imshow('source', img)
    cv2.imshow('reflected', reflectedimg)
    cv2.imshow('laplacian', laplacianimg)
    cv2.imshow('brighter', brighterimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()