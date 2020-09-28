import pyttsx3,cv2, os, webbrowser, time, random2, speech_recognition as sr, numpy as np
from antcer import aixa, aixa_sof
from selenium import webdriver


#hacer funcion para comparar rostro 
user = open('quest_usuario.txt')
bo = open ('bot.txt')
https = open('links.txt')
dial  = open('dialogo.txt')
dialogo_aray = []
usuario_aray = []
bot_aray = []
links = []
hand_hist = None
traverse_point = []
total_rectangle = 9
hand_rect_one_x = None
hand_rect_one_y = None
hand_rect_two_x = None
hand_rect_two_y = None
engine = pyttsx3.init()
av_virtual = "AIXA"
usuario_name = "YOU"



def nombre():
    os.system('cls')
    global usuario_name, av_virtual
    print("Welcome to")
    aixa()
    print("> Aixa is a virtual assistant.")
    print("> The origin of the program is to create an interaction between machine and human.")
    print("> Was created on August 7 at 1:20 am 2020.")
    print("> Features: +Voice recognition")
    print("            +Open desktop app")
    print("            +Conversational experience")
    print("            +Search in the browser")
    print("            +Object tracking")
    print("            +Time of the place where it is")
    print("            +Control of social networks or web")
    print("            ++Soon detect if two faces are the same")
    print()
    usuario_name = str(input("Enter your name: ")).upper()
    nombre_aixa = str(input("Assign name to V.A yes or no: ")).lower()
    if (nombre_aixa == str("si")) or (nombre_aixa == str("yes")):
        nombre = str(input("Enter the name of the V.A: ")).upper()
        av_virtual = f"{nombre} AIXA"
    if nombre_aixa == str("no"):
        av_virtual = av_virtual



def present_ai():
    os.system('cls')
    print("Welcome to")
    aixa()
    print()
    print(f"                                   {time.asctime()}")
    engine.say(f'bienvenido {usuario_name}')
    engine.say(f'que desea hacer hoy')
    engine.runAndWait()
    print()



nombre()
voice_tex = int(input("Ingrese 1 para Hablar Y 2 para Escribir:"))
present_ai()



def configuracion_voz():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    _volume = engine.getProperty('volume') 
    engine.setProperty('volume',10.0)



def crear_array():
    for _uo in range(26):
        user_read = user.readline()
        user_read = user_read.replace('\n',"")
        user_read = user_read.upper()
        user_read = user_read.split()
        usuario_aray.append(user_read)
    for _bt in range(len(usuario_aray)):
        bo_read = bo.readline()
        bo_read = bo_read.replace('\n',"")
        bo_read = bo_read.split()
        bot_aray.append(bo_read)
    for _lk in range(10):
        https_read = https.readline()
        https_read = https_read.replace('\n',"")
        https_read = https_read.split()
        links.append(https_read)
    for _dg in range(5):
        dialogo = dial.readline()
        dialogo = dialogo.replace('\n',"")
        dialogo = dialogo.split()
        dialogo_aray.append(dialogo)


crear_array()


def inicio():
    configuracion_voz()
    if voice_tex == 2:
        texto()
    if voice_tex == 1:
        reconocimento_voz()



def texto():
    oracion_usuario = str(input(f"{usuario_name}: ")).upper()
    control_web(oracion_usuario)
    dialoggo()
    fin(oracion_usuario)
    oracion_array_user = oracion_usuario.split()
    comparacion_tex_voice(oracion_array_user)



def reconocimento_voz():
    r = sr.Recognizer() 
    while True:
        with sr.Microphone() as voz:
            print('Habla cualquier cosa : ')
            audio = r.listen(voz)
            try:
                text = r.recognize_google(audio, language= 'es-ES').upper()
                oracion_voice = text.split()
            except:
                print(f"{av_virtual}: No te escuche")
                continue
            print()
            fin(text)
            print(f"{usuario_name}: {text}")
            comparacion_tex_voice(oracion_voice)



def comparacion_tex_voice(array_tex_voice):
    for j, k in zip(range(len(usuario_aray)), range(len(bot_aray))):
        for l in range(len(usuario_aray[j])):
            usu_ar = usuario_aray[j][l]
            bot = bot_aray[k][:]
            for oracion in array_tex_voice:
                if oracion == usu_ar:
                    bo =' '.join(bot)
                    print(f"{av_virtual}: {bo}")
                    engine.say(f'{bo} ')
                    engine.runAndWait()
                    abrir_apps(usuario_aray[j][l])
                    navegar_web(usuario_aray[j][l], array_tex_voice)
                    j, k, l, bot = 0, 0, 0, 0



def dialoggo():
    num1 = random2.sample(range(0,4),1)
    num1 = num1[0]
    if (num1 > 0) or (num1 <= 5):
        saludo = dialogo_aray[num1] 
        bot_aray[0] = saludo



def abrir_apps(clave_tex_voice):
    if clave_tex_voice == str(usuario_aray[9][0]):
        os.system('win32calc.exe')
    if clave_tex_voice == str(usuario_aray[11][0]):
        os.system('notepad.exe')
    if clave_tex_voice == str(usuario_aray[25][0]):
        vision_articial()



def navegar_web(clave_tex_voice, search):
    if clave_tex_voice == str(usuario_aray[8][0]):
        buscar = " ".join(search[1:])
        webbrowser.open_new_tab(f"{links[0][0]}{buscar}")
    if clave_tex_voice == str(usuario_aray[12][0]):
        musica = " ".join(search[2:])
        webbrowser.open_new_tab(f"{links[1][0]}{musica}")
    if clave_tex_voice == str(usuario_aray[14][0]):#w
        webbrowser.open_new_tab(f"{links[2][0]}")
    if clave_tex_voice == str(usuario_aray[16][0]):#ins
        webbrowser.open_new_tab(f"{links[3][0]}")
    if clave_tex_voice == str(usuario_aray[17][0]):#fac
        webbrowser.open_new_tab(f"{links[4][0]}")
    if clave_tex_voice == str(usuario_aray[15][0]):#twi
        webbrowser.open_new_tab(f"{links[5][0]}")
    if clave_tex_voice == str(usuario_aray[18][0]):#vk
        webbrowser.open_new_tab(f"{links[6][0]}")
    if clave_tex_voice == str(usuario_aray[19][0]):#git
        webbrowser.open_new_tab(f"{links[7][0]}")
    if clave_tex_voice == str(usuario_aray[20][0]):#cola
        webbrowser.open_new_tab(f"{links[8][0]}")



def fin(clave_tex_voice):
    if clave_tex_voice == str("CHAO") or clave_tex_voice == str("NADA"):
        os.system('cls')
        #print("            VA. AIXA  THURSDAY 7/AGOST/20 1:30am")
        print()
        engine.say(f'hasta mañana {usuario_name}')
        engine.runAndWait()
        aixa_sof()
        print('© 2020 AIXA SOFTWARE, INC.')
        print("From ISAAC ANTEPARA CEREZO")
        time.sleep(1)
        exit()



def rescale_frame(frame, wpercent=130, hpercent=130):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)



def contours(hist_mask_image):
    gray_hist_mask_image = cv2.cvtColor(hist_mask_image, cv2.COLOR_BGR2GRAY)
    _ret, thresh = cv2.threshold(gray_hist_mask_image, 0, 225, 0)
    cont, _hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return cont



def draw_rect(frame):
    rows, cols, _ = frame.shape
    global total_rectangle, hand_rect_one_x, hand_rect_one_y, hand_rect_two_x, hand_rect_two_y
    hand_rect_one_x = np.array(
        [6 * rows / 20, 6 * rows / 20, 6 * rows / 20, 9 * rows / 20, 9 * rows / 20, 9 * rows / 20, 12 * rows / 20,
         12 * rows / 20, 12 * rows / 20], dtype=np.uint32)
    hand_rect_one_y = np.array(
        [9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20, 10 * cols / 20, 11 * cols / 20, 9 * cols / 20,
         10 * cols / 20, 11 * cols / 20], dtype=np.uint32)
    hand_rect_two_x = hand_rect_one_x + 10
    hand_rect_two_y = hand_rect_one_y + 10
    for i in range(total_rectangle):
        cv2.rectangle(frame, (hand_rect_one_y[i], hand_rect_one_x[i]),
                      (hand_rect_two_y[i], hand_rect_two_x[i]),
                      (179, 113, 34), 2)
    return frame



def hand_histogram(frame):
    global hand_rect_one_x, hand_rect_one_y
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    roi = np.zeros([90, 10, 3], dtype=hsv_frame.dtype)
    for i in range(total_rectangle):
        roi[i * 10: i * 10 + 10, 0: 10] = hsv_frame[hand_rect_one_x[i]:hand_rect_one_x[i] + 10,
                                          hand_rect_one_y[i]:hand_rect_one_y[i] + 10]
    hand_hist = cv2.calcHist([roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    return cv2.normalize(hand_hist, hand_hist, 0, 255, cv2.NORM_MINMAX)



def hist_masking(frame, hist):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0, 1], hist, [0, 180, 0, 256], 1)
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))
    cv2.filter2D(dst, -1, disc, dst)
    _ret, thresh = cv2.threshold(dst, 150, 255, cv2.THRESH_BINARY)
    thresh = cv2.merge((thresh, thresh, thresh))
    return cv2.bitwise_and(frame, thresh)



def centro_objetp(max_contour):
    moment = cv2.moments(max_contour)
    if moment['m00'] != 0:
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        return cx, cy
    else:
        return None



def farthest_point(defects, contour, centroid):
    if defects is not None and centroid is not None:
        s = defects[:, 0][:, 0]
        cx, cy = centroid
        x = np.array(contour[s][:, 0][:, 0], dtype=np.float)
        y = np.array(contour[s][:, 0][:, 1], dtype=np.float)
        xp = cv2.pow(cv2.subtract(x, cx), 2)
        yp = cv2.pow(cv2.subtract(y, cy), 2)
        dist = cv2.sqrt(cv2.add(xp, yp))
        dist_max_i = np.argmax(dist)
        if dist_max_i < len(s):
            farthest_defect = s[dist_max_i]
            farthest_point = tuple(contour[farthest_defect][0])
            return farthest_point
        else:
            return None



def draw_circles(frame, traverse_point):
    if traverse_point is not None:
        for i in range(len(traverse_point)):
            cv2.circle(frame, traverse_point[i], int(5 - (5 * i * 3) / 100), [0, 255, 255], -1)



def gestion_imagen(frame, hand_hist):
    hist_mask_image = hist_masking(frame, hand_hist)
    hist_mask_image = cv2.erode(hist_mask_image, None, iterations=2)
    hist_mask_image = cv2.dilate(hist_mask_image, None, iterations=2)
    contour_list = contours(hist_mask_image)
    max_cont = max(contour_list, key=cv2.contourArea)
    cnt_centroid = centro_objetp(max_cont)
    cv2.circle(frame, cnt_centroid, 80, [0, 225, 0],3)
    if max_cont is not None:
        hull = cv2.convexHull(max_cont, returnPoints=False)
        defects = cv2.convexityDefects(max_cont, hull)
        far_point = farthest_point(defects, max_cont, cnt_centroid)
        #print("Centroid : " + str(cnt_centroid) + ", farthest Point : " + str(far_point))
        cv2.circle(frame, far_point, 5, [0, 0, 225], 2)
        if len(traverse_point) < 20:
            traverse_point.append(far_point)
        else:
            traverse_point.pop(0)
            traverse_point.append(far_point)
        draw_circles(frame, traverse_point)



def vision_articial():
    global hand_hist
    is_hand_hist_created = False
    capture = cv2.VideoCapture(0)
    while capture.isOpened():
        pressed_key = cv2.waitKey(1)
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        if pressed_key & 0xFF == ord('q'):
            is_hand_hist_created = True
            hand_hist = hand_histogram(frame)
        if is_hand_hist_created:
            gestion_imagen(frame, hand_hist)
        else:
            frame = draw_rect(frame)
        cv2.imshow("Artificial vision AIXA", rescale_frame(frame))
        if pressed_key == 27:   
            break
    cv2.destroyAllWindows()
    capture.release()



def control_web(clave_tex_voice):
    abrir_chrome = 'E:/Descargas/chromedriver_win32/chromedriver.exe'
    if clave_tex_voice == str("M"):
        enviar_messeger(abrir_chrome)
    if clave_tex_voice == str("I"):
        abrir_faceb(abrir_chrome)



def enviar_messeger(abrir_chrome):
    usuario_web = input("Email: ")
    contrasena = input("Password: ")
    navegador = webdriver.Chrome(abrir_chrome)
    navegador.get(f"{links[9][0]}")
    time.sleep(1)
    id_ususio = navegador.find_element_by_name('email')
    id_contrase = navegador.find_element_by_name('pass')
    id_ususio.send_keys(usuario_web)
    id_contrase.send_keys(contrasena)
    time.sleep(1)
    boton_iniciar = navegador.find_element_by_name('login')
    boton_iniciar.click()
    navegador.quit()



def abrir_faceb(abrir_chrome):
    usuario_web = input("Email: ")
    contrasena = input("Contraseña: ")
    navegador = webdriver.Chrome(abrir_chrome)
    navegador.get(f"{links[3][0]}")
    time.sleep(1)
    id_ususio = navegador.find_element_by_name('username')
    id_contrase = navegador.find_element_by_name('password')
    id_ususio.send_keys(usuario_web)
    id_contrase.send_keys(contrasena)
    time.sleep(1)
    boton_iniciar = navegador.find_element_by_class_name("sqdOP  L3NKy   y3zKF     ")
    boton_iniciar.click()
#revisar button de instag




while True:
    inicio()
