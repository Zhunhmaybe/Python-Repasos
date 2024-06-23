import cv2

def main():
    # Cargar el archivo de cascada de Haar para la detección de rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Iniciar la cámara
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: No se puede abrir la cámara")
        return

    while True:
        # Captura frame por frame
        ret, frame = cap.read()
        if not ret:
            print("No se recibió el frame. Saliendo ...")
            break

        # Convertir el frame a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detectar rostros
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Dibujar un rectángulo alrededor de los rostros detectados
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Muestra el frame resultante
        cv2.imshow('frame', frame)

        # Rompe el bucle al presionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cuando todo esté listo, libera la captura
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
